yuu-eguci です
===

## おまえだれよ(Python 流の自己紹介らしい)

趣味 Pythonista です。ジョギングとテレビゲームが好きです。

今回は、「プログラミング問題へのいざない」というテーマで短く LT をさせてもらおうと思います。

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## プログラミング問題へのいざない

会でたまに「ヒマな人いたらプログラミング問題やりません?」とご提案しておりますが、いつも「それ何どうやるの?」にうまくご回答できていません。ご回答します。

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## たとえばこうきかれます

- for ループを使用して、リスト内の整数の合計を計算せよ。

![1](https://user-images.githubusercontent.com/28250432/121463969-f896da00-c9ed-11eb-8a49-78ba0526580f.png)

- こうかな〜……
- でもどう答えればいい? 計算せよって言われてもなあ……

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## こうこたえます

こんなふうに、「回答をかく関数」と、自分のプログラムが「あっているか確かめる `print`」を用意します。

![2](https://user-images.githubusercontent.com/28250432/121463974-f9c80700-c9ed-11eb-9557-0648eafc6708.png)

&nbsp;

![3](https://user-images.githubusercontent.com/28250432/121463975-fa609d80-c9ed-11eb-9037-55dfcb4af688.png)

&nbsp;

![4](https://user-images.githubusercontent.com/28250432/121463976-faf93400-c9ed-11eb-9cb5-73a3e19ffb7c.png)

&nbsp;

![5](https://user-images.githubusercontent.com/28250432/121463977-fb91ca80-c9ed-11eb-8474-355f10d269bb.png)

&nbsp;

そんなわけで、こういう `print` をいくつか用意しておいて……

![6](https://user-images.githubusercontent.com/28250432/121463979-fb91ca80-c9ed-11eb-8bde-3eb10d9c0b96.png)

&nbsp;

すべてで `True` を出せればプログラムは正解になります。 Yey!

![7](https://user-images.githubusercontent.com/28250432/121463982-fc2a6100-c9ed-11eb-8054-718bc289dbdd.png)

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## できたら見せ合います

![8](https://user-images.githubusercontent.com/28250432/121463983-fc2a6100-c9ed-11eb-97cf-c458b2f35462.png)

- 私がこの遊びが面白いと思うのは、単純な問題でも、意外とみんなで書き方がちがうところです。
- 変数の名付け方、使う標準関数、ロジックの組み方が違います。
- プログラムの速さにこだわる人や、読みやすさにこだわる人、多少ムダでも最近知った Python の構文を使ってみたい人がいます。
- あなたはどんなタイプでしょうか? そして他のみんなはどんなタイプでしょうか?
- 同じ問題を解くから、比べやすく、意見が言いやすく、良いなと思うことを取り入れやすいです。
- 私が知っている Python の書き方のほとんどは、 GitHub でコードを読む、とかではなく、友達と遊んだプログラミング問題です。とくに数学が好きな友達は、変数の名付け方が目新しいものばかりで面白かったりしました。
- やりたくなってきましたね?

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## やりたくなってきたでしょうからやりましょう

ご用意しました。

```python
"""
交互に要素を取ることで、2つのリストを結合する関数を記述せよ。
例えば [a, b, c]と[1, 2, 3]という2つのリストを与えると、関数は [a, 1, b, 2, c, 3]を返す。

https://softantenna.com/wp/software/5-programming-problems/ より
"""


def solve(elements1: list, elements2: list) -> list:

    answer_list = []
    # ここに Python を書く。

    return answer_list


# 今回はシンプルにするため、ふたつのリストは同じ数の要素を含むという決まりにしてみます。
print(solve(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3])
print(solve([], []) == [])
print(solve(['あいう', 'かき', 'さしすせ'], ['えお', 'くけこ', 'そ'])
      == ['あいう', 'えお', 'かき', 'くけこ', 'さしすせ', 'そ'])

```

(もしご興味わいたら遊びましょう。)

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## 補足です。以上の「答え方」は一般的でもなんでもないと思います

実際はこんなふう↓に `input` で出題を受け取って、 `print` で答えを出します。

```python
n = input()

# ここで問題をとく。

print('???')

```

ただ私が友達と遊ぶときは、実行とかしやすいように + 答えがあってるかを `True` or `False` で判別しやすいように、こんな形式でやっています。

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## お時間いただきありがとうございました

気になるコト、興味のあるコトはございましたか? 自分のオモチャを広げてみて、興味のある方がおれば喋ったりしたいと思って LT しています。ぜひ声かけてください。

![github](https://user-images.githubusercontent.com/28250432/104541201-6bc93980-5664-11eb-92d3-1f6559282deb.png)

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## Powered by Sublime Text OmniMarkupPreviewer

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;
