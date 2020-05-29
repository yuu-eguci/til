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
