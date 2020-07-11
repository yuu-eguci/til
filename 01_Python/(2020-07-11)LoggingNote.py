"""
loggingNote

"""

import logging


def create_my_logger():
    """モジュール用のロガーを作成します。
    メインの処理とは別に関係ない。
    Returns:
        Logger -- モジュール用のロガー。
    """
    # ルートロガーを作成します。ロガーはモジュールごとに分けるもの。
    logger = logging.getLogger(__name__)
    # ルートロガーのログレベルは DEBUG。
    logger.setLevel(logging.DEBUG)
    # コンソールへ出力するハンドラを作成。
    handler = logging.StreamHandler()
    # ハンドラもログレベルを持ちます。
    handler.setLevel(logging.DEBUG)
    # ログフォーマットをハンドラに設定します。
    formatter = logging.Formatter(
        # NOTE: 改行は逆に見づらいので E501 を無視します。
        '%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s')  # noqa: E501
    handler.setFormatter(formatter)
    # ハンドラをロガーへセットします。
    logger.addHandler(handler)
    # 親ロガーへの(伝播をオフにします。
    logger.propagate = False
    return logger


logger = create_my_logger()
logger.debug('でばーぐ')
logger.info('いんーふぉ')
logger.warning('うぉーにん')
logger.error('えろあ')
logger.fatal('ふぇーたる(critical と同じっぽい)')
logger.critical('くりてぃこぉ')

try:
    raise Exception('自作例外')
except Exception:
    logger.exception('れーがい。発生した例外は raise されません。ただしこのあとに print されます。')

print('例外は raise されないからこの print は表示される。')
