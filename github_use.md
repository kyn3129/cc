## CentOS git 설치

su  // root 권한으로 접속
```sh
yum install git // git을 이용하기 위하여 설치 
                //우분투 에서는 apt-get
```

----
##git 사용법
```sh
mkdir ~/workspace 

cd ~/workspace

git status 

git init 
  
git status 

git config --global user.name 유저이름 
 
git config --global user.email 이메일주소

git remote add origin https://github.com/내주소/내레파지토리.git 

git pull -u origin master     # 파일 다운로드 

vi 아무거나만듦

git add [생성한파일] 

git status 

git commit -m "메세지" 
 
git status  

git push -u origin master     # 파일 업데이트  #이거하면 내꺼 github에 업뎃됨
```

-----
origin url 설정이 잘못되서 origin을 삭제(수정)해야할 경우

```sh
git remote rm origin

git remote rename origin origin_re
```

----

## git push error

### url return error

```sh
git remote set-url origin git@github.com:kyn3129/레포지터리이름.git
```

### public key error 참고링크

http://uiandwe.tistory.com/992

----
