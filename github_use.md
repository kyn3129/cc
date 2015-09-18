## CentOS git 설치
-
+```sh
su  // root 권한으로 접속

yum install git // git을 이용하기 위하여 설치 
                //우분투 에서는 apt-get
+```
mkdir ~/workspace 

cd ~/workspace

git status 

git init 
  
git status 

git config --global user.name [유저이름] 
 
git config --global user.email [이메일주소] 

git remote add origin https://github.com/kowonsik/raspberry.git 

git pull -u origin master     # 파일 다운로드 
40 43   
41 44  git add [생성한파일] 
42 45   
43 46  git status 
44 47   
45 48  git commit -m "메세지" 
 
