"""
mysql-connector-python Note

pip install mysql-connector-python
"""

import mysql.connector


try:
    # DB 接続を行います。
    mysql_connection_config = {
        'host': os.environ['MYSQL_HOST'],
        'user': os.environ['MYSQL_USER'],
        'password': os.environ['MYSQL_PASSWORD'],
        'database': 'schemaName'
    }
    connection = mysql.connector.connect(**mysql_connection_config)
    logger_info_for_azure('MySQL 接続 is_connected: '
                          f'{connection.is_connected()}')

    # 試しに SELECT を行ってみます。
    select_sql = ' '.join([
        'SELECT ... %s %s',
    ])
    # これが fetch 結果にカラム名を付与する属性。
    cursor = connection.cursor(dictionary=True)
    # %s とコレがプレースホルダー。
    cursor.execute(select_sql, (2, 0))
    records = cursor.fetchall()
    cursor.close()
    print(records)

    # 試しに UPDATE を行ってみます。
    update_sql = ' '.join([
        'UPDATE ...',
    ])
    cursor = connection.cursor(dictionary=True)
    cursor.execute(update_sql, (2008,))
    cursor.close()

except Exception:
    print('MySQL との接続でれーがい:')

else:
    connection.commit()

finally:
    # HACK: with ステートメントで書けるようにする。
    connection.close()
