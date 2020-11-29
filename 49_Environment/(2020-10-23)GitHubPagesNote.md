GitHub Pages Note
===


## 静的な HTML プロジェクトの場合

- いっとうカンタン。
- settings から GitHub Pages を ON にするだけ。


## vue-cli プロジェクトの場合

- Personal access token を作る。
    - 自分の settings > Developer settings > Personal access tokens > Generate new token > てきとうにリポジトリの名前とかで作る(What’s this token for? って但し書きがあるからわかりやすいよね) > repo にチェックをいれる
- PERSONAL_TOKEN として登録する。
    - Repository の settings > secrets > new secret
- ↓にある .github/workflows/nodejs.yml を作る。
    - `secrets.PERSONAL_TOKEN` のとこが↑で作ったやつね。
    - `./dist` はプロジェクトのどこにも記載がないけど、 `yarn build` したときビルドファイル生成されるフォルダのことです。
    - このあたりについては peaceiris/actions-gh-pages を使っている。この他にも別ブランチにデプロイする方法とかが README に載ってる。
        - https://github.com/peaceiris/actions-gh-pages
    - カスタムドメインで運用するときは `CUSTOM_DOMAIN_FOR_THIS_REPOSITORY` も secrets に追加する。
        - これを設定しないと、 Actions が走るたびにカスタムドメインの設定が空白になる。
- Actions から Enable GitHub Actions みたいなボタン押して有効化。
- `name: github pages` って定義してるから、 All workflows > github pages で CI/CD が始まっているはず。
- vue.config.js に publicPath を追加。↓に例示する。
    - そのままデプロイされると `https://[username].github.io/[repositoryname]/` の URL にデプロイされるからパスがずれる。

```yaml
name: github pages

on:
  push:
    branches:
      - master

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2

    - name: Setup Node
      uses: actions/setup-node@v1
      with:
        node-version: '10.x'

    - name: Cache dependencies
      uses: actions/cache@v1
      with:
        path: ~/.yarn
        key: ${{ runner.os }}-node-${{ hashFiles('**/yarn.lock') }}
        restore-keys: |
          ${{ runner.os }}-node-

    - name: Install dependencies
      run: yarn install

    - name: Build
      run: yarn build

    - name: deploy
      uses: peaceiris/actions-gh-pages@v3
      with:
        personal_token: ${{ secrets.PERSONAL_TOKEN }}
        publish_dir: ./dist
        cname: ${{ secrets.CUSTOM_DOMAIN_FOR_THIS_REPOSITORY }}
```

```JavaScript
module.exports = {
  // サブドメイン時のためのパラメータです。
  // ./ にすると assets は解決する。だけど spa が解決しなかった。
  // TODO: カスタムドメインでの運用が始まったら消すこと。
  publicPath: '/repositoryname/'
}
```


## カスタムドメインの設定

### サブドメインの場合

1. お名前でドメインを CHAME: `[username].github.io` に設定
1. GitHub リポジトリの settings > Custom domain
1. Enforce HTTPS にチェック入れる。

### Apex domain の場合

……やったことないけど。

1. お名前でドメインを A: ↓の ip address で設定。
1. あとはサブドメインと同じなんじゃない?

```plaintext
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```
