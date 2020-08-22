Vue-cli Note
===


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

## d-none 系のクラス

わかりづらいからメモっていく。 `sm` は「sm 以上で」という意味である。

- `d-sm-none` sm 以下で表示。
- `d-none d-sm-block` sm 以上で表示。

## b-table

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
  <!-- あるヘッダのデザインを変えたい場合。 -->
  <template v-slot:head(marker)="data">
    {{data.label}}aaa
  </template>

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

## toggle

### card を toggleable

```html
<b-card no-body class="mb-3">
  <b-card-header header-tag="header" class="p-1" role="tab">
    <b-button block href="#" v-b-toggle.accordion-1 variant="light">
      タイトル
    </b-button>
  </b-card-header>
  <!-- visible をつけると最初から開いてる。 -->
  <b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
    <b-card-body>
    </b-card-body>
  </b-collapse>
</b-card>
```

## フォームにアイコンを

```html
<!-- アイコンがテキストでいい場合 -->
<b-form-group label="タイトル:" size="sm">
  <b-input-group prepend="@" size="sm">
    <b-form-input v-model='foo' trim></b-form-input>
  </b-input-group>
</b-form-group>

<!-- アイコンを fontawesome にしたい場合 -->
<b-form-group label="タイトル:" size="sm">
  <b-input-group size="sm">
    <div class="input-group-prepend">
      <span class="input-group-text"><i class="fa fa-user"></i></span>
    </div>
    <b-form-input v-model='bar' trim></b-form-input>
  </b-input-group>
</b-form-group>

<!-- ついで。セレクトボックス -->
<b-input-group prepend="タイトル">
  <b-form-select v-model="baz" :options="options"></b-form-select>
</b-input-group>
```

## b-popover

```html
<!-- これマジでハマりどころなんだけど Safari では triggers="focus" が動作しない。 -->
<!-- 動作させるために href="#" をつける必要がある。 -->
<b-button :id="`markers`" href="#">
  foo
</b-button>
<b-popover :target="`markers`" triggers="focus" title="マーカー">
  bar
</b-popover>
```
