# ====================================
# @property ノート
# ====================================
"""
Python では……

- 属性(attribute)
    - インスタンス変数、インスタンスメソッドのこと。

- プロパティ
    - クラス変数のこと。

- マジックメソッド = dunder
    - double underscore で囲まれていることからそう呼ぶ。
"""


class Test:

    def __init__(self):
        self._foo = 0

    # @property をつけると getter になり、 foo をインスタンス変数みたいに呼び出せるようになる。
    @property
    def foo(self):
        # 取得するときに何か起こせることを確認するため、ムダに+1して返すようにします。
        return self._foo + 1

    # .setter をつけると setter になり、 foo へ値代入するとき起こることを定義できます。
    @foo.setter
    def foo(self, new_value):
        # 0～100のみ認めるようにします。
        if not (0 <= new_value <= 100):
            raise ValueError('0～100にしてくれ')
        self._foo = new_value


test = Test()
# print(test.foo)  # 初期値の0に+1されて1
test.foo = 100   # OK
# test.foo = 101   # NG


# ↑まったく同じ特徴をもつ bar, baz を追加すると
# メソッド量がヤベーことになる。再利用がまったくできてなくてゴミ。↓

class Test:

    def __init__(self):
        self._foo = 0
        self._bar = 0
        self._baz = 0

    @property
    def foo(self):
        return self._foo + 1

    @foo.setter
    def foo(self, new_value):
        if not (0 <= new_value <= 100):
            raise ValueError('0～100にしてくれ')
        self._foo = new_value

    @property
    def bar(self):
        return self._bar + 1

    @bar.setter
    def bar(self, new_value):
        if not (0 <= new_value <= 100):
            raise ValueError('0～100にしてくれ')
        self._bar = new_value

    @property
    def baz(self):
        return self._baz + 1

    @baz.setter
    def baz(self, new_value):
        if not (0 <= new_value <= 100):
            raise ValueError('0～100にしてくれ')
        self._baz = new_value


# ↓のように書けば OK

import weakref


class Descriptor:

    def __init__(self):
        # {インスタンス化された Descriptor: 値} という辞書を作ります。
        # NOTE:
        #   メモリリークを防ぐため、普通の辞書ではなく WeakKeyDictionary を使います。
        #   なぜ普通の辞書だとメモリリークになるのかはよくわかってない。
        #   まあ辞書と使用感は同じだから、「こっちのほうがいい」というならこっちを使えばいいだろう。
        self._values = weakref.WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        # instance: このプロパティ(この Descriptor はクラス変数となる)を持ってるインスタンス……か?
        # instance_type: このプロパティを持ってるインスタンスの型(クラス)。

        # NOTE: instance is None になる状況がわからないけどオライリーに書いてあったので置いてあります……。
        if instance is None:
            return self

        # 値を取得するのと同時に初期値を定義しています。
        # 上と同じく、取得するときに何か起こせることを確認するため、ムダに+1して返すようにしています。
        return self._values.get(instance, 0) + 1

    def __set__(self, instance, new_value):
        if not (0 <= new_value <= 100):
            raise ValueError('0～100にしてくれ')
        self._values[instance] = new_value


class Test:

    # ここで、「インスタンス変数からクラス変数になっとるやんけ」と思うんだけど、
    # 実はそもそも上のやつもインスタンス変数ではなかったのだ。
    # 「プロパティ」がそもそもクラス変数のこと。
    # 「アトリビュート」がインスタンス変数とインスタンスメソッドのこと。
    foo = Descriptor()
    bar = Descriptor()
    baz = Descriptor()


test1 = Test()
test2 = Test()

test1.foo = 50
test2.foo = 100

print(test1.foo)  # +1されて51
print(test2.foo)  # +1されて101

test2.foo = 101   # ValueError: 0～100にしてくれ って出る。
