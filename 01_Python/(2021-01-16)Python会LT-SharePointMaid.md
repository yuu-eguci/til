yuu-eguci です
===

好きなものをお持ち帰りください。

- 「SharePoint 内のファイルをいつもいつも手動で更新するのがめんどうくさい」(お話したいこと 1/3)
- 「Django ブログをいつもいつも手動でデプロイするのがめんどうくさい」(お話したいこと 2/3)
- ここまできたら Linux だけでなくクラウドサービスへも自動デプロイします(お話したいこと 3/3)

## 「SharePoint 内のファイルをいつもいつも手動で更新するのがめんどうくさい」(お話したいこと 1/3)

SharePoint 内のファイルを Python で自動操作するプログラムを作りました。

- SharePoint: Office365 サービスに含まれる、ファイル保存サービス

![sharepoint](https://user-images.githubusercontent.com/28250432/104531230-0ae43600-5651-11eb-8734-1d0d41a9eea9.png)

![teams](https://user-images.githubusercontent.com/28250432/104531232-0cadf980-5651-11eb-864a-5c5fb00f6e65.png)

- ここにある Excel ファイルを定期的に更新していたのが面倒だったので自動化しました。
    - 具体的にはファイル内の1シートを複製して追加する、というようなこと。
- Python にお願いすることはつぎ↓のとおり。
- 詳細に興味のない方もおられると思うので、ざっくり流れをご紹介。

```python
import requests
import get_access_token
import get_file_info
import copy_xlsx_sheet
import put_file

# アクセストークン。
access_token = get_access_token.run()

# ファイル情報取得。
file_info = get_file_info.run(access_token)
file_id = file_info['id']
file_name = file_info['name']
download_url = file_info['@microsoft.graph.downloadUrl']

# ファイルダウンロード。
res = requests.get(download_url)
with open(f'./{file_name}', 'wb') as f:
    f.write(res.content)

# ファイル書き換え。
copy_xlsx_sheet.run(f'./{file_name}')

# ファイル更新。
put_file.run(access_token, file_id, f'./{file_name}')
```

- この↑スクリプトを実行すれば勝手にやってくれますが、そんなの手動で実行していたらプログラム化した意味がありません。
- 自動実行してもらいます。
- GitHub Actions を使います。

![actions](https://user-images.githubusercontent.com/28250432/104534266-4da90c80-5657-11eb-9ee2-d10a8d0a3d1d.png)

- 定期的に……
    - このスクリプトを実行
    - 結果を Slack に通知
    - してもらいます。
- つぎ↓のような yaml(言語、フォーマットの一種)を書きます。
    - 文字が多くて見づらいと思いますが、実際のプログラムを見ることでイメージがわく方も(わたし)いると思うので軽く……

```yaml
name: Python application

on:
  push:
    branches: [ master ]
  schedule:
    # Ref: https://crontab.guru/
    - cron: '0 3 * * 3'

env:
  SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK_URL }}

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v1
      with:
        python-version: 3.8
    - name: Install pipenv and dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pipenv --upgrade-strategy=only-if-needed
        pipenv install --dev
    - name: Run
      run: |
        pipenv run python main.py
      env:
        TENANT_ID: ${{ secrets.TENANT_ID }}
        CLIENT_ID: ${{ secrets.CLIENT_ID }}
        CLIENT_SECRET: ${{ secrets.CLIENT_SECRET }}
        USER_OBJECT_ID: ${{ secrets.USER_OBJECT_ID }}
        TARGET_SITE_ID: ${{ secrets.TARGET_SITE_ID }}
        TARGET_FILE_PATH: ${{ secrets.TARGET_FILE_PATH }}
        SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
        SLACK_MESSAGE_CHANNEL: ${{ secrets.SLACK_MESSAGE_CHANNEL }}
        SLACK_MESSAGE_SUCCESS: ${{ secrets.SLACK_MESSAGE_SUCCESS }}
        SLACK_MESSAGE_FAILURE: ${{ secrets.SLACK_MESSAGE_FAILURE }}

    # 成功時はこちらのステップが実行されます。
    - name: Slack Notification on Success
      if: success()
      uses: rtCamp/action-slack-notify@v2.0.2
      env:
        SLACK_TITLE: SharePointMaid succeeded
        SLACK_COLOR: good

    # 失敗時はこちらのステップが実行されます。
    - name: Slack Notification on Failure
      uses: rtCamp/action-slack-notify@v2.0.2
      if: failure()
      env:
        SLACK_TITLE: SharePointMaid failed
        SLACK_COLOR: danger
```

## 機械学習とか AI とかもステキですけれど……

- 私は趣味レベルなので、日頃の面倒なぱそこん作業を自動化するのが好きです。
- 今回の Python は GitHub にあげてあります。
    - https://github.com/yuu-eguci/SharePointMaid

![sharepointmaid](https://user-images.githubusercontent.com/28250432/104532512-bb533980-5653-11eb-8bcc-e30af3d6c7c4.png)

## 「Django ブログをいつもいつも手動でデプロイするのがめんどうくさい」(お話したいこと 2/3)

自動化なんていう便利なものを見つけたのでブログのデプロイ作業も自動化しました。

- Django アプリケーションをレンタル Linux で動かしています。
- これまでは手動で SSH 接続してデプロイしていました。

![](https://www.mrrhp.com/media/markdownx/01a75302-664f-4f22-8a60-db4d77cb8466.jpg)

- めちゃめちゃ面倒なので push するだけでデプロイされるようにしました。

![](https://www.mrrhp.com/media/markdownx/0948c417-fed6-4e25-ad66-58d35ac154d8.jpg)

- 自動で……
    - レンタル Linux に SSH 接続
    - ソースのダウンロード
    - デプロイコマンドの実行
    - をしてもらいます。

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

    # Test を行う場合はここで set up Python や install dependencies, migration や test を行う。
    # NOTE: mrrhp-apache はユニットテストを行っていないのでスキップ。

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

## ここまできたら Linux だけでなくクラウドサービスへも自動デプロイします(お話したいこと 3/3)

- 今回のクラウドサービスは Azure App Service です。
- まったく同じコトをやりたい方なんていないと思いますので、「こういうこと(Azure への自動デプロイ)は可能でした」というご紹介をしたいです。

![restaurant](https://user-images.githubusercontent.com/28250432/104535298-41be4a00-5659-11eb-8f51-39435cf08dfc.png)

- yaml を紹介します。めちゃ長いですがかいつまむのでご安心を……

```yaml
name: Build and deploy Django app to Azure App Service

on:
  push:
    branches:
      - master

jobs:

  # ジョブひとつめ。
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      # App Service の Python が3.7です。統一します。
      - name: Setup Python version
        uses: actions/setup-python@v2
        with:
          python-version: 3.7

      # 仮想環境を作成、起動します。
      - name: Create and start virtual environment
        run: |
          python3 -m venv venv
          source venv/bin/activate
      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Collect static
        run: python manage.py collectstatic --noinput

      - name: Run tests
        run: python manage.py test

      # 次のジョブのためにファイルをアップロードします。
      # NOTE: 仮想環境はランタイム OS と互換性がないのでアップロードされません。
      # NOTE: ジョブの最後にファイルをアップロードすると、
      #       デプロイに失敗した場合には、[アクション] タブからファイルをダウンロードしてデバッグやコンテンツの確認できます。
      - name: Upload artifact for deployment jobs
        uses: actions/upload-artifact@v2
        with:
          name: python-app
          path: |
            .
            !venv/
      # 成功時はこちらのステップが実行されます。
      - name: Slack Notification on Success
        if: success()
        uses: rtCamp/action-slack-notify@v2.0.2
        env:
          SLACK_CHANNEL: restaurant
          SLACK_COLOR: good
          SLACK_MESSAGE: 'build-and-test job SUCCEEDED'
          SLACK_TITLE: build-and-test job succeeded
          SLACK_USERNAME: RESTaurant
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK_URL }}

      # 失敗時はこちらのステップが実行されます。
      - name: Slack Notification on Failure
        uses: rtCamp/action-slack-notify@v2.0.2
        if: failure()
        env:
          SLACK_CHANNEL: restaurant
          SLACK_COLOR: danger
          SLACK_MESSAGE: 'build-and-test job FAILED'
          SLACK_TITLE: build-and-test job failed
          SLACK_USERNAME: RESTaurant
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK_URL }}

  # ジョブふたつめ。
  deploy-to-webapp:
    needs: build-and-test
    runs-on: ubuntu-latest

    steps:

      # 前のジョブでアップロードしたファイルをダウンロードします。
      - uses: actions/download-artifact@v2
        with:
          name: python-app
          path: .

      # Azure CLI にログインします。
      # NOTE: CREDENTIALS は Deploy to Azure 拡張機能で自動生成してもらったものです。
      - name: Log in to Azure CLI
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS_252770C7 }}

      # DISABLE_COLLECTSTATIC: 前のジョブで行ったので不要です。
      # POST_BUILD_COMMAND: ランタイムビルドに続いてコマンドを実行できるフックです。
      # SCM_DO_BUILD_DURING_DEPLOYMENT: oryx ビルドパイプラインを有効にするものらしいがよくわからないです。
      # DJANGO_ENV: Django を production にします。
      # NOTE: settings.py だけしか設定ファイルがないとき有効なのかは知りません。
      #       -> 設定ファイルは manage.py や wsgi.py で分岐させています。 DJANGO_ENV は関係ありません。
      - name: Disable static collection and set migration command on App Service
        uses: Azure/appservice-settings@v1
        with:
          app-name: RESTaurant-app-service
          app-settings-json: '[
            { "name": "DISABLE_COLLECTSTATIC", "value": "true" },
            { "name": "POST_BUILD_COMMAND",  "value": "python manage.py makemigrations && python manage.py migrate" },
            { "name": "SCM_DO_BUILD_DURING_DEPLOYMENT", "value": "true" },
            { "name": "DJANGO_ENV", "value": "production"}
          ]'
          # NOTE: これら↑は App Service の環境変数に書かれる。
          # NOTE: であれば DB 用の環境変数もここ(というより GitHub secrets)に記載するべきか?
          #       いやでも secrets はあとから見返せないから……。検討。
          # NOTE: WEBSITE_HOSTNAME はおそらく App Service の予約名? だから設定不可。

      # デプロイします。
      - name: Deploy to App Service
        uses: azure/webapps-deploy@v2
        with:
          # NOTE: おそらく? azure/login@v1 を使わない場合は publish-profile が必要なのだと思う。
          app-name: RESTaurant-app-service

      # Azure logout
      - name: logout
        run: |
          az logout
      # 成功時はこちらのステップが実行されます。
      - name: Slack Notification on Success
        if: success()
        uses: rtCamp/action-slack-notify@v2.0.2
        env:
          SLACK_CHANNEL: restaurant
          SLACK_COLOR: good
          SLACK_MESSAGE: 'deploy-to-webapp job SUCCEEDED'
          SLACK_TITLE: deploy-to-webapp job succeeded
          SLACK_USERNAME: RESTaurant
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK_URL }}

      # 失敗時はこちらのステップが実行されます。
      - name: Slack Notification on Failure
        uses: rtCamp/action-slack-notify@v2.0.2
        if: failure()
        env:
          SLACK_CHANNEL: restaurant
          SLACK_COLOR: danger
          SLACK_MESSAGE: 'deploy-to-webapp job FAILED'
          SLACK_TITLE: deploy-to-webapp job failed
          SLACK_USERNAME: RESTaurant
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK_URL }}
```

- 割愛していましたが、こんな↓ふうに通知されます。

![succeeded](https://user-images.githubusercontent.com/28250432/104535981-826a9300-565a-11eb-88d6-4d01527ee271.png)

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## お時間いただきありがとうございました

- 今回は自動デプロイだけに焦点を絞りましたが、ほかには自動テストをよく行っています。
    - 自動テストを通過しないと main branch へマージできない、というような仕組み。
    - これによって友達とアプリを作っているとき、発生するバグをだいぶ抑えられています。
- もっとスマートな自動デプロイが知りたいです。
    - 「自分はこんなふうにやってる」
    - 「ここ無駄じゃない?」

ぜんぶ GitHub にアップしてあります。

- https://github.com/yuu-eguci/SharePointMaid
- https://github.com/yuu-eguci/mrrhp-apache
- https://github.com/yuu-eguci/RESTaurant

![github](https://user-images.githubusercontent.com/28250432/104541201-6bc93980-5664-11eb-92d3-1f6559282deb.png)

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## Powered by Sublime Text OmniMarkupPreviewer
