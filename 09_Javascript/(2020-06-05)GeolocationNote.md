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
