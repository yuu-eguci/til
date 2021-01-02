Vue-cli Note
===

なんで Vue なんて名前にしたんですかね。(View と聞き間違えながら)

## (2019-05-22)VueNote のメモ

> なんで Vue なんて名前にしたんですかね。(View と聞き間違えながら)

当時と感想変わらなくてワロタ。

### 始めてから一週間の奴が Vue について概説する

何もしらん一週間前のぼくに説明するなら……。

お、いまのぼくがどう感じるか見てみよう。

- HTML を分割して親ファイルと子ファイル(今のとこ親 vue 子 vue って呼んでる)に分ける作りだよ。
- 親 vue から子 vue を include する感じ。
    - 親 vue の中で `<子VUEの名前></子VUEの名前>` こんなふうに書くと include になる。
    - 子 vue の名前は子 vue の中で `parasails.registerComponent('子VUEの名前', ...` みたいに書いて登録する。
- 各 vue は変数を持てる。 data とか prop がある。
- prop は親から引き継ぐやつ。よって一番トップの親 vue にはない。
- data は各 vue 固有のやつ。 prop と同じ名前にしないこと。
- 変数は親子間でリアクティブに変更を受け取り合うことができる。

わかりやすいと思った例は「検索バーに打ち込まれるたびにテーブルの行を絞り込んでリアクティブに検索結果を表示」。

```plaintext
# 親子 vue 関係
- 親 vue  
  data: 検索ワード
    - 子 vue 検索バー  
      prop: 検索ワード  
      常に入力テキストを watch して検索ワードの変数に入れる。親経由で行の vue へ渡す
    - 子 vue テーブルの行  
      prop: 検索ワード  
      親から回ってきた検索ワードを使って絞り込んで表示する。
```

## 導入

```bash
yarn global add @vue/cli
yarn global upgrade --latest @vue/cli
vue create PROJECT_NAME
# これでもいいのかな。
npx @vue/cli create PROJECT_NAME
```

## バージョン確認

```bash
# npm
npm --version

# vue-cli
vue --version

# vue 自体
npm list vue
```

## @fortawesome/vue-fontawesome

