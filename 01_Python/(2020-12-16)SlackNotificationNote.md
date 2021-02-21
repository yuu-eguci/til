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

## slackapi/python-slack-sdk

```bash
pip install slack_sdk
pipenv install slack_sdk
```

トークンを作って、それを指定して WebClient を作って chat_postMessage する流れ。ドキュメントはここ↓。

- https://github.com/slackapi/python-slack-sdk/blob/main/tutorial/01-creating-the-slack-app.md
- https://api.slack.com/apps?new_granular_bot_app=1 から App 作成
- App 作成
- OAuth & Permissions > Scopes > chat:write 追加
    - postMessage の一部の引数は chat:write.customize を追加しないといけない。
    - ただしこのノートを書いているときはそこまでやっていない。
- 上の方の OAuth Tokens for Your Team に表示されている Token を取得
    - 2種類あって、 OAuth Access Token のほうは「自分からの」メッセージを送信できる
    - Bot User OAuth Access Token のほうはメッセージの name とか emoji を変えられるけれど、 bot を channel へ招待しないといけないみたい。今回はやってない。
- サンプルコードは GitHub 参照
    - https://github.com/slackapi/python-slack-sdk

```python
# サンプル。 SharePoindMaid プロジェクトで使用。
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

try:
    # NOTE: unfurl_links は時折鬱陶しいと思っている「リンクの展開機能」です。不要です。 False.
    response = slack_client.chat_postMessage(
        channel=SLACK_MESSAGE_CHANNEL, text=message, unfurl_links=False)
    # 返却値の確認は行いません。
    # NOTE: Slack api のドキュメントにあるコードなので追加していましたが排除します。
    #       リンクの含まれるメッセージを送信すると、返却値が勝手に変更されるため絶対一致しないからです。
    #       - リンクの前後に <, > がつく
    #       - & -> &amp; エスケープが起こる
    # assert response['message']['text'] == message
except SlackApiError as e:
    assert e.response['ok'] is False
    # str like 'invalid_auth', 'channel_not_found'
    assert e.response['error']
    print(f'Got an error: {e.response["error"]}')
```

- channel_not_found: 一度あったのが、チャンネル名が違うこと

## Sample

(2021-01-13)こちらは昔の。現在では slack_sdk を使うことにした。

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
        SLACK_CHANNEL: restaurant
        SLACK_COLOR: good
        SLACK_MESSAGE: 'job SUCCEEDED'
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
        SLACK_MESSAGE: 'job FAILED'
        SLACK_TITLE: build-and-test job failed
        SLACK_USERNAME: RESTaurant
        SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK_URL }}
```

## メンション

投稿メッセージの中でメンションを使う方法。

- `@yuu-eguci` の代わりに member ID を使う
- Slack アプリのユーザプロフィールから member ID をコピーできる
- あるいは Member 一覧ダウンロード > csv の中に id がある
- `<@UBHUQ6XXX>` こういう形式にするとメンションになる!

ユーザ以外の場合

- `<!here>`
- `<!channel>`
