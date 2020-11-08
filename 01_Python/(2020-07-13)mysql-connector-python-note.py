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


#
# ↓ with statement で
#


class DbClient:
    """DB アクセスを行うクラスです。 with 構文で使用可能です。
    """

    def __enter__(self):
        mysql_connection_config = {
            'host': MYSQL_HOST,
            'user': MYSQL_USER,
            'password': MYSQL_PASSWORD,
            'database': MYSQL_DATABASE,
        }
        self.connection = mysql.connector.connect(**mysql_connection_config)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

    def find_target_images(self, limit: int = None) -> list:
        """本プログラムの処理対象のレコードを HistoryFaceImage から取得します。

        Returns:
            list: FaceImage のリスト。
        """

        select_sql = ' '.join([
            'SELECT',
                'id,',  # noqa: E131
                'createdAt,',
                'imagePath',
            'FROM historyfaceimage',
            'WHERE',
                'recognitionStatus = %s',
            'ORDER BY id DESC',
            f'LIMIT {limit}' if limit else '',
        ])
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(select_sql, (WorkProgressStatus.WAITING,))
        records = cursor.fetchall()
        cursor.close()

        # レコード状態ではなく、モデル状態で返します。
        # NOTE: azure-cognitiveservices-vision-face がそういう作りだったため倣ってみます。
        face_images = [FaceImage.from_history_face_image_record(_)
                       for _ in records]

        return face_images

    def set_undetected_completed_status(
            self, history_face_image_ids: list) -> None:
        """顔が検出されなかったデータを更新します。
        単に COMPLETED を付与するだけです。

        Args:
            history_face_image_ids (list): 更新対象の HistoryFaceImage.id。
        """

        if not history_face_image_ids:
            return

        # id 用のプレースホルダです。
        placeholder = get_placeholder(len(history_face_image_ids))

        # [COMPLETED, id, id, id, ...] です。
        placeholder_values = [WorkProgressStatus.COMPLETED]
        placeholder_values.extend(history_face_image_ids)

        update_sql = ' '.join([
            'UPDATE historyfaceimage',
            'SET',
                'recognitionStatus = %s,',  # noqa: E131
                # FIXME: %H:%i:%s にすべき。
                # NOTE: ただ mysql.connector のプレースホルダ %s とバッティングし使用できない……。
                "updatedAt = DATE_FORMAT(NOW(), '%Y-%m-%dT%H:%i:00.000Z')",
            f'WHERE id IN ({placeholder})',
        ])
        cursor = self.connection.cursor()
        cursor.execute(update_sql, tuple(placeholder_values))
        cursor.close()
        self.connection.commit()


with functions.DbClient() as db_client:
    face_images = db_client.find_target_images()
