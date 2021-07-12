"""標準化をやってみようノート

- 標準化は、たくさんの数字の中のひとつの数字を、全体の平均からどれだけ離れているか明示する行為。
- 具体的には、「1. 数値から平均を引く」「2. 標準偏差で割る」というステップを踏む。
    - (言葉の解説↓)
    - 「標準偏差」は「分散」のルート値。
    - 「分散」は各数値の平均からの距離の二乗の平均。
- 1 はわかるにしても、標準偏差という謎数値は意味不明。ここの理解は諦める。
    - 数学の公式的に、「こうするといい感じに出るものボックス」に放り込んでおく。
"""

import math


# n 人の小学生のテストの点数を定義します。
# NOTE: 動的に計算しているので、ここの dic に人を足せば結果を変えられます。
dic = {
    'a': 90,
    'b': 92,
    'c': 97,
}
# 点数の平均を出しておきます。
average = sum(dic.values()) / len(dic.values())
# 点数の分散を出しておきます。(各数値の平均からの距離の二乗の平均)
# NOTE: variance っていうらしいです。
variance = sum(map(lambda v: (average - v) ** 2, dic.values())) / len(dic.values())
# 標準偏差を出しておきます。(「分散」のルート値。)
# NOTE: standard_deviation っていうらしいです。
standard_deviation = math.sqrt(variance)
# 出しておいた連中を観てみます。
print(dict(
    average=average,
    variance=variance,
    standard_deviation=standard_deviation,
))

# 標準化します。(「1. 数値から平均を引く」「2. 標準偏差で割る」)
standardized = {}
for k, v in dic.items():
    standardized[k] = (v - average) / standard_deviation
# 結果を出力します。
print(standardized)
