Video Capture Gif 画面録画 撮影 関連 Note
===

## Mac で画面キャプチャ

常識だから割愛。

## Mac で画面録画

1. Quick Time Player で画面を録画

## Mac で gif 化

- Gifted アプリでgifに変換
- ffmpeg を使う

```bash
brew install ffmpeg

# ffmpeg -i Input.mov -r FrameRate OutputFilename.gif
ffmpeg -i 画面収録_299U-08-09_1.93.N.mov -r 24 gamen_test1.gif
# よく使う
ffmpeg -i edit.mp4 -r 24 edit.gif
```

## ffmpeg

```bash
# 現在のサイズを取得。
ffprobe -i original.MP4

# リサイズ。自動で縮尺をあわせてほしいほうを -1 にする。
ffmpeg -i original.MP4 -vf scale=640:-1 output.mp4
ffmpeg -i original.MP4 -vf scale=1024:-1 output.mp4
ffmpeg -i original.MP4 -vf scale=1280:-1 output.mp4
ffmpeg -i original.MP4 -vf scale=1600:-1 output.mp4

# 音声削除。 copy が入ってると同時にリサイズはできないっぽい。
ffmpeg -i original.MP4 -vcodec copy -an output.mp4
# よく使う
ffmpeg -i original.mov -vcodec copy -an original.mp4
```

代表的な解像度

- https://qiita.com/riversun/items/d09d8e596a20ec1798f3#169%E3%81%AE%E4%BB%A3%E8%A1%A8%E7%9A%84%E8%A7%A3%E5%83%8F%E5%BA%A6

### 参考

- https://qiita.com/riversun/items/d09d8e596a20ec1798f3
- https://qiita.com/cha84rakanal/items/e84fe4eb6fbe2ae13fd8


## Windows で画面キャプチャ

- Windows + Shift + S
    - すぐに保存せず、範囲指定とかを選べる。
- Windows + PrintScreen
    - 即座に user/picture/screenshot に保存。
    - 保存先は以下手順でデスクトップにできる。

### 保存先をデスクトップに保存

ピクチャ/スクリーンショット 右クリック > 場所 > 移動 でデスクトップを選択

## Windows で画面録画

- Win + G
    - デフォルト機能なのでぜひ使いたいが、「デスクトップは録画できない」というのが無能すぎる
- ScreenToGif アプリを別途ダウンロード
    - https://forest.watch.impress.co.jp/library/software/screentogif/
    - オプション > 外部ツール > ffmpeg ダウンロード > 録画の雰囲気は Mac の Quick Time Player と同じ > ffmpeg を DL しておけば保存時に gif ではなく avi とか mp4 にできる
