Aviutl Note
===

## Installation

- 公式ページから Aviutl, 拡張編集Plugin, FilterPlugin, 出力Plugin をダウンロード。
    - http://spring-fragrance.mints.ne.jp/aviutl/
- Aviutl/Plugins フォルダ作成。
- Aviutl/Plugins の中に Plugin のファイルを全部入れる。
- L-SMASH Works から L-SMASH Works r940 release1 をダウンロード。
    - https://aviutl.info/l-smash-works/
    - これは Lhaplus ではなく 7-zip で解凍する。 Lhaplus だと解凍エラーが出て、その結果のファイルでは Aviutl でエラーになる。
- 4ファイルを Aviutl/Plugins へ入れる。
    - lwcolor.auc
    - lwdumper.auf
    - lwinput.aui
    - lwmuxer.auf
    - 参考: https://aviutl.info/l-smash-works/
- x264guiEx をダウンロード。 x264guiEx_2.64v3.zip を。
    - https://drive.google.com/drive/u/0/folders/0BzA4dIFteM2dOWhmTXA3bE9WaWs
    - (2020-10-23)なんかこの拡張が Mac Parallels で使えなくなったから入れ直したのだが、場所変わったかも
        - https://www.dropbox.com/sh/q6afzrpcrl8nsda/AACtGgD-V8Z9AnWTmwV6AKo5a -> また変わった
        - ファイル名も x264guiEx_2.65v2.zip になってた。
        - この件で気づいたんだけど、この拡張で出力した mp4 でないと mac のクイックビューで再生できない。
    - 参考: https://aviutl.info/x264guiex-intro/
- 中の auo_setup.exe を実行して、 exe_files をダウンロード。
- この順番で入れれば、 2016.01.29.Sun のメモにある「入力プラグインの優先度の設定」はしなくていいと思う。

## Text

- 拡張編集ウィンドウ右クリック > メディアオブジェクト追加 > テキスト
- 拡張編集でテキストをダブルクリック > このオブジェクト用のウィンドウが出る > 右上の + マークを押してフェードを加える
- あとは勘でいける。

## 「動画の終わりまで」のバー

- 図形で長四角を作る。
- 丁度いい大きさ(長さ)にする。
- クリッピングを + する。
- 上下左右どれか希望するものを直線移動にして、 0 -> [サイズの値] にする。

## WindowSize

- メニュー > 表示 > 拡大表示 > WindowSize
- これが編集しやすい。

## Warning: Detected CTS duplication at frame ...

- ファイル > 環境設定
    - 入力プラグイン優先度 > L-Smash Works File Reader を一番上に
    - 入力プラグインの設定 > L-Smash > Libav+L-Smash のチェックを解除

## ファイルの読み込みに失敗しました

↑の「Libav+L-Smash のチェックを解除」を戻したら解決した。
