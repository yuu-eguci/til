GitHub Actions and Heroku Note
===

ぼくが大好きなプログラム形式

- GitHub に push して
- Actions で Heroku にデプロイして
- Heroku で定期実行する
- あるいは単純実行する

のやりかたをまとめる。

## Python script

Heroku のスケジューラは crontab を書けねえ。だから一分ごと、一時間ごとに実行して、 Python 側でちゃんと任意のタイミングで実行するようにする。たとえばこんな感じの関数を用意しとく。

```python
import datetime
import pytz


def market_is_open() -> bool:
    """9〜15時であれば True を返します。

    Returns:
        bool: 9〜15時であれば True。
    """

    # 現在時刻。
    current_jst = datetime.datetime.now(tz=pytz.timezone('Asia/Tokyo'))
    # 現在の「時」。
    current_hour = current_jst.hour
    return 9 <= current_hour <= 15
```

## Actions yaml

このまま使え。 action のバージョンは、都度アップグレードしようね。

```yaml
name: Deploy to Heroku

on:
  push:
    branches:
      - master
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: akhileshns/heroku-deploy@v3.12.12 # This is the action
        with:
          heroku_api_key: ${{secrets.HEROKU_API_KEY}}  # required
          heroku_app_name: ${{secrets.HEROKU_NAME}}  # required
          heroku_email: ${{secrets.HEROKU_EMAIL}}  # required
```

## Heroku 上で実行する

```bash
brew tap heroku/brew && brew install heroku

heroku run python main.py shell --app APP_NAME
```

## Heroku で定期実行

- add-on の Heroku Scheduler を入れる。
- てきとうに設定する。(画面みりゃわかる)
- これで定期実行される。

## 定期実行のログを閲覧

```bash
# これで最新 --num 件を表示。(最大 1500)
heroku logs --num 100 --app APP_NAME

# プロセス番号指定で見る。
heroku logs --ps scheduler.XXXX --app APP_NAME
```
