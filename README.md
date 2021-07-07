# Python-Basic-Foundation

## Build Docker Container
```
docker build -t <원하는 이름> .  
ex) docker build -t python-test .
```

## Run Script on Docker Container
```
docker run <위에서 설정한 이름>  
ex) docker run python-test
```

중간에 User Input을 받는다면
```
docker run -it <위에서 설정한 이름>  
ex) docker run -it python-test
```

## Reqirements.txt 관리법
```
설치할 모듈or라이브러리 이름  
설치할 모듈or라이브러리 이름 == 원하는 버전  
ex)  
requests==2.25.1  
beautifulsoup4  
```
