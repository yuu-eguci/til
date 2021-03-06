npm & yarn Note
===

このふたつはセットでノートにしてもいいのでは? というわけで。

## よく使うやつ

### npm

```bash
# npm のバージョン。
npm --version

# npm のバージョンを変更する。
npm install -g npm@6.14.12
# ちなみに nodejs とのバージョン対応はこちら: https://nodejs.org/ja/download/releases/

# ローカルのパッケージを1階層表示
npm list --depth 0
# グローバルのパッケージを1階層表示
npm list --depth 0 -g

# package-lock.json を更新するコマンド。
npm install --package-lock-only

# 削除(-g でグローバルから)
npm uninstall PACKAGE -g

# バージョンをアップデートするときのセット。
# outdated で新しいバージョンが出ているものをチェック -> uninstall で package から削除 -> install することで最新が入る。
# ただし、 npm-check-updates を使ってもっとシンプルにやるのがいいらしい。
npm outdated
npm uninstall PACKAGE
npm install PACKAGE
```

### yarn

```bash
yarn install --network-timeout 60000

yarn add PACKAGE

yarn remove PACKAGE
```

## "${MODULE_A}" has unmet peer dependency "${MODULE_B}" の対応

```bash
# ふつーはこっち。
yarn add "${MODULE_B}"

# A が開発用のパッケージならこっち。
yarn add -D "${MODULE_B}"
```

## エラー Client network socket disconnected before secure TLS connection was established

```bash
yarn add PACKAGE --trusted-host
```

## error An unexpected error occurred: "https://...tgz: unexpected end of file"

(2020-10-12)根治。これは中国国内向けのミラーサイト taobao を使おうとしているから起きている。プロジェクトのルートに .vuerc を置いて↓を書こう。

(2020-11-02)いやこれ yarn install には効いてなくね?!

```json
{
  "useTaobaoRegistry": false
}
```

***

以下、 `useTaobaoRegistry` を知らなかったころの対処療法。

DevOps pipelines 上の yarn install で発生する問題。

- `https://...tgz` を resolved で持つパッケージを upgrade する。
    - `yarn upgrade @vue/cli-service@^4.2.0` こんな感じ。
- それで変わらなかったら、 yarn.lock のそのパッケージの部分を削除して、 yarn install し直すと更新されることがあった。
- あるいは、 yarn.lock を破棄して yarn install し直し、新しい resolved で昔の yarn.lock を更新する。

とくにふたつのメジャーバージョンが混在しているパッケージのとき非常に面倒くさい。
