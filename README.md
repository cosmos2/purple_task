# purple nest task

## Note
유저와 반려동물 정보를 제공하는 장고 프로젝트입니다.
DB는 postgresql 12.0으로 구성하였습니다.
view는 rest-framework의 viewset과 장고의 class-based generic views 2가지를 이용하였습니다.
circleCI가 적용되어있고 codecov로 코드 커버리지를 확인 할 수 있습니다.
테스트 서버를 위한 settings는 `purple.settings.local` 입니다.
`python manage.py runserver_plus --settings=purple.settings.base`로 서버를 구동합니다.

## Packages
### django-extensions
- `django-admin.py`보다 조금 더 향상된 정보를 제공합니다.
- 모델들이 미리 로드된 `shell_plus`나 디버깅 기능이 향상된 `runserver_pllus` 덕분에 개발이 더 용이했습니다.

### codecov
- 소프트웨어의 테스트가 얼마나 코드를 커버하고 있는지 알 수 있는 지표를 제공합니다.
- CI와 함꼐 사용하면 코드를 PR하고 리포트를 바로 받아 볼 수 있습니다.

### pytest
- 테스트케이스 작성을 도와주는 도구입니다.
- fixture 모듈과 플러그인을 통한 확장성이 장점입니다.
- 해당 프로젝트에서는 `pytest-django`와 `pytest-cov`를 사용하여 pytest로 테스트케이스를 작성하였습니다.

### virtualenv
- 해당 프로젝트의 라이브러리, 모듈 등의 개발환경을 격리시키는 가상환경 도구입니다.

### psycopg2
- 파이썬에서 postgresql를 동작하게 도와주는 라이브러리 입니다.

### django-restframework
- django에서 REST API 제작을 편리하게 해주는 프레임워크입니다.

### Werkzeug
- `django-extentions`의 `runserver_plus`의 디버깅 기능을 사용하기 위해 설치한 WSGI 라이브러리 입니다.

### mixerr
- 장고 인스턴스를 쉽고 빠르게 생성해줍니다. 테스트 케이스 작성시 도움을 주는 라이브러리입니다.

## Authors
김도연 [Saturn Kim Blog](https://saturnkim.dev/).