SailsNote
===

## layout.ejs 問題

- ページごとに違う layout を使いたい。
- ページごとに違う css を使いたい。

```javascript
// routes.js
'GET /login' :  { action: 'view-login',
                  locals: {
                    layout: 'layouts/layout-login',
                  },
                },
```

```html
// layout-login.ejs

↓ これは消す。勝手に assets の中のファイルが記述されちゃうから。
<!--STYLES-->
<!--STYLES END-->

↓ こうして別途書く。
<link rel="stylesheet" href="/styles/pages/login.css">
```

## intercept

```javascript
// helper からエラーを受け取る。
const newKey = await sails.helpers.subscription.generate.with({
  arg: 1,
}).intercept('duplicateError', () => {
  return 'duplicateError';
});
```

- https://gitter.im/balderdashy/sails?at=5ab44f512b9dfdbc3a113e2f

以下5つは同じ。

```JavaScript
.intercept('E_UNIQUE', 'emailAlreadyInUse')

.intercept('E_UNIQUE', ()=>'emailAlreadyInUse')

.intercept('E_UNIQUE', ()=>{ return 'emailAlreadyInUse'; })

try {
  // …
} catch (err) {
  if (err.code === 'E_UNIQUE') {
    throw 'emailAlreadyInUse';
  } else { throw err; }

try {
  // …
} catch (err) {
  if (err.code === 'E_UNIQUE') {
    return exits.emailAlreadyInUse();
  } else { return exits.error(err); }
```

## update は fetch できるが updateOne はできない

```javascript
// fetch しなくても fetch されてる。
const row = await Table.updateOne({
  arg: 1,
}).set({
  available: false,
});
```

## DevOps pipelines test

出た問題と解放をまとめる。

- Sequelize は実行できる?
  - `npm install sequelize-cli --save` すれば yaml から `./node_modules/.bin/sequelize` でコールできる。
- yaml の中では variable(環境変数的なやつ)を使える。(下に yaml を使える。)
- てか普通に環境変数としてプロジェクト内で使えるらしい。
- sails.lift 後に sails.lower してもプロセスは終わらない。下に書くコードで終わらせないといけない。 DevOps 終わらなくなる。

```yaml
trigger:
- dev

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: NodeTool@0
  inputs:
    versionSpec: '10.15.3'
  displayName: 'Install Node.js'

- script: |
    npm install
  displayName: 'npm install'

- script: |
    npm run lint
  displayName: 'npm run lint'

- script: |
    ./node_modules/.bin/sequelize db:create --url '$(DB_URL)'
    ./node_modules/.bin/sequelize db:migrate --url '$(DB_URL)'
  displayName: 'Prepare DB for tests'

- script: |
    npm run test-on-devops
  displayName: 'npm run test-on-devops'

- script: |
    ./node_modules/.bin/sequelize db:drop --url '$(DB_URL)'
  condition: always()
  displayName: 'Drop DB for tests'
```

```JavaScript
after((done) => {

    // sails.lower を呼び出しただけでは process が終わりません。イベント登録を用いて process を終わらせます。
    // NOTE: exit しないと DevOps での自動チェックが永遠に終わりません。
    sails.on('lower',  () => {
        setTimeout(
            // NOTE: ここは 0 でも 1 でも成立します。どちらにしようが失敗しているテストがあれば DevOps の結果は failed になります。
            //       ひとまず参考コードのまねをして 1 を指定しています。
            () => { process.exit(1); },
            5000
        );
    });

    sails.lower(done);

});
```
