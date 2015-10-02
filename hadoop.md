    2. 계정 추가

```sh

    # SSH 설치 및 공개 키 설정 
    #   Hadoop클러스터에서 Master와 Slave들 간에 통신은 SSH를 이용함
    #   모든 컴퓨터에는  SSH가 설치되어 있어야 함
    #   Master에서 암호없이 Slave에 접속하기 위해서 공개 키가 필요함

    useradd hadoop //유저 추가
    su - hadoop    //hadoop으로 접속
    ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa
    cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys  // cat 에서 '>>'가 있으면 A >> B B로 A 내용 복사
    chmod 0600 ~/.ssh/authorized_keys  //권한 부여
```

    3. 로컬호스트 들어갔다 나오기

```sh
    ssh localhost
    exit
```

    4. 하둡다운로드
    
```sh
    su
    cd /home
    mkdir hadoop //hadoop 폴더 생성
    cd hadoop
    wget http://apache.tt.co.kr/hadoop/common/hadoop-2.7.1/hadoop-2.7.1.tar.gz 
    tar -zxvf hadoop-2.7.1.tar.gz
```

    5. 컨피규어링

```sh
    vi $HOME/.bashrc
    
    # 아래 11개 export 만 추가해주면 됨
    export JAVA_HOME=/usr/java/jdk1.8
    export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar
    export HADOOP_HOME=/home/hadoop/hadoop-2.7.1
    export HADOOP_INSTALL=$HADOOP_HOME
    export HADOOP_MAPRED_HOME=$HADOOP_HOME
    export HADOOP_COMMON_HOME=$HADOOP_HOME
    export HADOOP_HDFS_HOME=$HADOOP_HOME
    export HADOOP_YARN_HOME=$HADOOP_HOME
    export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
    export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
    export JAVA_LIBRARY_PATH=$HADOOP_HOME/lib/native:$JAVA_LIBRARY_PATH

    # 실행
    source $HOME/.bashrc
```

    6. 설정값 추가하기

![connection](https://github.com/kowonsik/CCL/blob/master/lecture/hadoop.png)
![connection](https://github.com/kowonsik/CCL/blob/master/lecture/name_data_node.png)


```sh
    # (하둡을 구동하는 스크립트에서 사용되는 환경 변수)
    vi $HADOOP_HOME/etc/hadoop/hadoop-env.sh 
    export JAVA_HOME=/usr/java/jdk1.8
```

------------------------------------------

```sh
    # Hadoop 설치 후 로그파일, 네트워크 튜닝, I/O튜닝, 파일 시스템 튜닝, 압축 등과 같이 기본적인 하부 시스템 설정
    # 맵리듀스에서도 공통으로 사용
    
    vi $HADOOP_HOME/etc/hadoop/core-site.xml
    
    <configuration> 
        <property>
            <name>fs.default.name</name>
            <value>hdfs://localhost:9000</value>
        </property>
    </configuration> 
```

-------------------------------------------------

```sh
    # (네임노드, 보조 네임노드, 데이터노드 등과 같은 HDFS 데몬을 위한 환경 설정 구성)
    vi $HADOOP_HOME/etc/hadoop/hdfs-site.xml
    
    <configuration> 
        <property>
            <name>dfs.replication</name>
            <value>1</value>
        </property>
 
        <property>
            <name>dfs.name.dir</name>
            <value>file:///home/hadoop/hadoopdata/hdfs/namenode</value>
        </property>
 
        <property>
            <name>dfs.data.dir</name>
            <value>file:///home/hadoop/hadoopdata/hdfs/datanode</value>
        </property>
    </configuration>         
```

-------------------------------------------------

```sh
    # 실행
    cp $HADOOP_HOME/etc/hadoop/mapred-site.xml.template $HADOOP_HOME/etc/hadoop/mapred-site.xml
    
```
-------------------------------------------------

```sh
    # (잡트래커와 테스크트래커와 같은 맵리듀스 데몬을 위한 환경 설정 구성)
    vi  $HADOOP_HOME/etc/hadoop/mapred-site.xml
    
    <configuration> 
        <property>
            <name>mapreduce.framework.name</name>
            <value>yarn</value>
        </property>
    </configuration> 
```

-------------------------------------------------

```sh
    vi $HADOOP_HOME/etc/hadoop/yarn-site.xml

    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
```

-------------------------------------------------

```sh
    # 실행
    set JAVA_HOME
```


    7. 하둡시작
    
```sh
    hdfs namenode -format
    start-dfs.sh
    start-yarn.sh
```
    8. Web GUI 확인

```sh    
    # 웹브라우저(firefox)를 열고 테스트
    localhost:50070  # NameNode 정보 확인
    localhost:50090  # Secondary NameNode 정보 확인
    localhost:8088   # 클러스터와 모든 어플리케이션 정보 확인
```
    9. word counting example

```sh
    # 테스트 문서 제작
    vim test.txt
    
    # 아래 두줄을 test.txt 에 넣어주면 됨
    # 테스트용 문서를 옮겨놓고 사용해도 됨)
    i am a boy
    you are a girl
    
    hdfs dfs -mkdir /user   # user 디렉토리를 만듬 # exist directory 인 경우는 패스하면 됨
    hdfs dfs -mkdir /user/hadoop   # hadoop 디렉토리를 만듬 # exist directory 인 경우는 패스하면 됨
    hdfs dfs -mkdir /user/hadoop/input   # input 디렉토리를 만듬
    hdfs dfs -put test.txt /user/hadoop/input   # test.txt 파일을 input 디렉토리에 넣음
    
    # Word Count java 코드 작성( github 에서 WordCount.java 파일 다운로드)
    wget https://raw.githubusercontent.com/kowonsik/CCL/master/WordCount.java
    
    # WordCount.java compile
    hadoop com.sun.tools.javac.Main WordCount.java
    
    # jar 파일 만들기
    jar -cf wc.jar WordCount*.class
    
    # Word Count 실행
    hadoop jar wc.jar WordCount /user/hadoop/input /output
    
    # 결과 확인
    hdfs dfs -cat /output/part-r-00000
    
    # 기본 파일 명령어
    hadoop fs -ls /   # 모든 디렉토리 확인
    hadoop fs -ls /output   # output 디렉토리 확인 
    hadoop fs -rmr /output   # output 디렉토리 삭제
    
```
