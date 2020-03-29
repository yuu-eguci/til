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

## BootstrapVue

- [https://bootstrap-vue.js.org/docs](https://bootstrap-vue.js.org/docs)

```bash
yarn add vue bootstrap-vue bootstrap
```

```javascript
import { BootstrapVue } from 'bootstrap-vue'
Vue.use(BootstrapVue)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
```

### b-table

- https://bootstrap-vue.js.org/docs/components/table

```javascript
export default {
  data() {
    return {
      // カラム名情報。
      fields: [
        {
          key: 'column0',
          label: '名前',
          sortable: true,
          // カラムの色。https://bootstrap-vue.js.org/docs/reference/color-variants/
          variant: '',
        },
        {
          key: 'showDetails',
          label: '勤務状況',
          sortable: false,
          variant: '',
        },
      ],
      items: [
        {
          isActive: true,
          column0: 'わたし',
          // セルの色。
          _cellVariants: { column0: 'info' },
        },
        {
          isActive: true,
          column0: 'あなた',
          _cellVariants: { column0: 'warning' },
        },
      ],
    }
  }
}
```

```html
<!--
  striped とかは↑ url の「Table styling」のところにある。
  :fields がカラム名 :items はレコード。
-->
<b-table
  striped
  hover
  small
  fixed
  :items="items"
  :fields="fields"
>
  <!-- あるカラムのデザインを変えたい場合。 -->
  <template v-slot:cell(column0)="row">
    <b-link to="/members">{{ row.item.column0 }}</b-link>
  </template>

  <!-- ログを開くやつ。 -->
  <template v-slot:cell(showDetails)="row">
    <!-- As `row.showDetails` is one-way, we call the toggleDetails function on @change -->
    <b-form-checkbox v-model="row.detailsShowing" @change="row.toggleDetails">
      ログを見る
    </b-form-checkbox>
  </template>
  <template v-slot:row-details="row">
    <b-card>
      <b-card-text>ろぐ</b-card-text>
      <b-row class="mb-2">
        <b-col sm="3" class="text-sm-right"><b>9:00</b></b-col>
        <b-col>作業中</b-col>
      </b-row>
      <b-row class="mb-2">
        <b-col sm="3" class="text-sm-right"><b>12:00</b></b-col>
        <b-col>作業中断</b-col>
      </b-row>
      <b-row class="mb-2">
        <b-col sm="3" class="text-sm-right"><b>13:00</b></b-col>
        <b-col>作業中</b-col>
      </b-row>
    </b-card>
  </template>
</b-table>
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

```javascript
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

```javascript
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

## vue-router のライフサイクル(って言っていいのかな?)

1. `router.beforeEach`
1. 親 route record の `beforeEnter`
1. 子 route record の `beforeEnter`

```javascript
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    // これら各 route の object は route record と呼ばれる。(children 内のも同じく。)
    {
      // この親 route record が開かれたときに呼ばれる。各 child が開かれるときは呼ばれない。
      // 各 child が開かれるときの処理は後述の beforeEach に書く。
      beforeEnter: (to, from, next) => {
        console.info('2. 親 route record の beforeEnter だよ')
        next()
      },
      path: '/',
      component: App,
      children: [
        // このひとつひとつも route record。
        {
          path: '',
          name: 'Home',
          component: () => import(/* webpackChunkName: "home" */ '../views/Home.vue'),
          // この route record が開かれたときに呼ばれる。
          beforeEnter: (to, from, next) => {
            // これ、出ない。
            console.info('3. 子 route record の beforeEnter だよ')
            next()
          },
        },
        {
          path: 'about',
          name: 'About',
          component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
        },
      ]
    },
  ],
})

router.beforeEach((to, from, next) => {
  console.info('1. router.beforeEach だよ')
  // next() を呼ばないといけない。
  next()
})
```

## i18n

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

```javascript
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

```javascript
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

## @

tsconfig.json に `@` を定義しているところがあって、 src 直下のパスとして扱える。

```json
{
"paths": {
  "@/*": [
    "src/*"
  ]
}
```

- `'@/views/Home.vue'`
- `<img alt="Vue logo" src="@/assets/logo.png">`: template タグ内の img src にも使えるみたい。
