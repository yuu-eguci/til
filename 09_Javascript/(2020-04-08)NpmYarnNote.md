npm & yarn Note
===

このふたつはセットでノートにしてもいいのでは? というわけで。

## よく使うやつ

### npm

```bash
# npm のバージョン。
npm --version

# グローバルのパッケージを1階層表示
npm list --depth 0

# package-lock.json を更新するコマンド。
npm install --package-lock-only
```

### yarn

```bash
yarn install --network-timeout 60000

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

DevOps pipelines 上の yarn install で発生する問題。

- `https://...tgz` を resolved で持つパッケージを upgrade する。
- それで変わらなかったら、 yarn.lock のそのパッケージの部分を削除して、 yarn install し直すと更新されることがあった。
- あるいは、 yarn.lock を破棄して yarn install し直し、新しい resolved で昔の yarn.lock を更新する。

とくにふたつのメジャーバージョンが混在しているパッケージのとき非常に面倒くさい。
