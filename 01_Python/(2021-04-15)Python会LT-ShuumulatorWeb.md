yuu-eguci です
===

## おまえだれよ(Python 流の自己紹介らしい)

趣味 Pythonista です。ジョギングとテレビゲームが好きです。

Favorite libs: dotenv

トピックを1本用意しました。

- 先日に発表させてもらった株自動売買シミュレータ。あれの結果をみなさんが見れるようにしました。

詳細には興味ない方が多いと思います。今回の LT は「Python でこんなことが出来ました! もし興味のあるモノがあればのちほど個別で詳しく!」というスタンスで詳細は飛ばして発表いたします。

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## その前に……先日の発表の訂正させてください

先週の発表で、こんなことを申し上げました。

> 作ったプログラムを、「GitHub Actions」というサービスで、  
> 永遠に無料で定期実行できます!

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

![1](https://user-images.githubusercontent.com/28250432/114846660-dcc0ee80-9e17-11eb-95b8-e298d1e23ceb.png)


あれはウソです。じゃなくて間違いでした。訂正します。

- これまでやっていたこと: Python を GitHub にアップロードして、そこで実行
- これからやること: Python を GitHub にアップロードして、自動で Heroku へアップロードしてもらって、そこで実行

![actions-heroku](https://user-images.githubusercontent.com/28250432/114848573-cae04b00-9e19-11eb-8ad2-a7e487032492.png)

いや、何が何だか。 GitHub Actions って何。っていう方がほとんどだと思いますので、サッと訂正するにとどめますが、とりあえず「Actions」を使うことになったら(なんか気をつけることがあるって聞いたな……)程度の参考になれば、さいわいです。

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## 「あれ」の結果をウェブサイトで見れるようにしました

「あれ」は友達のアイデアで作ったものでしたが……

- 友達「あれええけど、結果おれ見れないやん?」

### 🤔

言えてる……どうする? あのサーバのパスワードをあげる?

### 🤭💡

ウェブサイト作ろう。

つくりました。

&nbsp;

&nbsp;

&nbsp;

<iframe width="800" height="515" src="https://www.youtube.com/embed/LJVL15vgi0o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

&nbsp;

みんな見れます。

[https://yuu-eguci.github.io/ShuumulatorWeb/](https://yuu-eguci.github.io/ShuumulatorWeb/)

今回の全体図はこんな感じになってます。

![test](https://user-images.githubusercontent.com/28250432/114857455-3bd83080-9e23-11eb-939a-1f1ccd641491.png)

### 作り手しか興味ないこだわりポイント

- 輝く Python アイコン
- ログインに「セッション」じゃなくて「json web token」を使用
- Python も html も CI/CD 対応

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
