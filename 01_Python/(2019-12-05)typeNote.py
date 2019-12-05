"""typeNote

type とは何なのか?

- object の型を返す組み込み関数であり、
- class の型である。
- class の型なので class を作れる。
"""

# type の定義
# type(object)                object の型を返す。(object.__class__ と同じ。)
# type(name, bases, dict)     型オブジェクト(class のこと)を返す。


# 以下ふたつが同じ意味。 class を使わず class を作れる。
class A:
    a = 1
A = type('A', (), dict(a=1))


# メタクラス内で使う type
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print(bases)
        return type.__new__(meta, name, bases, class_dict)
class A(metaclass=Meta):
    pass
class B(object, metaclass=Meta):
    pass
print(A.__bases__)
print(B.__bases__)

## 疑問
#
# 定義時に object をつけていないとき、 metaclass の __new__ の中でも bases に object が無い。
# なのにできあがったクラスの __bases__ には object がある。
# どこで追加されるの?
#
## 一応の理解
#
# わかんないけどたぶん type.__new__ の中で自動で追加されてる。
