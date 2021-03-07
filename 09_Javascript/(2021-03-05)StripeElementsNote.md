Stripe Elements Note
===

## よい感じの記事

- [@y_toku - Stripe.js & Elements を利用して決済フローを理解する](https://qiita.com/y_toku/items/7e51ef7e69d7cbbfb3ca)
- [Stripe.js v3 with Bootstrap 4 (beta) Test](https://codepen.io/skunkbad/pen/BdgYmY)
- [https://stripe.com/docs/testing#international-cards](https://stripe.com/docs/testing#international-cards)

## ひとつの Element に番号、期限、 CVC を押し込むパターン(推奨されている)

```html
<form id="stripe-form">
  <!--
    NOTE: Stripe Elements が mount するには、フォームを BootstrapVue 無しで定義する必要があります。
          素の html で記述します。
  -->
  <div class="form-group">
    <label for="stripe-card-number">カード情報を入力してください</label>
    <div class="input-group">
      <span id="stripe-card" class="form-control">
        <!-- Stripe Card Element -->
      </span>
    </div>
  </div>

  <!-- Used to display form errors -->
  <!-- stripeErrorMessage -->
  <b-alert v-if="stripeErrorMessage" show variant="danger">
    {{ stripeErrorMessage }}
  </b-alert>

  <hr />

  <div class="w-100">
    <p class="float-right">
      <b-button variant="primary"
                id="stripe-submit"
                type="submit"
                :disabled="modalLoading || Boolean(stripeErrorMessage)">
        <font-awesome-icon v-if="modalLoading" :icon="['fas', 'spinner']" spin class="fa-fw" />
        <font-awesome-icon v-else :icon="['fas', 'edit']" class="fa-fw" />
        登録する
      </b-button>
    </p>
  </div>
</form>
```

```js
// 「クレジットカード」タブのフォームに Stripe Elements をマウントします。
initializeStripeElements: async function () {

  // Stripe の API キーです。
  // NOTE: これはテスト用のキーです。 This ensures that you don’t accidentally modify your live customers or charges.
  const stripeApiKey = 'pk_test_...';
  this.stripeInstance = await loadStripe(stripeApiKey);

  // Stripe Elements のインスタンスを生成します。
  const elements = this.stripeInstance.elements();
  // Try to match bootstrap 4 styling
  const style = {
    base: {
      'fontSize': '16px',
      'color': '#495057',
    },
  };
  const cardElement = elements.create('card', {style});
  cardElement.mount('#stripe-card');

  // 入力エラーがあったときその旨表示するイベントです。
  // NOTE: 多くのサンプルで this.$refs.stripeCardErrors に直接 message を格納しています。
  //       今回は message の有無によって b-alert の visility を toggle したいので data 変数に格納します。
  const onChangeEvent = ({error}) => {
    if (error) {
      this.stripeErrorMessage = error.message;
    } else {
      this.stripeErrorMessage = '';
    }
  };
  // Stripe Element にイベントを登録します。
  cardElement.addEventListener('change', onChangeEvent);

  // Submit ボタンにイベントを登録します。
  // 入力されたカード情報を Stripe に送って、こちらでは token を受け取るイベントです。
  const stripeForm = document.getElementById('stripe-form');
  stripeForm.addEventListener('submit', (event) => {
    // ぐるぐるを出します。
    this.modalLoading = true;

    event.preventDefault();
    const payload = {
      // 他のカード情報……名義等をフォームに含めるならばここに記述します。
    };

    // 入力情報を Stripe サーバへ渡します。返却値として token を得ます。
    this.stripeInstance.createToken(cardElement, payload).then(async (result) => {
      if (result.error) {
        this.stripeErrorMessage = result.error.message;
        // ぐるぐるを解除します。
        this.modalLoading = false;
        return;
      }

      // TODO: トークンをサーバに送信
      console.info({ token: result.token });

    });
  });

},
```

## 番号、期限、 CVC を分けるパターン

```html
<form id="stripe-form">
  <!--
    NOTE: Stripe Elements が mount するには、フォームを BootstrapVue 無しで定義する必要があります。
          素の html で記述します。
  -->
  <div class="form-group">
    <label for="stripe-card-number">カード情報を入力してください</label>
    <div class="input-group">
      <span id="stripe-card" class="form-control">
        <!-- Stripe Card Element -->
      </span>
    </div>
  </div>

  <div class="form-group">
    <label for="stripe-card-number">カード番号を入力してください</label>
    <div class="input-group">
      <span id="stripe-card-number" class="form-control">
        <!-- Stripe Card Element -->
      </span>
    </div>
  </div>
  <div class="form-group">
    <label for="card-exp">有効期限</label>
    <div class="input-group">
      <span id="stripe-card-expiry" class="form-control">
        <!-- Stripe Card Expiry Element -->
      </span>
    </div>
  </div>
  <div class="form-group">
    <label for="card-cvc">セキュリティコード</label>
    <div class="input-group">
      <!-- NOTE: CVC -> Card Verification Code の略です。日本で通りがよいため「セキュリティコード」と表記します。 -->
      <span id="stripe-card-cvc" class="form-control">
        <!-- Stripe CVC Element -->
      </span>
    </div>
  </div>
  <!-- Used to display form errors -->
  <!-- stripeErrorMessage -->
  <b-alert :show="stripeErrorMessage" variant="error">
    {{ stripeErrorMessage }}
  </b-alert>

  <button id="stripe-submit" class="btn btn-primary">Submit Payment</button>
</form>
```

```js
// Stripe の API キーです。
// NOTE: これはテスト用のキーです。 This ensures that you don’t accidentally modify your live customers or charges.
const stripeApiKey = 'pk_test_...';
this.stripeInstance = await loadStripe(stripeApiKey);

// DOM が生成されてからでないとこの先の処理はできません。 DOM 生成まで待ちます。
const interval = setInterval(() => {

  // mount 対象の全 DOM が生成されるまで待ちます。
  if (document.getElementById('stripe-card-number')
      && document.getElementById('stripe-card-expiry')
      && document.getElementById('stripe-card-cvc')) {
    // すべて揃っておれば OK.
  } else {
    // でなければまだ待機です。
    return;
  }

  // Stripe Elements のインスタンスを生成します。
  const elements = this.stripeInstance.elements();
  // Try to match bootstrap 4 styling
  const style = {
    base: {
      'fontSize': '16px',
      'color': '#495057',
    }
  };
  const cardNumberElement = elements.create('cardNumber', {style});
  const cardExpiryElement = elements.create('cardExpiry', {style});
  const cardCvcElement = elements.create('cardCvc', {style});
  cardNumberElement.mount('#stripe-card-number');
  cardExpiryElement.mount('#stripe-card-expiry');
  cardCvcElement.mount('#stripe-card-cvc');

  // 入力エラーがあったときその旨表示するイベントです。
  // NOTE: 多くのサンプルで this.$refs.stripeCardErrors に直接 message を格納しています。
  //       今回は message の有無によって b-alert の visible を toggle したいので data 変数に格納します。
  const onChangeEvent = ({error}) => {
    if (error) {
      this.stripeErrorMessage = error.message;
    } else {
      this.stripeErrorMessage = '';
    }
  };
  // 各 Stripe Element に登録します。
  cardNumberElement.addEventListener('change', onChangeEvent);
  cardExpiryElement.addEventListener('change', onChangeEvent);
  cardCvcElement.addEventListener('change', onChangeEvent);

  // Submit ボタンにイベントを登録します。
  // 入力されたカード情報を Stripe に送って、こちらでは token を受け取るイベントです。
  const stripeForm = document.getElementById('stripe-form');
  stripeForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const payload = {
      // 他のカード情報……名義等をフォームに含めるならばここに記述します。
    };

    // NOTE: Stripe Elements を複数に分けているが cardNumberElement のみ指定でよい。
    //       公式 doc にこのタイプのサンプルがない。
    this.stripeInstance.createToken(cardElement, payload).then((result) => {
      if (result.error) {
        this.stripeErrorMessage = result.error.message;
        return;
      }
      // TODO: トークンをサーバに送信
      console.info({ token: result.token });
    });
  });

  clearInterval(interval);

}, 1000);
```
