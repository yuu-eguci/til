vue-router Note
===


## Installation

```bash
yarn add vue-router
```


## 基本形

ptf-vue-alime repository の [#4 ✨ vue-router を src にシンプルに導入](https://github.com/yuu-eguci/ptf-vue-alime/commit/fe4dd1a03e68cd01ee3805d37127a01dbfd33173)より。

```JavaScript
// main.js
import router from './router';  // 追加。

new Vue({
  router,  // 追加。
  render: h => h(App),
}).$mount('#app')
```

```vue
App.vue
<template>
  <div id="app">
    <router-view />
  </div>
</template>
```

```JavaScript
// src/router.js ファイルごと追加。
import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

const routes = [
  {
    path: '/',
    name: 'HelloWorld',
    component: () => import('./components/HelloWorld.vue'),
  },
];

const router = new Router({
  mode: 'history',
  routes,
});

// ページ遷移ごとに発生する処理です。
router.beforeEach(async (to, from, next) => {
  // next() は必須です。
  next();
});

export default router;
```


## vue-router と vue-i18n を組み合わせて、 url に locale を含めたいときの基本形

- router-view だけもつ component を作る。
- それを component としてもつ親 route を定義して、その children に各ページを定義する。
- HACK: 結果的に生成される `<div id="locale-parent">` は本来不要なものなので、これを省く方法を知れたらこの情報はアップデートされるだろう。

```vue
LocaleParent.vue
<template>
  <div id="locale-parent">
    <router-view />
  </div>
</template>
<script>
// router の親 component としてのみ使用される空っぽの component です。
// 詳細は router.js に記載しました。
export default {
  name: 'LocaleParent',
}
</script>
```

```JavaScript
// router.js
const routes = [
  {
    // NOTE: App.vue <router-view /> の中身がこの route になります。
    //       この route の component を App.vue にすると、 App.vue の中で App.vue が描画されることになります。
    //       ようは <div id="app"><div id="app">[children]</div></div> こうなるってことです。
    //       当然嫌なので、空っぽの component を用意しています。
    //       こうすると <div id="app"><div id="locale-parent">[children]</div></div> こうなります。(GOOD)
    // HACK: もし「component なし route」みたいなのが定義できるならそれがいい。
    //       今は知らないのでこういうかたちにしました。
    path: '/:locale',
    component: () => import('./LocaleParent.vue'),
    beforeEnter(to, from, next) {
      // URL の locale によって使用する locales ファイルを切り替えます。
      // NOTE: VUE_APP_I18N_FALLBACK_LOCALE 環境変数のおかげで ['en', 'ja', 'ro'].includes(to.params.locale)
      // というようなチェックは必要ありません。
      i18n.locale = to.params.locale;
      next();
    },
    children: [
      {
        path: '',
        name: 'HelloWorld',
        component: () => import('./components/HelloWorld.vue'),
      },
      {
        path: '2',
        name: 'HelloWorld2',
        component: () => import('./components/HelloWorld2.vue'),
      },
    ]
  },
  // 想定外の URL は /en へリダイレクトします。 '/' とかね。
  {
    path: '*',
    redirect: '/en',
  },
];
```


## vue-router のライフサイクル(って言っていいのかな?)

1. `router.beforeEach`
1. 親 route record の `beforeEnter`
1. 子 route record の `beforeEnter`

```JavaScript
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
            // これ(debug)、出ない。
            console.debug('3. 子 route record の beforeEnter だよ')
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

  // こんな風に、遷移先の Route に値を足すことで……
  to.params['bar'] = 'BAR';
  // component 側でこんなふうに参照できる……
  // console.log(this.$route.params.bar);
  // 注意: App.vue のほうが router より早く呼ばれるから App.vue のほうで参照はできない。

  // でも params や query は url の情報が格納されているところだ。
  // props はこう。
  to.matched[0].props.default.baz = baz;


  // next() を呼ばないといけない。
  next()
})
```
