AngularNote
===

- [ドキュメント](https://angular.jp/docs)

## angular-cli

```bash
# angular-cli 入ってたっけ?
npm ls --depth=0 -g

# angular-cli インストール。
npm install -g @angular/cli@latest

# プロジェクト作成。
ng new PROJECT --style=sass

# Would you like to add Angular routing? (y/N)
# SPA 使うか? ってこと。

# WARN の解決。 dev にしたほうがいいとかある?
npm install --save core-js@^3 jasmine-core@^3.5

# angular-cli-ghpages 追加。
ng add angular-cli-ghpages

# コンポーネント追加。
ng generate component COMPONENT
```

## GitHub Pages で公開

サブドメインの設定方法。 apex domain の場合は違う。

1. お名前でドメインを CHAME: username.github.io に設定
1. GitHub リポジトリの settings > Custom domain
1. Enforce HTTPS にチェック入れる。

Apex domain の場合……やったことないけど。

1. お名前でドメインを A: ↓の ip address で設定。
1. あとはサブドメインと同じなんじゃない?

```plaintext
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```
