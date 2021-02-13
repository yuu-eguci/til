yuu-eguci です
===

## おまえだれよ

趣味 Pythonista です。

Favorite libs: django, requests, decimal?

トピックを2本用意しました。

- 週にどれだけプログラミングしたか、見たくないですか? 見たいですね!
- tkinter よりラク?! 一度だけ傍聴したオンライン Python 会で紹介されていた、 GUI ライブラリ eel 使ってみました!

詳細には興味ない方が多いと思います。今回の LT は「Python でこんなことが出来ました! もし興味のあるモノがあればのちほど個別で詳しく!」というスタンスで詳細は飛ばして発表いたします。

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## みなさんは週にどれだけプログラミングしていますか?

測れるサービスがあります。 WakaTime といいます。無料です。

![wakatime](https://user-images.githubusercontent.com/28250432/107598767-20ee1200-6c62-11eb-87af-55b7f8a8d824.png)

- みなさんのエディタにプラグインをひとつインストール -> 書いた時間とか言語を集計してくれて -> それを可視化。
- そのままだとこの画面で見て「へー」って思うだけなんですが -> Python で継続的にデータ取得して GitHub に載せてみました!

(註)GitHub は作ったプログラムを保存しておいたり、誰でも見れるように公開できるサイトです。「プログラマの SNS」とも呼ばれているみたいです。こないだ三井住友銀行のソースコードがこの GitHub 上で流出して話題になりしたね!

![github](https://user-images.githubusercontent.com/28250432/107599319-75de5800-6c63-11eb-94f5-b308e035a13b.png)

これはほぼリアルタイム更新です。次のような手順でココに載せています。

1. 1時間ごとに WakaTime にアクセスして「データください」と言う(GitHub Actions による定期実行)
1. くれる
1. 「Text 48% Python 25 % ...」みたいなデータをくれるので、それを使ってバーチャートを作る
1. GitHub へアップロード
1. ここ↑に載る

GitHub のプロフィールページを賑やかにしてみたくて作りました!

やりたいと思った方はいませんか?

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## tkinter で苦労している方いるでしょうか? いないでしょうか?

- 註: tkinter は、 Python で GUI ……パソコンの画面に、ウィンドウが出るタイプのアプリケーション……を作るときに使うライブラリです。

こちらは私がいちばん最初につくった Python です。

![eff](https://user-images.githubusercontent.com/28250432/107610242-8226dd00-6c84-11eb-96ba-1aa984da26ad.png)

ポケモンの対戦には欠かせない、「努力値振り」の計算を補助するプログラムです。みなさんもやりましたよね? 

tkinter ライブラリで作ってあります。

いつかのオンライン Python 会で、「GUI を作るとき eel 良いですよ!」というのを聞きました。最近は GUI はあんまり作っていないのですが、 GUI はやっぱり目に見えるので楽しい! のと Python 会でお会いする Python はじめたばっかりの方も GUI を作ってるのをたまに見かけたので……やってみました。

努力値振り計算アプリのリメイクです。

![2](https://user-images.githubusercontent.com/28250432/83946780-df44d600-a84d-11ea-8056-4921fd46d834.png)

![3](https://user-images.githubusercontent.com/28250432/83946781-e10e9980-a84d-11ea-81f7-8f24cfb0c954.png)

正直、 tkinter で GUI をがんばって作るとき、ウィジェットの画面配置がうまくいかなくて苦労しませんでしたか? eel ライブラリでは、画面作りを html と css で行えます!

html なんか知らない……という場合は tkinter と苦労度は同じかもですが…… html の場合 tkinter よりネットの記事も多いのでラクです! 次から GUI 作るときは慣れた html を使って eel で作りたいと思いました。

![1](https://user-images.githubusercontent.com/28250432/83946778-de13a900-a84d-11ea-9869-4e699a34ee53.png)

「タブ」などもこの通りカンタンに作れました。 tkinter では、どうしたらよいものやら、という感じです。

個人的には、「画面デザイン」と「計算」を言語レベルで(html と Python)ばっさり切り分けられるのも、素敵だと思いました。

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
