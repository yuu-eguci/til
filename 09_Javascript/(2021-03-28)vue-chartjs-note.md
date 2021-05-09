vue-chartjs note
===


## Installation

```bash
yarn add vue-chartjs chart.js
```


## Document

### 公式

公式はここ。

- https://vue-chartjs.org/ja/guide/#初めに

サンプルコードのようなものがズラズラ並んでいるけれど、親コンポーネントから `<MyChart />` みたいに呼ぶときのやり方は下の方にあるから注意。

- https://vue-chartjs.org/ja/guide/#チャートデータの更新

### グラフはどんなふうに作ればええんや

参考になったサイトを書いとく。

- 「どのグラフがいいんだろ。サンプル一覧が見たい」
    - https://www.chartjs.org/docs/latest/samples/bar/stacked.html
- 「だけどこの↑サイトはサンプルコードが見づらい。コードを編集してリアルタイムに反映される様子を見たい」
    - https://www.chartjs.org/docs/latest/charts/bar.html
- 「だけどこの↑サイトは stacked bar chart のサンプルが無い。 stacked(ひとつの単位にプラスとマイナス両方出すやつ)の config はどうすればいいんだろう?」
    - https://github.com/apertureless/vue-chartjs/issues/226#issuecomment-336697199

## 基本形

ChartJs 専用コンポーネントを作る。

```js
// MyChart.vue
// 本 vue には template を書きません。
// NOTE: 棒グラフなら Bar を import する。
import { Line, mixins } from 'vue-chartjs';
const { reactiveProp } = mixins;

export default {

  name: 'MyChart',

  // NOTE: 棒グラフなら Bar を extends だよ。
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
    datacollection: {},
    // NOTE: この options は Bar を出すときの設定です。
    options: {
      responsive: true,
      scales: {
        yAxes: [{
          stacked: true,
          ticks: {
            beginAtZero: true,
          },
        }],
        xAxes: [{
          stacked: true,
          ticks: {
            beginAtZero: true,
          },
        }]
      },
      maintainAspectRatio: false,
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

    // NOTE: Stacked Bar chart の設定はこんなふうに行う。
    const data = {
      labels: ['foo', 'bar'],  // label の一覧。
      datasets: [
        {
          label: 'ひとつめのデータセット',
          data: [65, 59],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 159, 64, 0.2)',
          ],
          borderColor: [
            'rgb(255, 99, 132)',
            'rgb(255, 159, 64)',
          ],
          borderWidth: 1,
        },
        {
          label: 'ふたつめのデータセット',
          data: [-15, -25],
          backgroundColor: [
            'rgba(255, 205, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
          ],
          borderColor: [
            'rgb(255, 205, 86)',
            'rgb(75, 192, 192)',
          ],
          borderWidth: 1,
        },
      ],
    };
    this.datacollection = data;

  },

}
```
