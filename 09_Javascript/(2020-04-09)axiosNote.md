axios Note
===

## インストール

```bash
yarn add axios
```

## axios.defaults 設定

```javascript
axios.defaults.headers['Content-Type'] = 'application/json;charset=UTF-8';
axios.defaults.withCredentials = true;
```

## SessionID を持続させたい

axios は使い方にパターンがあってすげえ調べづらい。

### axios() のパターン

configObject を使うパターン、とも言う。

```javascript
const response = await axios({
  url: 'http://hitoren.net/api/v1/example',
  method: 'POST',
  withCredentials: true,  // これが大事。ただこれをつけると Access-Control-Allow-Credentials ヘッダ絡みの cors エラーが起こることも。(true がかえらないとダメ)
  data: {
    foo: 'foo',
  },
  headers: {
    'Content-Type': 'application/json;charset=UTF-8',
  },
});
```

### axios instance のパターン

```javascript
const axiosInstance = axios.create({
  baseURL: 'http://hitoren.net',
  headers: {
    'Content-Type': 'application/json',
  },
  responseType: 'json',
  withCredentials: true,
});

// request を使う。
const response = await axiosInstance.request({
  url: '/api/v1/example',
  method: 'POST',
  data: {
    foo: 'foo',
  },
});

// post を使う。
const response = await axiosInstance.post('/api/v1/example', {
  foo: 'foo',
});


// delete を使う。
// delete では謎に
const response = await axiosInstance.post('/api/v1/example', {
  data: { foo: 'foo' },
});
```

### axios.post のパターン

```javascript
const response = await axios.post('http://hitoren.net/api/v1/example', {
  foo: 'foo',
}, {
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json;charset=UTF-8',
  },
});
```

## 例外処理

Axios は返却コードが200じゃないとき? 例外をぶん投げるのでマジで注意。

`.catch` の部分がないと200以外の body 部を取得できない。

```JavaScript
const res = await axios.get("/user?id=123")
 .catch(err => {
   return err.response
 });

if (res.status !== 200) {
   console.log("例外発生時の処理")
}
```

## cors の問題

参考になった。

- https://qiita.com/att55/items/2154a8aad8bf1409db2b#axios-を使う場合
- https://info.yama-lab.com/LaravelのAPI別ドメインからaxiosを使ってアクセス

> axios では「サーバーサイドの実装では一つ注意点があります。」  
> Access-Control-Allow-Origin で \*(ワイルドカード) を設定しているとエラーが返されてしまいます。  
> credentials mode (withCredentials パラメータを着けている場合) では Access-Control-Allow-Origin は \*(ワイルドカード) だとダメとのこと。  
> なので、このように Origin を明示的に指定する必要があります。  
> - Access-Control-Allow-Origin: https://trusted-one.co.jp // CORS を許可する Origin を明示的にする  
> - Access-Control-Allow-Credentials: true  
> ちなみに、Node.js で cors module を使う場合は以下のような実装で解決できました。  
> import cors from 'cors';  
> const app = express();  
> app.use(cors({ origin: true, credentials: true }));  
> クッキーを許可するために ‘Access-Control-Allow-Credentials’ で ’true’を返す。  
> Cookieを許可するのですが、この値を途中、1(数字)と返してしまいすこしはまった。文字列の’true’でうまくいきました。
