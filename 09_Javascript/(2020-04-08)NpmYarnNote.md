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
