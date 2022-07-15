# xpass

우분투 기준입니다.


0. apt update
```
sudo apt update
```

1. docker, docker-compose 설치
```
sudo apt install docker.io
sudo apt install docker-compose 
```

2. docker 권한 설정
```
sudo usermod –ag docker $user
sudo service docker restart
인스턴스 재실행
```

3. 레포다운로드
```
git clone https://github.com/zeroistfilm/xpass.git
cd xpass
docker-compose up -d
```
