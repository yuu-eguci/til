Vue-cli Note
===

なんで Vue なんて名前にしたんですかね。(View と聞き間違えながら)


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

b-table の内容を更新するときは b-table に ref="mainTable" をつけて、 `this.$refs.mainTable.refresh();` する。
