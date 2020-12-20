Django & GitHub Actions = Continuous Deployment
===


## GitHub Actions が VPS へ ssh 接続してデプロイする

- ssh 公開鍵認証の用意をする

```bash
ssh-keygen

# ↓生成される。
# /Users/user/.ssh/id_rsa     -> GitHub secret へ登録
# /Users/user/.ssh/id_rsa.pub -> VPS のホームディレクトリに置く
```

- VPS 側で公開鍵認証の設定をする

```bash
cd
mkdir .ssh
chmod 700 .ssh/
mv id_rsa.pub .ssh/authorized_keys
chmod 600 .ssh/authorized_keys
```

- ローカルから秘密鍵指定でアクセスできることを確認(ssh コマンドについては sshnote へ)

```bash
ssh -i /Users/user/.ssh/id_rsa root@host
```

- VPS 側でパスワードログインを禁じる
- /etc/ssh/sshd_config を編集

```plaintext
PasswordAuthentication no
```

- GitHub Actions 用の yml を用意

```yaml
name: Python application

on:
  push:
    branches: [ master ]

env:
  SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK_URL }}

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Deployment
      run: |
        echo "$SECRET_KEY" > secret_key
        chmod 600 secret_key
        ssh -oStrictHostKeyChecking=no ${SERVER_USER}@${SERVER_HOST} -i secret_key "
        cd /vagrant/ &&
        git fetch origin &&
        git reset --hard origin/master &&
        sudo /env3.6/bin/python3.6 /vagrant/manage.py migrate --settings=config.settings.production &&
        sudo /env3.6/bin/python3.6 /vagrant/manage.py collectstatic -c --noinput --settings=config.settings.production &&
        sudo apachectl restart
        "
      env:
        SECRET_KEY: ${{ secrets.SECRET_KEY }}
        SERVER_USER: ${{ secrets.SERVER_USER }}
        SERVER_HOST: ${{ secrets.SERVER_HOST }}

    # 成功時はこちらのステップが実行されます。
    - name: Slack Notification on Success
      if: success()
      uses: rtCamp/action-slack-notify@v2.0.2
      env:
        SLACK_TITLE: Mrrhp deployment succeeded
        SLACK_COLOR: good

    # 失敗時はこちらのステップが実行されます。
    - name: Slack Notification on Failure
      uses: rtCamp/action-slack-notify@v2.0.2
      if: failure()
      env:
        SLACK_TITLE: Mrrhp deployment failed
        SLACK_COLOR: danger
```
