# 네이버 기계번역 API 예제


# 네이버 기계번역 API 예제
import os
import sys
import urllib.request
import json
client_id = "NZIM1FAELxGTPVpOQnM8"
client_secret = "fN4rIqn3EM"
f = open('titleList.txt','r')
f2 = open('titleList_한글.txt','w')
lines = f.readlines()
for line in lines:
    encText = urllib.parse.quote(line.strip())
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/language/translate"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        jsonStr = json.loads(response_body.decode('utf-8'))
        print("영문명 :: ",line.strip())
        print(jsonStr['message']['result']['translatedText'])
        f2.write(jsonStr['message']['result']['translatedText']+'\n')
    else:
        print("Error Code:" + rescode)