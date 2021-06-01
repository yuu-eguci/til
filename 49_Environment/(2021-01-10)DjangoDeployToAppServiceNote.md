Django Deploy To AppSerivce Note
===

- ググると色んなパターンが出てくる…… vscode からクリックでデプロイだったり、そもそも Django じゃなかったり、 DevOps だったり……だけど GitHub Actions を使いたいに決まっているだろ!

## GitHub Actions を使ったデプロイ

### ざっくりした手順

- App Service 用意。
- DB 用意。
- schema も準備しておく。
- requirements.txt 用意。
    - `pipenv lock -r > requirements.txt`
- CREDENTIALS を作成。(GitHub Actions から Azure CLI へログインするときに必要)
    - ちと邪道だけど VSCode の拡張機能 **Deploy to Azure** を使って発行すると、一気に secrets 登録までしてくれてラク。
    - GitHub > settings > Developer > Personal access tokens 発行
        - 追加する権限は「repo すべて」「workflow」
    - コマンドパレット > Deploy to Azure:Configure CI/CD Pipeline
    - 多分? Python to Linux Web App on Azure を選択 > サブスクリプションを選択
    - その次に何か input しろって言われる。これが何かは初見ではわからないのだが、これは `AZURE_CREDENTIALS_xxxx` の `AZURE_CREDENTIALS` 部分だと思われる。 AZURE_CREDENTIALS にしとけ。
- 下に用意した yaml を .github/workflows/workflow.yml みたいに用意。
- これだけでデプロイ自体はできるはず。だけど Django 側の settings が AppService 環境用になってないので設定する。(下に書く)
- createsuperuser は……
  - AppService ページ > SSH > go >
  - `python manage.py createsuperuser --email *** --username ***`

### AppService 環境用の設定

(2021-04-03)もともと下の方にある「使う yaml」がこのセクションにあったけど、こっちの「AppService 環境用の設定」をしないまま yaml だけ push して Actions コケたので順番を変えた。せっかちすぎるんだよな。まさに「この設定は、 AppService というよりその前の collectstatic で必要」のとこでコケた。

- settings.py
- production.py
- AppService 環境では production.py を使うよう設定
- production.py に書いた環境変数を定義
    - `DJANGO_DATABASE_NAME`
    - `DJANGO_DATABASE_PASSWORD`
    - `DJANGO_DATABASE_SERVER`
    - `DJANGO_DATABASE_USER`
- urls.py and views.py で ServerError500 対応
- もちろん最初は view が無いので、アクセスしても 404 になる。

コードは↓にあるよ。

### AppService tips

- Deployment Center にデプロイの履歴がざっくりと残るよ
- ログは Log Stream にちゃんと出るよ

### 「AppService 環境用の設定」のコード郡

```python
# settings.py
# この設定は、 AppService というよりその前の collectstatic で必要。
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

```python
# production.py
# AppService 環境用の設定。
from .settings import *
import os

# NOTE: 無いと Did you install mysqlclient? と煽られます。
import pymysql
pymysql.install_as_MySQLdb()

DEBUG = False

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']
                 ] if 'WEBSITE_HOSTNAME' in os.environ else []

# WhiteNoise configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Add whitenoise middleware after the security middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# NOTE: この設定はいろんなサイトに記載されているが、 Missing staticfiles manifest entry エラーを引き起こすので排除。
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATIC_ROOT は settings.py に定義済み。

# Configure Postgres database; the full username is username@servername,
# which we construct using the DBHOST value.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DJANGO_DATABASE_NAME'],
        'USER': os.environ['DJANGO_DATABASE_USER'],
        'PASSWORD': os.environ['DJANGO_DATABASE_PASSWORD'],
        'HOST': os.environ['DJANGO_DATABASE_SERVER'],
        'PORT': '3306',
        'OPTIONS': {
            'ssl': {'ssl-ca': '/var/www/html/BaltimoreCyberTrustRoot.crt.pem'}
        }
    }
}
```

```python
# manage.py と wsgi.py
# AppService 環境では production.py を使う設定をする。

# App Service 環境では config.production を使います。
# NOTE: WEBSITE_HOSTNAME は App Service 環境のデフォルト環境変数です。
# NOTE: manage.py にも同様の設定があります。
settings_module = 'config.production' if 'WEBSITE_HOSTNAME' in os.environ else 'config.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
```

### どうせ ServerError500 が出て困るハズだから 500 のユーザー定義もしよう

- [Django Server Error (500)攻略法【2019 アドカレ】](https://qiita.com/yuu-eguci/items/a1e4b0a2f238d5ccc985)

```python
# urls.py
from app import views

handler500 = views.my_customized_server_error
```

```python
# views.py
from django.views.decorators.csrf import requires_csrf_token
from django.http import (
    HttpResponseServerError,
)

@requires_csrf_token
def my_customized_server_error(request, template_name='500.html'):

    # NOTE: print が App Service で機能するかどうか確かめるために print しています。
    import traceback
    print(traceback.format_exc())
    # return HttpResponseServerError('<h1>Server Error (500)</h1>')

    # DEBUG = True と同様の画面を出します。
    import sys
    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)
```

### 使う yaml

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
          creds: ${{ secrets.AZURE_CREDENTIALS_xxxx }}

      # DISABLE_COLLECTSTATIC: 前のジョブで行ったので不要です。
      # POST_BUILD_COMMAND: ランタイムビルドに続いてコマンドを実行できるフックです。
      # SCM_DO_BUILD_DURING_DEPLOYMENT: oryx ビルドパイプラインを有効にするものらしいがよくわからないです。
      # DJANGO_ENV: Django を production にします。
      # NOTE: settings.py だけしか設定ファイルがないとき有効なのかは知りません。
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

      # デプロイします。
      - name: Deploy to App Service
        uses: azure/webapps-deploy@v2
        with:
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

### このデプロイで発生するエラー

```
An unknown error has occurred. Check the diagnostic log for details.
Error: Failed to deploy web package to App Service.
Error: Deployment Failed with Error: Package deployment using ZIP Deploy failed. Refer logs for more details.
```

今のところ原因はわからないが、コードが原因じゃないっぽい。 Re-run で解決した。
