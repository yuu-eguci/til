localStorageNote
===

`localStorage` を使って、別ウィンドウ別タブ同士でデータをやり取りできる!

## ウィンドウその1

```javascript
/**
 * ウィンドウその1
 * localStorage を1秒ごとに見張り、変数 aaaa があれば中身を取り出して表示する。
 */

// 初回起動時、 localStorage のデータを削除。
localStorage.removeItem('aaaa')

const checkStorage = function () {

  // localStorage をチェック。
  if (localStorage.aaaa) {

    // 変数の中身を取り出す。
    const aaaa = JSON.parse(localStorage.aaaa)
    console.info(aaaa)

  } else {

    // 変数がセットしていなければ1秒後にまた見に行く。
    setTimeout(checkStorage, 1000)

  }
}
checkStorage()
```

## ウィンドウその2

```javascript
/**
 * ウィンドウその2
 * 変数を localStorage にセットする。
 */

localStorage.aaaa = JSON.stringify('あーー')
```