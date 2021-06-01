MySQLWorkbenchNote
===

MySQLNote とかに散ってた情報を Workbench に関連するものだけまとめたノート。
結構 Workbench 指定で情報欲しいときあるから作りました。

## MySQL Workbench 関連のあれこれ

- MySQLworkbenchでsqlファイルをimportするときのエラー
    - Cannot load from mysql.proc. The table is probably corrupted
    - シェルから mysql_upgrade -u user -p で解決した(もちろんこのあとでパスワードを入れる)
- フォントサイズを変えたい
    - C:\Users\user\AppData\Roaming\MySQL\Workbench\wb_options.xml
    - ってのをエディタで開いて、"Font"っていう表記があるところの数字を変える。マジ見やすくなるぜ。
- MySQL Workbench 8.0.23.CE は Catalina で crash する
    - https://stackoverflow.com/questions/65798626/mysql-workbench-crashes-on-mac-os-fresh-install
    - > downgrading to 8.0.22 from MySQL archives allows it to startup without a problem.
    - https://downloads.mysql.com/archives/workbench/

## エクスポート -> インポートするときの tips

- Export to Dump Project Folder のほうが1ファイルが小さくなるから嬉しいが、インポートでエラーが出る。(ことがある)
    - ERROR 1044 (42000): Access denied for user 'admin'@'%' to database 'schemaname'
- 今の所 Export to Self-Contained File しか使ったことない。
- Export > Advanced Options... > Other lock-tables のチェックを外すことでエクスポート時のテーブルロックをナシに出来る。
    - でかい DB のバックアップを取るときはコレ必須だ。
    - この設定は docs.microsoft.com で読んで知った。
        - https://docs.microsoft.com/ja-jp/azure/mysql/concepts-migrate-import-export#data-export
        - あざす。

## 再インストール時に必須 接続先のエクスポート

- Tools > Configurations > Backup Connections
