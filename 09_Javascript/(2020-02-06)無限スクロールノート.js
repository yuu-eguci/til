/**
 * 無限スクロール。
 * というか、「下の方までスクロールしたときなんかする」というノート。
 */

$(document).on('load scroll', function () {

  // ページ全体の高さ。
  const documentHeight = $(document).innerHeight()

  // デバイスウィンドウの高さ。
  const windowHeight = $(window).innerHeight()

  // スクロール量。
  const scrollRange = $(window).scrollTop()

  // スクロールの限度。
  const scrollLimit = documentHeight - windowHeight

  // 最下部までの距離。
  const rangeUntilBottom = scrollLimit - scrollRange

  console.info(`スクロール最大値:${scrollLimit}px 最下部まで:${rangeUntilBottom}px`)

  // このとき、最下部までスクロールした。
  // rangeUntilBottom <= 0
  //      (最下部までの距離 <= 0)

  // このとき、最下部から50px のところまでスクロールした。
  // rangeUntilBottom <= 50
  //      (最下部までの距離 <= 50)

  if (rangeUntilBottom <= 50) {
    // やりたいこと。
  }
})