RedisNote
===

## Medis

Mac 用のクライアントアプリ。

```bash
# 導入するとき。
cd /Applications
git clone https://github.com/luin/medis.git
cd medis
npm install
npm run-script build
nohup npm start &>/dev/null &
```

```bash
# 次回以降起動するとき。
cd /Applications/medis
nohup npm start &>/dev/null &

# NOTE: ……このコマンド何。
```

## Sails.js の session id の解析方法

```
sid: s%3AVe3fOoTbaCHHL_k3DTzW8FIB4eGN9qPH.LfEE3IZlPx%2FgPWopJU5eWbVg7s9NZx%2BS27cN%2B69NX%2BA
↓
分解して……
↓
s%3A
Ve3fOoTbaCHHL_k3DTzW8FIB4eGN9qPH  <-- ここが redis のキー
.
LfEE3IZlPx%2FgPWopJU5eWbVg7s9NZx%2BS27cN%2B69NX%2BA
```
