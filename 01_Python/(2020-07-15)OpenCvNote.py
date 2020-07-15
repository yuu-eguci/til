"""
OpenCV Note

pipenv install opencv-python

このノートは ↑ install すれば実行できる。
"""


import cv2
import numpy


# ローカルファイルから mat ファイルを作る。
mat = cv2.imread('./file.png')

# グレースケールで作る。
gray_scale_mat = cv2.imread('./file.png', cv2.IMREAD_GRAYSCALE)


# バイナリから mat ファイルを作る。
def imread_from_bytes(b: bytes) -> numpy.ndarray:
    numpy_array = numpy.frombuffer(b, numpy.uint8)
    numpy_ndarray = cv2.imdecode(numpy_array, cv2.IMREAD_COLOR)
    return numpy_ndarray


# NOTE: mat ってのは numpy の1,2次元配列です。
# NOTE: type(mat) -> <class 'numpy.ndarray'>
# NOTE: 1次元のことを channel といい、2次元のことを dimension といいます。
# print(mat)
# [[[ 37  40  49]
#   [ 34  37  44]
#   [ 47  51  66]
#   ...
#   [ 48  61  74]
#   [ 47  59  74]
#   [ 47  61  73]]
#   ...
#  [[ 80 115 139]
#   [ 88 127 152]
#   [130 166 190]
#   ...
#   [ 97 133 166]
#   [ 73 108 143]
#   [ 64  94 127]]]

# mat を画像で閲覧できます。ニュッと GUI で出てくる。
cv2.imshow('mat', mat)
cv2.waitKey(0)

# mat の情報は普通に numpy.ndarray の持っているメソッドで確認できる。
# channel はカラー画像のとき存在します。
# NOTE: グレースケールと見分けるのに使われるようだ。
width, height, channel = mat.shape
# print(width, height, channel)
# Example:100     100        3


# 画像(mat)同士を連結。 mat 自体を2次元配列にしたものを渡すと、1つの mat になって返ってきます。
def concatenate_tile(mat_list_2d: numpy.ndarray) -> numpy.ndarray:

    # mat_file の1次元配列を受け取り、タイル状に連結します。
    return cv2.vconcat([cv2.hconcat(list_1d) for list_1d in mat_list_2d])


# ブランク画像です。
# NOTE: 黒画像なら numpy.zeros((100, 100, 3), numpy.uint8)
blank_mat = numpy.ones((100, 100, 3), numpy.uint8) * 255

# 今回は試しに2x2にしてみる。(file.png 3枚とブランク1枚で。)
mat_list_1d = [mat, mat, mat]
# 数が合わないと(4枚じゃないと)ダメ。
graft_list = [blank_mat] * (4 - len(mat_list_1d))
mat_list_1d.extend(graft_list)
# 4x4にします。 numpy の reshape を使ってもいい気がするが大袈裟かなと。
mat_list_2d = [
    mat_list_1d[0:2],
    mat_list_1d[2:4],
]
# 連結。
concatenated_mat = concatenate_tile(mat_list_2d)

# 確認します。
cv2.imshow('concatenated_mat', concatenated_mat)
cv2.waitKey(0)
