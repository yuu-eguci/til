"""NBSP Note

Markdown で "- " が機能しなくて、なんでだろ?
-> ハイフンのあとにあるのが、半角スペースじゃなくて NBSP だった!
という経緯で出会った NBSP
「正体不明のスペース」って呼んでたけどわかってよかった。 &nbsp; は半角スペースではない!
"""

space = ' '
space2 = ' '

print(ord(space))  # 32
print(ord(space2))  # 160

print(hex(ord(space)))  # 32 -> 0x20
print(hex(ord(space2)))  # 160 -> 0xa0

# https://ja.wikipedia.org/wiki/Unicode%E4%B8%80%E8%A6%A7_0000-0FFF
# Unicode 一覧で確認すると……
# 0x20 -> ふつーの半角スペース
# 0xa0 -> NBSP

# この NBSP というのが今回の「正体不明スペース」。 no-break space, non-breaking space
# - &nbsp; の html 上での姿
# - 自動折返しが行われないスペース
