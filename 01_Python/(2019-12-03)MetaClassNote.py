"""MetaClassNote

- サブクラスの検証
"""


# メタクラスは type からの継承で定義される。継承しないと TypeError が出た。
#   TypeError: type.__new__(Meta): Meta is not a subtype of type
class Meta(type):

    # インスタンス化されるときではなく、クラスが定義されるときにすでに実行される。
    def __new__(meta, name, bases, class_dict):
        # meta: self みたいなもん <class '__main__.Meta'>
        # name: これが metaclass として設定されているクラスの名前 MyClass
        # bases: 継承関係にあるクラス type が格納されている ()
        # class_dict: {'__module__': '__main__', '__qualname__': 'MyClass', 'stuff': 123, 'foo': <function MyClass.foo at 0x000001BAA6EA3598>}

        print(meta, name, bases, class_dict)

        # Parent クラスでは妥当性検証しない。
        # そもそも初期値を None にしているので <= で検証したらエラー出る。
        if bases != ():
            if not (0 <= class_dict['stuff'] <= 100):
                raise ValueError('0～100にしてくれ')

        return type.__new__(meta, name, bases, class_dict)


class Parent(metaclass=Meta):
    # Python2 ではこんなふうに定義する。
    # __metaclass__ = Meta

    # サブクラスで規定するつもり。
    stuff = None


class Child(Parent):

    stuff = 101  # ValueError: 0～100にしてくれ って出る
