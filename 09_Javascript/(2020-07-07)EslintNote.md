Eslint Note
===

## Sample code

このノートを設けたのは、このコメントを参照することが多いため。

```JavaScript
// eslint-disable-next-line @typescript-eslint/no-var-requires
// eslint-disable-line @typescript-eslint/no-var-requires
// eslint-disable-line @typescript-eslint/no-unused-vars
/* eslint-disable */
// eslint-disable-next-line no-console
```

## VSCode で使う

```bash
npm install -g eslint
npm run lint

npm install -g eslint eslint-plugin-vue
```

TypeScript で使いたいときは

```json
"eslint.validate": [
    "javascript",
    "typescript",
]
```

## eslint + eslint-plugin-vue

長らく、 eslint による波線が vscode のエディタに出ないことにモヤモヤしていたけど、少なくとも以下の方法で、 ShuumulatorWeb には波線が出た。グローバルの eslint を参照するかローカルのを参照するかが分水嶺だったような気がする。

***

- vscode eslint: https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint
- eslint-plugin-vue: https://eslint.vuejs.org/user-guide/#usage

vue-cli でプロジェクトを作った時点でふたつはインストール済みだと思う。

```bash
# 最新化したいときはこう。なんか upgrade 使いづらい。
yarn remove eslint eslint-plugin-vue
yarn add -D eslint eslint-plugin-vue
```

```bash
# .eslintrc.js を作る。
./node_modules/.bin/eslint --init  # ローカル(プロジェクト内)にインストールした場合。
# 一応、いまぼくはこっち↑を推してる。リポジトリ内で完結するほうがいい気がする。
# eslint --init  # ←グローバルに eslint をインストールした場合はこう。
```

.eslintrc.js として ShuumulatorWeb で作ったもの↓。

```js
module.exports = {

    // XXX: ./node_modules/.bin/eslint --config .eslintrc.js . が plugin:vue を無視しやがる。なぜ? わからない。
    //      plugin:vue の lint を行うときは↓のいずれかを使うほかない。
    //      vscode はちゃんと plugin:vue を表示してくれてる。
    //      yarn lint も plugin:vue に反応する。
    // NOTE: yarn lint は自動で auto fix が走る。嫌なら yarn lint --no-fix を使うこと。

    "root": true,
    // env: 静的検証の前提条件
    //      brwoser -> document, onload 等ブラウザのグローバル変数を有効にする。
    //      node -> require 等が定義される
    //      es6 -> ES6 の構文が有効になる。ただし ES Modules 機能は有効にならない。 parserOptions.sourceType で定義して。
    "env": {
        "browser": true,
        "es6": true,
        "node": true,
    },
    // NOTE: サードパーティやESLintが推奨するベースのルールを設定する。
    "extends": [
        "eslint:recommended",
        "plugin:vue/recommended"
    ],
    // NOTE: 有効にするグローバル変数。
    "globals": {
        "Atomics": "readonly",
        "SharedArrayBuffer": "readonly"
    },
    "parserOptions": {
        // NOTE: ECMAScript の構文を有効にする。
        "ecmaVersion": 2018,
        // NOTE: env.es6=true だけでは有効にならない ES Modules を有効にする。
        //       コードを module として扱うと予約語が増えたり強制的に strict mode になったりする。
        //       既存コードを module として扱うと壊れる可能性があるため、 env.es6 とは別定義になっている。
        "sourceType": "module",
        // NOTE: import とか? を有効にする設定。
        //       vue-cli の初期設定でついてくる。
        "parser": "babel-eslint",
    },
    // NOTE: サードパーティによって定義されたルールを有効にする。
    "plugins": [
        "vue"
    ],
    // NOTE: 何かを有効にしたり、無効にしたり。あまり特別ルールは足したくないね。
    "rules": {
    }
};
```

vue-cli で作ったプロジェクトの場合、 package.json に eslintConfig があると思う。そっちは要らない。削除。

この方法、 .eslintrc.js の一番上にあるような問題がある。

```js
// XXX: ./node_modules/.bin/eslint --config .eslintrc.js . が plugin:vue を無視しやがる。なぜ? わからない。
```
