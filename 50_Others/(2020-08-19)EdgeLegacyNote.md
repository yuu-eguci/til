Edge Legacy Note
===

- クソ窓をクリーンインストールしたら最初から新 Edge が入っていて、アンインストールができない・・・・・・

## コマンドで強制的にダウングレード

- エクスプローラで `C:\Program Files (x86)\Microsoft\Edge\Application` へ。
- そこのフォルダにいまの Edge のバージョンがある。それをコピっとく。
- cmd を管理者権限で開く。
- 下記コマンドで強制ダウングレード。

```plaintext
cd "C:\Program Files (x86)\Microsoft\Edge\Application\[ここにコピったバージョン]\Installer"
setup.exe --uninstall --system-level --verbose-logging --force-uninstall
```

### 参考

- [Microsoft EdgeをChromium版から以前のEdgeに戻す手順（Edgeダウングレード）](http://tanweb.net/2020/03/11/31135/)

## Blocker Toolkit

- ダウンロード。
	- https://docs.microsoft.com/ja-jp/deployedge/microsoft-edge-blocker-toolkit
- MicrosoftEdgeChromiumBlockerToolkit.exe を実行すると、展開先を聞かれるからてきとうに。 EdgeChromium_Blocker.cmd とかが出てくる。
- cmd を管理者権限で開く。
- EdgeChromium_Blocker.cmd のところまで移動。
- 下記コマンドで新 Edge のインストールをブロックする。

```plaintext
> EdgeChromium_Blocker.cmd /B

MICROSOFT TOOL KIT TO DISABLE DELIVERY OF
MICROSOFT EDGE (CHROMIUM-BASED)

Copyright (C) Microsoft Corporation.  All rights reserved.

LOCAL!
Blocking deployment of Microsoft Edge (Chromium-based) on the local machine
この操作を正しく終了しました。
```

ブロックを解除したいときは U オプションね。

```plaintext
> EdgeChromium_Blocker.cmd /U
```

### 参考

- [新しい Edge 用の Blocker Toolkit が公開](https://hebikuzure.wordpress.com/2019/12/18/new-edge-blockertoolkit/)
