# -*- coding: utf-8 -*-

# Dictionary 타입의 변수 사용
# (다른 프로그래밍 언어의 MAP 타입)
# Dictionary의 변수는 Key:Value 형태의 
# 데이터를 저장합니다.
# Dictionary 내부에 저장된 Key 값은
# 중복이 허용되지 않습니다.(해싱)

# Dictionary 타입의 변수 선언
# { Key : Value }
dict_1 = {'name' : 'python', 'version' : 3.6}
print(dict_1)

# Dictionary 내부의 데이터를 참조하는 방법
# Dictionary변수명["키값"]
# (입력된 키값에 해당되는 데이터가 반환됨)
print(dict_1['name'])
print(dict_1['version'])

# Dictionary변수명.get("키값")
# (입력된 키값에 해당되는 데이터가 반환됨)
print(dict_1.get('name'))
print(dict_1.get('version'))

# Dictionary 변수에 데이터(Key:Value)를 
# 추가하는 방법
# Dictionary 타입의 변수는 리스트와 같이
# 다수개의 데이터를 저장할 수 있습니다.
# Dictionary변수명[newKey] = newValue
dict_1['level'] = 'high'
print(dict_1)








