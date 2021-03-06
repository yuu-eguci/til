Geolocation Note
===

デバイスの経緯度取得。

## await で使う

```javascript
// 経緯度を取得します。
// これが返り値 -> { latitude:[数値], longitude:[数値] }
async getGeolocation() {

  // NOTE: 取得できなかった場合、てきとーに -1 を設定します。
  const meanlessCoords = { latitude: -1, longitude: -1 };

  // 位置情報の取得ができない端末への対応です。
  if (!navigator.geolocation) {
    return meanlessCoords;
  }

  // NOTE: navigator.geolocation.getCurrentPosition を await で利用するためのラッパー関数です。
  const getCurrentPositionAsync = function () {
    return new Promise((resolve, reject) => {
      navigator.geolocation.getCurrentPosition(resolve, reject);
    });
  };

  try {
    const currentPosition = await getCurrentPositionAsync();
    return {
      latitude: currentPosition.coords.latitude,
      longitude: currentPosition.coords.longitude,
    };
  } catch (error) {
    // NOTE: エラーコードです。
    // 1: PERMISSION_DENIED
    // 2: POSITION_UNAVAILABLE
    // 3: TIMEOUT
    meanlessCoords.errorCode = error.code;
    return meanlessCoords;
  }

}
```

## (Chrome)Geolocation permission has been blocked as the user has dismissed the permission prompt several times

これが出るとブラウザの設定画面からブロックを取り消しできなくなる。 URL の左のマークから取り消しできるようになる。

## await なし(非同期)で試す

```js
navigator.geolocation.getCurrentPosition(
  // 取得成功した場合
  function(position) {
      alert("緯度:"+position.coords.latitude+",経度"+position.coords.longitude);
  },
  // 取得失敗した場合
  function(error) {
    switch(error.code) {
      case 1: //PERMISSION_DENIED
        alert("位置情報の利用が許可されていません");
        break;
      case 2: //POSITION_UNAVAILABLE
        alert("現在位置が取得できませんでした");
        break;
      case 3: //TIMEOUT
        alert("タイムアウトになりました");
        break;
      default:
        alert("その他のエラー(エラーコード:"+error.code+")");
        break;
    }
  }
);
```
