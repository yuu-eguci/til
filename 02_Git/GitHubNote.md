GitHubNote
===


## hub コマンド

### Mac

```bash
$ brew install hub
$ which hub
/usr/local/bin/hub
```

### Windows

- [https://github.com/github/hub/releases](https://github.com/github/hub/releases)
- ぱそこ再起動。

### hub コマンドに紐づく GitHub アカウントを変更

`~/.config/hub` ファイルを消せ。


## コマンドラインから PR する準備

これがウェブページでデフォで出来ないのは不便。 GitLab を見習って。 GitLab はそもそもコミットがなくても PR できるんだからな。

```bash
$ git checkout ORIGINALBRANCH
$ git checkout -b BRANCHNAME
$ git commit --allow-empty -m "Make PR"
$ git push origin BRANCHNAME
$ hub pull-request
```

以上を alias 化したものが以下。 gitconfig に追加。

```gitconfig
[alias]
    # $1 : Default branch (where make new branch from)
    # $2 : New branch
    # $3 : If you want to add options to pull-request command
    #    : --reviewer(-r) --assign(-a) --milestone(-M) --labels(-l) --draft(-d)
    #    : --browse(-o)   --message(-m) "Title"        --edit(-e) < path/to/message-template.md
    # tip: When you have .github/PULL_REQUEST_TEMPLATE.md, no need to add -m and -e. Probabil.
    # ref: https://hub.github.com/hub-pull-request.1.html
    mkpr = !"f() { git checkout $1; git checkout -b $2; git commit --allow-empty -m \"Make PR\"; git push origin $2; hub pull-request $3; }; f"
```

使い方はこう。

```bash
$ git mkpr ORIGINALBRANCH BRANCHNAME "-r xxx,xxx -a xxx,xxx -l xxx,xxx"
```

`subl` の設定をしておけばこのあと PR の編集画面が開く。


### subl の設定

これを打つ。

```bash
$ ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" "/usr/local/bin/subl"
$ git config --global core.editor "subl -w"
```


## GitHub 開発フロー

1. Milestone 作成
    - 例: `v.1.0.0 Initial release`
1. Issue 作成
    - 追加機能やバグはすべて Issue で管理。
    - Milestone と Assignees を設定する。Assignees が実装を行う。
1. Branch と PR を作成。
    - `git mkpr BRANCHNAME`
    - BRANCHNAME は `ユーザ名/機能名(_区切り)`
    - PR 名は `[WIP] BRANCHNAME`
1. Commit, Push
    - 試行錯誤の過程は除くこと。
    - コミットメッセージは英語で。
    - バグ修正は `Fix + 修正内容 + (Issue番号)` `ex. Fix entry dialog (#1)`
    - 機能追加は `Add + 追加内容 + (Issue番号)` `ex. Add entry dialog (#1)`    
1. レビュー準備が出来たら
    - Reviewers, Assignees, Labels, Milestone 設定
    - `[WIP]` を外して Reviewers へ mention を送る。
    - PR のコメントに `fixes #ISSUE番号` をつけるとマージと同時に issue を閉じてくれる。


## Slackと連携

参考

```
https://get.slack.help/hc/ja/articles/232289568-GitHub-%E3%81%A8-Slack-%E3%82%92%E9%80%A3%E6%90%BA%E3%81%95%E3%81%9B%E3%82%8B#%E3%82%A2%E3%83%97%E3%83%AA%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B
```

- [https://slack.github.com/](https://slack.github.com/) にアクセス。
- /github subscribe owner/repo issues,pulls,statuses,public,commits:all,releases,comments,branches,reviews

使い始めるとき

```plaintext
# チャンネル作る

# チャンネルの中で /github を打つ
# このチャンネルに github さんを含めますか? って訊かれるのでイエス。
/github

# subscribe のコマンドを打つ
# この repo がまだ slack 連携に含まれてなかったら、 github ページに飛んで手続きを行う。チェックをつける程度。
/github subscribe owner/repo issues,pulls,statuses,public,releases,comments,reviews

# もういっぺん subscribe
# これで OK
/github subscribe owner/repo issues,pulls,statuses,public,releases,comments,reviews

# unsubscribe
# subscribe のオプションを付け直したいときも一度これを
/github unsubscribe owner/repo
```

### Could not find resource: owner/repo

自分がそのリポジトリの権限を持っていることは当然として……
↓コマンドで GitHub アカウントへのサインインをやり直せる。

```
/github signin
```

## Organization と individual

Organization private と individual private を同時に使うことになったので、違いをメモしていく。

|                    |    Organization    |      Individual     |
|--------------------|--------------------|---------------------|
| 外部のユーザを招く | 有料シート枠が必要 | 3人まで無料追加可能 |
| PR の Draft 機能   | 使える             | 使えない            |
|                    |                    |                     |

## GitHub Desktop で unable to access エラー

別の固定 IP で使っていたぱそこを他の Wifi で使っているとき、 GitHub Desktop が使えねえ。

```plaintext
fatal: unable to access 'https://github.com/yuu-eguci/work-notes.git': schannel: failed to receive handshake, SSL/TLS connection failed
```

`~/.gitconfig` にこれを足したら動いた。

```plaintext
[http]
    sslbackend = openssl
```

## Commit から PR を探す方法

このクソコードいつのタイミングで紛れ込んだんだ? -> どこの PR で見逃したんだ?

1. ファイルの blame から、クソコードが追加されたコミットを探す
1. ここから PR に行くのが面倒なんだけど、コミットのページの一番上に `feature/a (#170, #98) + feature/b (#168, #98) + v0.0.1 (#98)` こんな表示がある
1. なんかよくわかんないんだけど、このへんをクリックするとコミット履歴が出てくるから、そこからギリ、コミットが含まれる PR を探せる……
