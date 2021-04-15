DjangoRestFrameworkNote
===

## 基本形作成

```bash
# NOTE: デプロイ環境と合わせること。たとえば Azure AppService なら今のとこ3.8までしかない。
pipenv install --python 3.8

pipenv install django djangorestframework markdown django-filter

# mysql を使う場合、 App Service を使う場合はこれも。
pipenv install pymysql whitenoise

# .gitignore
# NOTE: GitHub 上で gitignore を作ると自動で作られるよ。
open https://github.com/jpadilla/django-project-template/blob/master/.gitignore

# Initialize Django
# NOTE: 最初のうちは、 -project つけるといいかもと思った。 config もいいけど。
django-admin startproject config .

# Add apps
# NOTE: これは config と同階層に作るか、 config 内に作るかは知らん。中に作ったほうがいいか?
python manage.py startapp app

# Migrate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin

# Run
python manage.py runserver
```

## REST framework の場合

このあたりを参考に serializers.py とか views.py を編集しないといかん。

- https://www.django-rest-framework.org/
- https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8

まあいちいち記事見るのも面倒だから書いとく。以下4ファイル settings, urls, views, serializers を編集すればフツーに見れるハズ。

```python
# settings.py
INSTALLED_APPS = [
    'rest_framework',  # <-- 追加
]
```

```python
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
# NOTE: viewsets とやらは views.py で定義する。
router = DefaultRouter()
# r'api/v1/users' にすればその URL でアクセスできる。
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # NOTE: ViewSet を使って↑のように書くことで、こういうのが全部省略できる。
    # path('users/', user_list, name='user-list'),
    # path('users/<int:pk>/', user_detail, name='user-detail'),

    # Django 本来のアドミン画面。
    path('admin/', admin.site.urls),
    # トップ画面を REST framework にする。
    path('', include(router.urls)),
    # NOTE: api-auth/ を追加することで画面に login のリンクが出る。
    path('api-auth/',
         include('rest_framework.urls',
                 namespace='rest_framework'),
         ),
]
```

```python
# views.py
from rest_framework import viewsets
from rest_framework import permissions
from app.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
```

```python
# serializers.py
# 新たに作るファイル。
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
```

## Non model ModelViewSet を作るときの追加ブツ

- init.py
- serializers.py
- views.py
- urls.py

```python
# __init__.py
class Portfolio(object):
    """
    GET /api/v1/portfolio で返却する予定の model らしきものです。
    NOTE: GET /api/v1/portfolio を rest_framework で実装したいけれど、
          Model の無い ModelViewSet を実装する方法がわかりません。
          テキトーに {foo:foo} とかだけ出す API をどう作ればいいの?
          というわけでこちらの repository を参考にして実装しました。
          https://github.com/linovia/drf-demo
          Thank you.
    """

    def __init__(self, **kwargs):
        for field in ('id', 'foo', 'bar', 'baz'):
            setattr(self, field, kwargs.get(field, None))
```

```python
# serializers.py
class PortfolioSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    foo = serializers.CharField(max_length=256)
    bar = serializers.CharField(max_length=256)
    baz = serializers.CharField(max_length=256)
```

```python
# views.py
from rest_framework.response import Response
# __init__.py に定義しているクラスです。
from . import Portfolio

class PortfolioViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = PortfolioSerializer

    def list(self, request):
        # NOTE: 今回は list は不要だが、これがないとトップページの API リストにこの ViewSet が載らない。
        serializer = PortfolioSerializer(instance=[], many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # NOTE: pk を user id として扱えばいいかな。
        sample_portfolio = Portfolio(
            id=123,
            foo='FOOOO',
            bar='BAAAR',
            baz='BAAAZ',
        )
        try:
            # NOTE: 本来ならここで一件取得するらしい。
            # task = tasks[int(pk)]
            pass
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # NOTE: many=True をつけることで返却値が単一オブジェクトではなくリストになります。
        #       そのときは instance=[sample_portfolio] となる。
        #       retrieve は一件返却なので many=False
        #       def list のほうでは複数にするのだろう。
        serializer = PortfolioSerializer(instance=sample_portfolio)
        return Response(serializer.data)
```

```python
# urls.py
# NOTE: The base to use for the URL names that are created.
#       (って書いてあるけど URL になるのは第一引数だ。どゆこと?)
#       If unset the basename will be automatically generated based on the queryset attribute of the viewset, if it has one.
#       Note that if the viewset does not include a queryset attribute
#       then you must set basename when registering the viewset.
#       (portfolio は non model API なので、 queryset が無い。わざわざ定義する必要がある。)
# NOTE: でも上述したとおり URL になるのは第一引数だ。なんのために basename を定義してるのかわからん。
#       それを表すため、意味のない値 foo を設定しています。
router.register(r'portfolio', views.PortfolioViewSet, basename='foo')
```