- [https://www.npmjs.com/package/@fortawesome/vue-fontawesome](https://www.npmjs.com/package/@fortawesome/vue-fontawesome)

```bash
yarn add @fortawesome/fontawesome-svg-core
yarn add @fortawesome/free-solid-svg-icons
yarn add @fortawesome/free-regular-svg-icons
yarn add @fortawesome/free-brands-svg-icons
yarn add @fortawesome/vue-fontawesome
```

```JavaScript
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(fas, fab, far)
Vue.component('font-awesome-icon', FontAwesomeIcon)
```

```html
<font-awesome-icon :icon="['fas', 'info-circle']" />

<!-- 等幅 -->
<font-awesome-icon :icon="['fas', 'info-circle']" class="fa-fw" />
```

## htmlWebpackPlugin.options.title を変更

vue.config.js を手動追加。

```JavaScript
module.exports = {
  pages: {
    index: {
      entry: 'src/main.ts',
      title: 'たいとる',
    }
  }
}
```

## v-for

```typescript
// for で回したいデータ。
export default {
  data() {
    return {
      items: [
        {
          to: '/company',
          icon: ['fas', 'info-circle'],
          title: 'foo',
          description: 'foo',
        },
        {
          to: '/facilities',
          icon: ['fas', 'home'],
          title: 'bar',
          description: 'bar',
        },
      ]
    }
  }
}
```

```html
<!-- for で回す。 -->
<Item
  v-for="item in items"
  :to="item.to"
  :icon="item.icon"
  :title="item.title"
  :rawHtmlDescription="item.description"
  :key="item.id" <!-- これゼッタイ必要。 -->
/>
```

- https://jp.vuejs.org/v2/guide/list.html#コンポーネントと-v-for
  - 2.2.0 以降で key は必須。
  - item をそのままコンポーネントに渡さないことがここで推奨されてる。

コンポーネント側。

```typescript
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class TopListGroupItem extends Vue {
  @Prop() private to!: string;
  @Prop() private icon!: string[];
  @Prop() private title!: string;
  @Prop() private rawHtmlDescription!: string;
}
```

```html
<!--  -->
<b-list-group-item :to="this.to"> <!-- タグ内にはこう渡すみたい。 -->
  <div class="d-flex w-100 justify-content-between">
    <h5 class="mb-1">
      <font-awesome-icon :icon="this.icon" class="fa-fw" />
      {{this.title}} <!-- ふつーに表示。 -->
    </h5>
  </div>
  <p class="mb-1" v-html="this.rawHtmlDescription"></p> <!-- HTML のサニタイズを妨害するやつ。 -->
</b-list-group-item>
```

## i18n(vue-cli-plugin-i18n)

> The vue-cli-plugin-i18n that has been released on npm will be released as @intlify/vue-cli-plugin-i18n in near future.

らしい。わくわくだね。ページごとに翻訳 json を用意するという記事もあるけどそれは kazupon/vue-cli-plugin-i18n ではなく kazupon/vue-i18n だから注意。

```bash
vue add i18n
```

```plaintext
? The locale of project localization. en
? The fallback locale of project localization. en
? The directory where store localization messages of project. It's stored under `src` directory. locales
? Enable locale messages in Single file components ? No  # ←何を意味するかわからない。
```

これだけで全体的に src が変わる。

```json
// メッセージの定義はこう。 ja.json en.json ro.json
// 下に示すようにページごともできるらしい!
{
  "message": "やあ i18n !!",
  "hello": "Hallo {name}!",
  "wolves": "no wolf | one wolf | a pack of wolves",
  "wolves2": "no wolf | one wolf | a pack of {n} wolves",
  "wolves3": "no wolf | one wolf | a pack of {numberOfWolves} wolves",

  // 構造化可能
  "main-screen": {
      "title": "Main screen",
      "description": "This is the main screen..."
  },
  "about-screen": {
      "title": "About screen",
      "description": "That's what this is all about...."
  },
}
```

```html
<!-- 使い方。シンプルな html -->
<p>{{ $t('message') }}</p>
<p>{{ $t('hello', { name: 'Vue.js'}) }}</p>

<!-- 複数形 -->
<p>{{ $tc('wolves', 1) }}</p>
<p>{{ $tc('wolves2', 5) }}</p>
<p>{{ $tc('wolves3', 5, {numberOfWolves: 5}) }}</p>

<!-- 属性で使う -->
<sub-component :title="$t('message')"></sub-component>

<!-- 構造化したやつ使う -->
<p>{{ $t('about-screen.title') }}</p>
```

### URL で i18n

1. 親 route record のパスを `/:locale` で設定。
1. `router.beforeEach` で locale をもとに `i18n.locale` をセット。

```JavaScript
routes: [
  {
    // :locale 動的セグメントです。これをもとに beforeEach 内で i18n.locale をセットします。
    path: '/:locale',
    component: App,
    children: [
      {
        path: '',
        // ...
      }
    ]
  }
]

router.beforeEach((to, from, next) => {
  // URL の locale を i18n.locale にセットします。
  if (['en', 'ja', 'ro'].includes(to.params.locale)) {
    // OK.
  } else {
    return next('en')
  }
  i18n.locale = to.params.locale

  // beforeEnter では next() を呼ばないといけない。
  next()
})
```

## 認証要求のページ

1. 認証要求のページに `requiredAuth` を設定。
1. `router.beforeEach` で認証確認。

```JavaScript
{
  path: 'admin',
  name: 'Admin',
  component: () => import(/* webpackChunkName: "admin" */ '../views/Admin.vue'),
  // Admin ページを表示するためには認証が必要であるとします。
  meta: { requiredAuth: true },
}

router.beforeEach((to, from, next) => {
  // meta: { requiredAuth: true } を指定した route のときこれが true になります。
  if (to.matched.some(record => record.meta.requiredAuth)) {
    // 今回はてきとうに、 GET クエリに auth=ok があったときとします。
    if (to.query.auth === 'ok') {
      // ok ならそのまま流して、 next() を実行します。
      console.info('認証 ok')
    } else {
      // ng ならトップへ。
      console.info('認証 ng')
      next({
        name: 'Home', query: { redirect: to.fullPath }
      })
      return
    }
  }

  // beforeEnter では next() を呼ばないといけない。
  next()
})
```

## Vuex

書くこと多すぎるので ptf-vue 参照……でも大事なところをすこし記録。 TypeScript と JavaScript で違うので、参考記事が見つけづらい……。

```typescript
// types.ts
export interface RootState {
  version: string;
}

export interface I18nState {
  locale: string;
}
```

```typescript
// index.ts
import Vue from 'vue'
import Vuex, { StoreOptions } from 'vuex';
import { RootState } from './types';
import { i18n } from '@/store/modules/i18n'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const store: StoreOptions<RootState> = {
  state: {
    version: '1.0.0',
  },
  modules: {
    i18n,
  },
  plugins: [
    createPersistedState({
      storage: window.sessionStorage
    })
  ],
}

export default new Vuex.Store<RootState>(store)
```

```typescript
// modules/i18n.ts
import { Module, GetterTree, MutationTree, ActionTree } from 'vuex';
import { I18nState, RootState } from '@/store/types';

const state: I18nState = {
  locale: 'en',
}

// GetterTree<I18nState, RootState> この部分よくわかってない。
const getters: GetterTree<I18nState, RootState> = {
  locale: (state: I18nState) => {
    return state.locale
  },
}

const mutations: MutationTree<I18nState> = {
  set: (state: I18nState, newLocale: string) => {
    state.locale = newLocale
  },
  remove: (state: I18nState) => {
    state.locale = ''
  },
}

const actions: ActionTree<I18nState, RootState> = {
}

export const i18n: Module<I18nState, RootState> = {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
}
```

```typescript
// getters 経由で取得
this.$store.getters['モジュール名/データ名']
this.$store.getters['i18n/locale']

// mutations 実行
this.$store.commit('モジュール名/定義したメソッド名', '引数')
this.$store.commit('i18n/locale', 'en')
this.$store.commit('i18n/locale', this.$i18n.locale)

// actions 実行
this.$store.dispatch('increment')
```

## @ アットマーク

tsconfig.json に `@` を定義しているところがあって、 src 直下のパスとして扱える。

```json
{
  "paths": {
    "@/*": [
      "src/*"
    ]
  }
}
```

- `'@/views/Home.vue'`
- `<img alt="Vue logo" src="@/assets/logo.png">`: template タグ内の img src にも使えるみたい。

## 環境変数

環境変数ファイル

- .env.local
- .env.staging
- .env.production

中身

```plaintext
NODE_ENV='local'
VUE_APP_API_BASE_URL='http://localhost:1337'
```

使うとき

```JavaScript
// eslint-disable-line @typescript-eslint/no-console
console.info(process.env.VUE_APP_API_BASE_URL)
```

環境切り替え package.json

```json
"serve": "vue-cli-service serve --mode production",
"build:local": "vue-cli-service build --mode local",
```

## test:unit mixin

package.json

```json
"test:unit": "vue-cli-service test:unit 'tests/**/*.spec.{j,t}s'"
```

@/mixins/util.js

```JavaScript
export default {
  methods: {
    foo() {
      return 'aaa';
    },
  }
}
```

tests/unit/mixin/util.spec.js

```JavaScript
import { expect } from 'chai';
import dateUtil from '@/mixins/dateUtil.js';

describe('JS', () => {
  it('should success', () => {
    expect(dateUtil.methods.foo()).to.deep.equal('aaa');
  })
});
```

コンポーネントでの呼び出し方。

```JavaScript
// ...
import util from '@/mixins/util';
// ...
mixins: [util]
// ...
this.foo()
```

## v-model を component で使う

```html
<!-- 親側 -->
<MyComponent :label="'タイトル'" v-model="title" />

<!-- 子側 -->
<b-form-input v-model="innerValue" trim></b-form-input>
<script>
export default {

  props: [
    'value',
  ],

  computed: {

    // NOTE: このコンポーネントで v-model を使うための実装です。
    innerValue: {
      get() {
        return this.value
      },
      set(val) {
        this.$emit('input', val)
      }
    }
  },

}
</script>
```

## ハマるとこ

- 自分のコンポーネントに `@click` をつけるときは `@click.native` と書く!
- .env.local は全環境で読み込まれる!
