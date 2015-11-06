 #!/usr/bin/python

import sys
import urllib2
import time
import requests
import json
from datetime import datetime, timedelta


while 1 :
        t = time.localtime()
        tsec = t.tm_sec

        if tsec%20!=0 :
                print tsec
                time.sleep(0.2)

        else :
                url = "http://127.0.0.1:4242/api/put"
                data =  {
                "metric": "foo.bar",
                "timestamp": time.time(),
                "value": time.time(),
                "tags":
                {
                "host": "mypc"
                }
                        }
                ret = requests.post(url, data=json.dumps(data))
                print "ok"
