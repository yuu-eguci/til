"""
dotenv Note

Python で環境変数を取得するノート。
waka-box で実践してる。

os.environ['SECRET_API_KEY']  KeyError あり。
os.getenv('SECRET_API_KEY')  None が返る。
"""


class EnvNotFoundError(WakaBoxException):
    """特定の環境変数が見つからないことを表す例外クラス。

    Arguments:
        WakaBoxException {[type]} -- [description]
    """


# .env で環境変数を取得する場合に対応します。
# raise_error_if_not_found: .env が見つからなくてもエラーを起こさない。
dotenv.load_dotenv(dotenv.find_dotenv(raise_error_if_not_found=False))


def get_env(keyname: str) -> str:
    """環境変数を取得します。

    Arguments:
        keyname {str} -- 環境変数名。

    Raises:
        EnvNotFoundError: 環境変数が見つからない。

    Returns:
        str -- 環境変数の値。
    """
    try:
        # GitHub Actions では環境変数が設定されていなくても yaml 内で空文字列が入ってしまう。空欄チェックも行います。
        _ = os.environ[keyname]
        if not _:
            raise KeyError(f'{keyname} is empty.')
        return _
    except KeyError as e:
        raise EnvNotFoundError(keyname) from e
