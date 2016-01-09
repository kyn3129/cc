
## Homework for Internship: Sentience

###요구사항
1. (주변에 리눅스가 없는 경우?!) 본인 컴퓨터에 virtualbox 등으로 centos 대략 최신 버젼을 설치합니다.
2.(이미 설치되어 있지 않은 경우) Python, MySQL, Flask 를 설치합니다. (virtualenv를 활용하면 좋습니다)
3.사용자가 입력한 주식 종목 코드를 Flask 앱으로 입력받아, (ex : NASDAQ:EA)
4.해당 코드를 urllib 등으로 Google Finance (https://www.google.com/finance)에 전달하고
-Google Finance 가 인지하지 못하는 입력 값은 처리하지 않아도 좋습니다.
5.그 결과를 BeautifulSoup 등으로 파싱해서
6.현격(price), 가격변동(price change) 두 가지 값을 결과로 보여줍니다.
7.보여준 값을 임의의 MySQL Table 에 종목, 시간을 key로 잡아서 기록으로 남깁니다. (sql alchemy object 활용 보다는 RAW SQL 을 사용하면 더 좋습니다)
8.기록된 내용을 아주 간단하게 대강 볼 수 있는 Flask 앱을 만듭니다.
9.1) 각 과정을 어떻게 구현했는지 단계별로 간략한 설명과, 2) 최종적으로 만들어진 소스코드, 3) 동작화면 샘플/스샷을 자신의 blog / github 등에 기록해서 이메일 (hello.sentience@gmail.com) 로 제출합니다. (ex: blog / github인 경우 url 을 알려주시면 됩니다)

###기타사항
-과제는 원칙적으로는 채용공고 마감일 (1월 17일 24시) 전까지 제출하실 수 있으나, 조기 마감의 가능성이 있으므로 일부러 늦게 제출하시는 것은 권장하지 않습니다.
-공동 작업을 염두에 둔 소스 코드의 간략함 및 Readability 가 가장 중요하게 평가됩니다. 
-필요한 경우 원격 시연을 요청할 수 있으므로, 웹 서비스 포트를 잠깐 열거나, teamviewer 등을 잠시 설치하셔야 할 수 있습니다. 
-프로그래밍 초보이신 경우에도 의욕만 있으면 충분히 실현 가능한 난이도로 설정하였습니다.
-프로그래밍 경험자 분들에게는 크게 부담되지 않도록, 다운로드 등 시간을 제외한 순수한 작업 시간은 2~4시간 정도를 예상하여 작성 되었습니다.

###작업일지
가상머신 : VMware WorkStation 12.1
OS : CentOS7 - 64bit
