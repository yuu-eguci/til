
SQL Server Note (SQLserverNote)
===


## 環境作成

- SSMS と SQLserver インストール。


## 環境編

#### 01. ローカルの SQL server に繋ぐとき

SSMS で SQL server で自分のPCを選択して windows認証。

#### 02. エクスポートがしたい

- DB 右クリック(この DB は「データベース」の下階層のスキーム名を指す。)
- スクリプト生成
- エクスポートしたいテーブルにチェック
- 次へ
- 詳細設定
- スクリプトを作成するデータの種類 でいつも Workbench で選んでいる「構造のみ、データのみ」が選べる


#### 03. インポートがしたい

上のエクスポートで作成したファイルはスキーマからの作成SQLになっている。だからテーブルのCREATEからやりたいなら中のテキストを切り抜いて実行すればOK。


## って何? 編

#### 01. 認証が2種類あんの何?

- Windows認証: デフォルトの認証。
- SQL Server認証: 専用ユーザ、パスワードでの認証。

#### 02. セキュリティ > ログイン にある sa って何?

最高権限をもつユーザ。Mysqlのrootみたいなもんかな? sysadminロールを持つ。

ただし使用は推奨されないっていうかMicrosoftはSQL Server認証自体を認証してない。デフォルトでは無効になっている。(アイコンにバツがついてる。)


## SQL 編

#### 01. LIMIT がやりたい

n 件目から m 件を取得。

```sql
SELECT *
    FROM table
    OFFSET n ROWS FETCH NEXT m ROWS ONLY
```

いちばんはじめから3件。

```sql
    OFFSET 0 ROWS FETCH NEXT 3 ROWS ONLY
```

一度の表示件数が5件で、3ページ目。(11件〜15件)

```sql
    OFFSET 10 ROWS FETCH NEXT 5 ROWS ONLY
```

#### OFFSET FETCH を速くする方法

```sql
-- これを
OFFSET 0 ROWS FETCH NEXT 20 ROWS ONLY

-- こうする
DECLARE @a int = 20;
OFFSET 0 ROWS FETCH NEXT @a ROWS ONLY
```

参考: [大きいデータの時の OFFSET FETCH は定数でクエリ書いた方が有利そう？](https://odashinsuke.hatenablog.com/entry/2016/06/28/221732)

**パラメータ化すると内部でソートの方法が変わる**のでそういうことになると言う。……が、意味がよくわからない。わかるときはくるだろうか。

#### 02. SQL の中で変数使いたいんですけど

`DECLARE` で宣言するときは型に注意しないとだめ。 `string` とかざっくりしたのは使えない。めんど。

```sql
DECLARE @NUM char(6);
SET @NUM='000010';
DELETE FROM table1 WHERE code=@NUM;
DELETE FROM table2 WHERE code=@NUM;
DELETE FROM table3 WHERE code=@NUM;
```

#### 03. 全テーブルの件数を知りたい

```sql
SELECT
    OBJ.name, IND.rows
FROM sys.objects AS OBJ
JOIN sys.sysindexes AS IND
ON OBJ.object_id = IND.id AND IND.indid < 2
WHERE OBJ.type = 'U'
ORDER BY OBJ.name;
```

`type='U'` はユーザテーブル。

#### 04. SQLの履歴が見たい

```sql
SELECT creation_time, text
FROM   sys.dm_exec_query_stats qs
CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) st
WHERE creation_time >= 'yyyy-mm-dd'  -- 別になくてもいいけどね
ORDER BY creation_time DESC -- 別になくてもいいけどね
```

#### オートインクリメントにする

```sql
column_name bigint IDENTITY(1,1) NOT NULL
```

## SSMS 絞り込んで編集する

上位200行の編集 > 上メニューのクエリデザイナー > ペイン > SQL
