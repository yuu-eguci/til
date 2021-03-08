yuu-eguci です
===

## おまえだれよ

趣味 Pythonista です。

Favorite libs: django, requests, decimal?

トピックを1本用意しました。

- 株の自動売り買いのシミュレータを作ってみました

詳細には興味ない方が多いと思います。今回の LT は「Python でこんなことが出来ました! もし興味のあるモノがあればのちほど個別で詳しく!」というスタンスで詳細は飛ばして発表いたします。

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## 株、やってますか?

まずことの経緯を。株なんて興味なくて Python の話だけききたい方、すいません……。

- 友達「株なんておめー、上がるか下がるかの二択なんだから勝率は50%になるんだよ!」

天才かな?

- 友達「ただ収支がプラマイゼロになるわけじゃない。株価が10%上がったときの利益と10%下がったときの損失はイコールじゃないから。」

どゆこと?

- 友達「100円だった株価が10%上がったときは10円儲かるけど、そのあと10%下がったら11円の損失になって結果1円損してるってこと。」

じゃあ下がってるときは早めに売らないといけないんだ。

- 友達「そうやね。」

めんど!

- 友達「そこで計算式を用意したで。」

![1](https://user-images.githubusercontent.com/28250432/110226195-78fdf880-7f30-11eb-9ae2-636ce1171fcb.png)

↓

![2](https://user-images.githubusercontent.com/28250432/110226196-7a2f2580-7f30-11eb-9900-8b65cee904c5.png)

全然わからん。

- 友達「これで収支がきちんとプラマイゼロになるパーセンテージがわかるで。」

整理させてほしいんだけど、「株をランダムに買って」「その計算式でプラマイゼロの売りタイミングで売れば」「収支がゼロになる」ってこと?

- 友達「そのはず。」

何それすごい。シミュレータとか作ってホントにそうなるのか試してみたくない?

- 友達「試してみたいけどめんどい。」

作ってくるわ!

↓

作りました。

![](https://user-images.githubusercontent.com/28250432/109735015-518fee80-7c05-11eb-89a0-1c275fe81594.png)

[https://github.com/yuu-eguci/Shuumulator#description](https://github.com/yuu-eguci/Shuumulator#description)

- requests モジュールで株価を掲載しているウェブサイトにアクセス
- BeautifulSoup モジュールで html を解析して、株価を抽出
- mysql.connector モジュールで、その株価をデータベースに書き込み
- GitHub Actions サービスでこのプログラムを定期実行
- 同じく GitHub Actions で結果(現在の勝率とか、実現損益)を閲覧

以下が、動作している様子です。

![shuumulator-screen-shot1](https://user-images.githubusercontent.com/28250432/109889788-5f0eac80-7cc9-11eb-9c54-cb2c6ab54070.png)

![shuumulator-screen-shot2](https://user-images.githubusercontent.com/28250432/109889791-5fa74300-7cc9-11eb-815e-f5855ad1dfbe.png)

何がおもしろいって、実際にお金を使っていないと、どれだけ損が出ていても「わーめっちゃ損してるーーー」と笑えるところですね。実際のトレードも、それくらい気楽にやりたいものです。

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

## 定期的に Pull Request を投稿する

GitHub をやってない方にはホントに関係ないトピックですみません……開き直って GitHub の用語をたくさん使います……。手早くご紹介。

- 友達と一緒にアプリケーションを作っていて、月イチで更新をリリースしています。
- リリースには GitFlow 開発サイクルを使っていまして、月イチで develop branch -> master branch Pull Request をすることになります。
- メンドくさいので自動化しました。

実際にやっていることは次の通りです。

- 月イチで実行。またまた GitHub Actions を利用
- GitHub で PR を投稿
- PR に含まれるコミットをリストアップ
- それを「リリースノート」として Slack へ投稿

![](https://user-images.githubusercontent.com/28250432/106868735-7e3e0c80-6712-11eb-89d6-f7d492a3978e.png)

![pr](https://user-images.githubusercontent.com/28250432/107607880-cc589000-6c7d-11eb-88ba-1f6dcee818b2.png)

今回使っているワザはこれ。

- GitHub Actions 定期実行
- 特定のラベルを貼り付けた PR のみ Slack に通知
- api.github.com を利用。
    - 似たような、 GitHub を操作する API には「hub コマンド」や「gh コマンド」がありますが一番汎用性のあるものを利用。 
