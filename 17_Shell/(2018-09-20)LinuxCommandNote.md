
Linux Command Note
===

## よく使うやつ

```bash
$ pwd
$ mount_smbfs '//user%20name%21%21:password@dir/free' '/Users/username/mount'
    # スペースは %20 ビックリマークは %21
$ tar cvzf ".tar.gz" ""
$ tar xvzf ".tar.gz"
$ mv "移動物" "移動先"
$ cp -p "index.php" ".ht--index.php@"
    # -pは全部の属性を引き継ぐ
$ su - username
    # ユーザ切り替え。書かなければルートになる。
$ less ""
$ cat ""
$ cp "original" "copy"
$ chmod 777 ""
$ chmod +x ""
$ rm ""
$ rm -rf "" (ディレクトリを再帰的に消す場合。rmは複数可能)
$ ln -sf "ターゲット(絶対パス)" "シンボ名"
$ wget -r -np {URL}
    # r = recursive, np = no parent

$ sudo tail -f "ファイルパス"
$ source ~/.bash_profile

# このポートを占有してるプロセスを出す。
lsof -i:1337
# PID 指定で殺す。
kill 20

# 環境変数表示。
printenv
```

## curl

```bash
curl -i -b cookie -X PUT http://localhost:1337/api/v1/timecard -H "Content-type:application/json" -d @timecard.json

curl -u admin:password http://127.0.0.1:8000/users/            -H 'Accept: application/json; indent=2'

# -i --include : HTTP ヘッダを出力に含める
# -b --cookie  : クッキーを利用
# -X --request : HTTP メソッド
# -H --header  : ヘッダ情報付与
# -u: ベーシック認証

# よく使うパターン。
API_URL='http://localhost'
C_TYPE_JSON='Content-type:application/json'
AUTH_KEY='Authorization:***'
curl -H $C_TYPE_JSON -H $AUTH_KEY --include \
    -X GET $API_URL'/api/v1/foo?x=1&y=2';
```

- curl コマンドを python に変換: https://curl.trillworks.com/
- ぼくは頻繁に、「GET クエリを ? と & で連結させずに '--data foo=1' みたいな形式で設定できないものか」とか考えるがその考えは捨てろ。
    - いまのところよさげなのが、 POSTMAN アプリで API をコールして、「code」のトコ(右側の `</>` マーク)で curl コマンドを生成してもらうこと。
    - この「code」で urlencode もやってくれるからラクチン。
- なお Postman は cookie にも対応しているからログインも可。

## 出力結果を変数に格納

```bash
VAR=`pwd`
```

## ssh

```bash
# 基本
ssh user@000.000.000.000

# 秘密鍵を使ってログイン
ssh -i /Users/user/.ssh/id_rsa user@000.000.000.000

# 秘密鍵を使わずにログイン
# NOTE: なんか一度秘密鍵を指定すると次から自動で使われちゃうみたい。
ssh -o PubkeyAuthentication=no user@000.000.000.000
```
