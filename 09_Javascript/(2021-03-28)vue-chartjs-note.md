vue-chartjs note
===


## Installation

```bash
yarn add vue-chartjs chart.js
```


## Document

公式はここ。

- https://vue-chartjs.org/ja/guide/#初めに

サンプルコードのようなものがズラズラ並んでいるけれど、親コンポーネントから `<MyChart />` みたいに呼ぶときのやり方は下の方にあるから注意。

- https://vue-chartjs.org/ja/guide/#チャートデータの更新


## 基本形

ChartJs 専用コンポーネントを作る。

```js
// MyChart.vue
// 本 vue には template を書きません。
import { Line, mixins } from 'vue-chartjs';
const { reactiveProp } = mixins;

export default {

  name: 'MyChart',

  extends: Line,

  mixins: [reactiveProp],

  props: ['options'],

  mounted () {
    // this.chartData is created in the mixin.
    // If you want to pass options please create a local options object
    this.renderChart(this.chartData, this.options)
  },

}
```

親コンポーネント側。

```html
<MyChart :chartData="datacollection"
               :options="options" />
```

```js
import MyChart from '@/components/MyChart.vue';

// components
components: {
  MyChart,
}

// data
data() {

  return {

    // chartjs へ渡すデータです。
    // NOTE: データ形式は公式サイトを参照します。
    //       https://vue-chartjs.org/ja/guide/#最初のチャートの作成
    //       > チャート毎に必要なオブジェクト構造は公式 Chart.js docsをチェックしてください。
    //       > https://www.chartjs.org/docs/latest/#creating-a-chart
    datacollection: null,
    options: {
      responsive: true,
      maintainAspectRatio: false
    },

  };

}

// mounted
async mounted () {

  this.fillData()

}

// methods
methods: {

  fillData () {
    this.datacollection = {
      labels: [this.getRandomInt(), this.getRandomInt()],
      datasets: [
        {
          label: 'Data One',
          backgroundColor: '#f87979',
          data: [this.getRandomInt(), this.getRandomInt()]
        }, {
          label: 'Data One',
          backgroundColor: '#f87979',
          data: [this.getRandomInt(), this.getRandomInt()]
        }
      ]
    }
  },
  getRandomInt () {
    return Math.floor(Math.random() * (50 - 5 + 1)) + 5
  }

}
```
