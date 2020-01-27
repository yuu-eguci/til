
"""TimezoneNote
"""


import datetime
import pytz


"""まとめ

・ tz付datetimeつくりたい -> PYTZを引数に
・ 文字列変換             -> %z が該当
・ タイムゾーン確認       -> DATETIME.tzinfo
・ あとからtzを付与       -> PYTZ.localize()
・ あとからtzを変更       -> DATETIME.astimezone(PYTZ)

"""

TZ_JAPAN = pytz.timezone('Asia/Tokyo')
TZ_NEPAL = pytz.timezone('Asia/Katmandu')
# TZ_UTC は pytz.utc で OK。

# いまの UTC 時間。
current_utc = datetime.datetime.now(tz=pytz.utc)

# 特定の時間 8個目にtz指定しよう!
print( datetime.datetime(2019, 1, 31, 1, 2, 3, 4, pytz.utc) )

# いまの日本時間。
current_japan = datetime.datetime.now(tz=TZ_JAPAN)

# naive datetime(タイムゾーンを持たないもののこと)
naive = datetime.datetime.now()
# を、日本時間にする。(localize:タイムゾーン付与)
current_japan = TZ_JAPAN.localize(naive)

# 日本時間を UTC にする。(normalize:タイムゾーン変換)
# pytz.utc がふたつもあって冗長に見えるけどこれはしかたないそうだ。
current_utc = pytz.utc.normalize(current_japan.astimezone(pytz.utc))

# UTC をネパール時間にする。ここで今の日本時間がネパール時間で何時なのかわかるね!
current_nepal = TZ_NEPAL.normalize(current_utc.astimezone(TZ_NEPAL))

# ↑のように一度 UTC にするのもいいけど、日本->ネパールに一発で変換するには?
current_nepal = TZ_NEPAL.normalize(current_japan.astimezone(TZ_NEPAL))

# ---------------------------------------------

# strptime
print( datetime.datetime.strptime('2018-02-14' + '+0000', '%Y-%m-%d%z') )

# strftime
_ = datetime.datetime.now(tz=pytz.utc)
print( datetime.datetime.strftime(_, '%Y-%m-%d %z') )

# タイムゾーン情報を持っていることの確認。
#     もっているもの: aware と呼ぶ
#     もってないもの: naive と呼ぶ
aware  = datetime.datetime.now(tz=pytz.utc)
naive = datetime.datetime.now()
print(aware , '----', type(aware.tzinfo) , aware.tzinfo )
print(naive, '----', type(naive.tzinfo), naive.tzinfo)

"""Django では下記メソッドでタイムゾーンつき現在時刻を取得できる
"""
# from django.utils import timezone
# timezone.now()        UTC
# timezone.localtime()  設定したタイムゾーン
