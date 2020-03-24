Vue-cli Note
===

## 導入

```bash
yarn global add @vue/cli
yarn global upgrade --latest @vue/cli
vue create PROJECT_NAME
# これでもいいのかな。
npx @vue/cli create PROJECT_NAME
```

## BootstrapVue

- https://bootstrap-vue.js.org/docs

```bash
yarn add vue bootstrap-vue bootstrap
```

```javascript
import { BootstrapVue } from 'bootstrap-vue'
Vue.use(BootstrapVue)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
```

## @fortawesome/vue-fontawesome

- https://www.npmjs.com/package/@fortawesome/vue-fontawesome

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
      title: 'Taskal Time-Card',
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
