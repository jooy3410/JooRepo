from urllib.parse import urlencode, quote_plus, unquote
from urllib.request import urlopen, Request
import requests
#xml을 json으로 변환하는 라이브러리
import xmltodict
import json

url = ''
#키값
key = ''
#키값뒤에 올 url
queryParams = '&' + urlencode({quote_plus('stdate'): '20210101', quote_plus('eddate'): '20211231'})
#get_data에 requests.결과값담기
get_date = requests.get(url + key + unquote(queryParams))
#제대로 불러졌는지 확인하기 위해 print(get_data)해줌
#결과값<Response [200]>
#200번은 성공을 뜻함
print(get_date)


request = Request(url + key + queryParams)
#요청하는 url이 get형식으로 되어었음
request.get_method = lambda: 'GET'

#response_body에 요청한 결과값 저장
response_body = urlopen(request).read()

#xml파일로 저장하는 코드
# f = open('test_1.xml', 'wb')
# f.write(response_body)

#json파일로 저장하는 코드
tojson = xmltodict.parse(response_body)
json_obj = json.dumps(tojson, ensure_ascii=False)
art_file = open('test_3.json', 'w+', encoding='utf8')
art_file.write(json_obj)
# f.close()


