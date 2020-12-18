SlackNote
===

## Setup

- https://api.slack.com/apps から App を追加
- Building Apps for Slack からどれか選ぶ(複数可)
    - Incoming Webhooks: 外部のアプリケーションからSlackへメッセージを送る
    - Slash commands: /でユーザがアプリを起動できるようにする
    - Bots: Appとのインタラクティブなやりとりを可能にするボットを追加する
    - Interactive Components: Appにボタンを追加してインタラクティブな操作を可能にする
    - Event Subscriptions: ユーザからの入力などに対して反応するようにする
    - Permissions: AppがAPIを使用するための権限設定

## Sample

```python
# FIXME: なぜか普通に実行すると OK で
# nosetests を実行すると ModuleNotFoundError: No module named 'slack' が出る。
import slack

# Send the information to Slack.
# This repository is set private because real token is written here.
# As this code is for members to practice coding, not should be complicated.
# Token should be stored as environment variable.
client = slack.WebClient(token='xoxb-000000000000-1111111111111-GGGGGGGGGGGGGGGGGGGGGGGG')  # noqa: E501

# Post message.
# This library doesn't support sender_emoji neither sender name.
response = client.chat_postMessage(
    channel='CCCCCCCCC',
    text=text_to_send
)
assert response['ok']
assert response['message']['text'] == text_to_send
```

## GitHub Actions 使う場合は yml に書くことを考えてね

- https://github.com/rtCamp/action-slack-notify
- ↑ここにもあるけど、まず https://slack.com/apps/A0F7XDUAZ-incoming-webhooks から webhook url を取得。
- 以下、 yml

```yml
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

    # 成功時はこちらのステップが実行されます。
    - name: Slack Notification on Success
      if: success()
      uses: rtCamp/action-slack-notify@v2.0.2
      env:
        SLACK_CHANNEL: post_yuu-eguci
        SLACK_TITLE: SharePointMaid succeeded
        SLACK_COLOR: good

    # 失敗時はこちらのステップが実行されます。
    - name: Slack Notification on Failure
      uses: rtCamp/action-slack-notify@v2.0.2
      if: failure()
      env:
        SLACK_CHANNEL: post_yuu-eguci
        SLACK_TITLE: SharePointMaid failed
        SLACK_COLOR: danger
```
