MySQL Note
===


## SQLって何だし

Structured Query Language 構造化問い合わせ言語


## 使えるようになるまで

xamppでスタートして、xampp-mysql-binのmysql.exeのパスをコピーして、コマンドプロンプトに貼り付けて実行
管理者権限がアレだったりでうまくやれん場合
    binディレクトリで mysql -h localhost -u root
登録されてるユーザがわかんねえ場合
    xampp-mysql-resetroot.batをコマンドプロンプトから実行すると登録されているユーザー名が出てくる。
アクセスを拒否される場合
    Access denied と出る場合、パスワードがあってないって意味
    Host ... is not allowed と出る場合、そのホスト(localhostとか)が許可されてないって意味

## ユーザのパスワードを変更する

update user set password=password("password") where user='root';
commit;

## 最初に必要になりそうなコマンド

DBリストとかDBの中身をみる
    show databases;
    show tables;
DBの中に入る
    use {name};
DBとかテーブルを作る column名は例
    create database {name};
    create tabel {name} (
        no int not null primary key,
        year int,
        winner varchar(2))
    default character set = utf8;
DBを消す
    drop database {name};

## DB内で日本語が文字化けする問題

my.ini(xamppコンパネから飛べる)
[myspl][client]欄に
default-character-set = utf8 追加
[mysqld]欄に
character-set-server=utf8 追加

## 日付

マジであっちでもこっちでも日付は面倒くさいな。

```sql
-- UTC 日付を iso フォーマットで取得。
DATE_FORMAT(UTC_TIME(), '%Y-%m-%dT%H:%i:00.000Z')
```
