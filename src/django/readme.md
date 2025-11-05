# This is Django Study

## 2025.10.27
1. make project
   1. 명세 작성
   2. 가상환경 만들기
      1. 프로젝트 아리브러리를 다른 프로젝트와 분리하면 여러가지 장점이 있음, 배포시 꼭필요함
      2. python -m venv ll_env
      3. 가상환경 활성화 하기
         1. source ll_env/bin/activate
   3. Django 설치
      1. [here](https://docs.djangoproject.com/en/5.2/)
      2. pip install --upgrade pip
      3. $ python -m pip install Django
      4. django-admin startproject ll_project .
         1. startproject는 ll_project라는 새 프로잭트를 시작합니다. 마지막 점은(".") 개발을 완료 했을때 어플리케이션을 서버에 배포하기 쉬운 폴더구조를 사용해 프로젝트 시작
         2. manage.py
            1. 명령을 받아 Django의 관련 부분으로 전달하는 쩗은 프로그램, 이 명령을 사용해 데이터베이스 작업, 서버실행 같은 작업을 수행
         3. settings.py, urls.py, wsgi.py
            1. settings.py
               1. Django가 시스템에 접근하고 프로젝트를 관리하는 방법을 지정, 프로젝트를 진행하면서 이 설정 중 일부를 수정하거나 추가할 겁니다.
            2. urls.py
               1. 브라우저의 요청에 응답해 어떤 페이지를 만들지 지정
            3. wsgi.py
               1. Django가 생성한 파일을 전송하는 역활, wsgi는 "web server gateway interface"의 약자
   4. 데이터베이스 생성
      1. Django는 프로젝트 정보 대부분을 데이터베이스에 저장
      2. python manage.py migrate
   5. 프로젝트 확인하기
      1. runserver
         1. python manage.py runserver
         2. http://127.0.0.1:8000/
   6. 애플리케이션 시작하기
      1. Django프로잭트는 개별 애플리케이션 그룹으로 구성
         1. 지금은 애플리케이션 하나를 만들어 대부분의 동작 수행
      2. 앞에서 연 터미널의 개발 서버를 계속 실행고 있어야 함
      3. 새로운 터미널을 열고 mange.py가 있는 폴더에서 가상환경 활성 startapp 명력
         1. python manage.py startapp learning_logs
         2. __init__.py, admin.py, apps.py, models.py, tests.py, views.py
         3. models.py 중요함
            1. 애플리케이션에서 사용하는 데이터를 정의
         4. admin.py, views.py가 중요함
      4. 모델 정의하기
         1. models.py 
            1. model이란 Django가 애플리케이션에서 저장되는 데이터를 사용하는 방법
            2. 모델은 클래스
            3. 모델에서 사용할 수 있는 필드 [refer page](https://docs.djangoproject.com/en/4.1/ref/models/fields)
      5. 모델 사용하기
         1. 모델을 사용하려면 어플리케이션에 포함시켜야함
         2. settings.py
            1. INSTALLED_APP 
               1. 기본 엡을 덮어써야 하는 경우가 있어 직접만든 애플리케이션을 기본 앱보다 앞에 배치 해야 함
         3. 데이터베이스 수정
            1. python manage.py makemigrations learning_logs
            2. python manage.py migrate
            3. 학습로그에서 관리하는 데이터를 수정할 때마다 model.py수정 --> learning_logs에서 makemigrations호출 --> 프로젝트 migrate 이렇게 3단계를 거침