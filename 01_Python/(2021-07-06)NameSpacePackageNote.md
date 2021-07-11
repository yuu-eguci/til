Name Space Package Note
===

## Name space package 実験リポジトリ

ここで name space package を自作した。

- [https://github.com/yuu-eguci/name_space_package_lab](https://github.com/yuu-eguci/name_space_package_lab)

## Name space package まわりの挙動

- A: 普通のディレクトリ
- B: 名前空間パッケージ
- C: 普通のパッケージ(`__init__.py` をもつパッケージ)

### パターン1: import A したあと A.B.C.E を参照する。 -> 参照できない。

```python
import A
print(A.B.C.E)  # -> AttributeError: module 'A' has no attribute 'B'
                # B は名前空間パッケージとして作ったので、 AttributeError になります。
```

### パターン2: from A.B.C import D したあと A.B.C.E を参照する。 -> 参照できる。

```python
import A
from A.B.C import D
print(E)  # NameError: name 'E' is not defined
          # わかる。
print(A.B.C.E)  # -> <function E at 0x1048925e0>
                # わからない。
                # from A.B.C の時点で、 import A がパワーアップするってこと???
```

### パターン3: from A.B import C したあと A.B.C.E を参照する。 -> 参照できる。

```python
import A
print(A.B)  # -> AttributeError: module 'A' has no attribute 'B'

from A.B import C
print(A.B)  # -> <module 'A.B' (namespace)>
            # from A.B することで A.B が参照できるようになっている。
            # 「名前空間パッケージ下のパッケージをひとつ import する(from A.B import C)することで名前空間パッケージが
            #   ようやくロードされ、 import A がパワーアップして A.B.C.E が参照できるようになる」
```

### ここまでの所感

- `import A` のあとで `from A.B import ...` することで名前空間パッケージがロードされ(拡張という言い方でもいいか)るという仕様わかりづらっ!

## Name space package 下の関数を呼び出す方法

```python
# これが普通。
from A.B.C import E
print(E)

# だけどぼくは、 A.B.C.E って使いたいのでこうする。
import A.B.C
print(A.B.C.E)
```

## 余談 - 似たような「わかりづらっ」

`import os.path` で `os.path.***` 以外も使えるのわかりづらすぎない?

```python
import os.path

print(os.path.abspath('/'))  # -> /
print(os.getcwd())  # -> /Users/user/Documents/GitHub/lab
                    # これも直感と違うな…… import os.path している場合、
                    # os.path.** しか使えないように見えちゃってた。
```
