"""
Numpy Note

pipenv install numpy

このノートは ↑ install すれば実行できる。
"""


import numpy


# [None, None, None, None ...] 作成。
_ = numpy.full(5, None)

# 連結。
_ = numpy.hstack([_, _])

# 縦方向に連結。 [[None, None], [None, None]]
_ = numpy.vstack([_, _])

# 1次元配列 -> 2次元配列。
_ = numpy.array(['foo', 'bar', 'baz', 'qux', 'quux', 'corge'])
_ = _.reshape(3, 2)  # 行:3 列:2
# [['foo' 'bar']
#  ['baz' 'qux']
#  ['quux' 'corge']]

# ndarray から行、列指定で取得。
_ = _[2, 1]  # ↑の例だと corge

print(_)
