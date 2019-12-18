# -*- coding: utf-8 -*-

# http 프로토콜 기반의 통신을 지원하는 모듈
# - 세션의 개념을 적용하여 통신 프로그램을
# 작성할 수 있는 모듈
import requests

session = requests.Session()

# 다운받을 이미지 파일의 주소
url = 'https://previews.123rf.com/images/zoloterustra/zoloterustra1612/zoloterustra161200010/69658905-%EB%8F%84%EC%8B%9C%EC%9D%98-%EA%B2%A8%EC%9A%B8-%ED%92%8D%EA%B2%BD%EC%9E%85%EB%8B%88%EB%8B%A4-.jpg'

# 세션을 활용하여 URL에 해당되는 데이터를 수신
response = session.get(url)

with open('./download_file_01.jpg', 'wb') as f:
    # response의 content 멤버를 통해서
    # 웹 데이터의 정보를 추출할 수 있음
    # - 파일로 저장
    f.write(response.content)
    












