# -*- coding: utf-8 -*-

# Dictionary 내부에 저장된 키 값은 중복을
# 허용하지 않습니다.
dict_1 = {'name':'python'}
print(f'dict_1["name"] -> {dict_1["name"]}')

# version 키 값으로 데이터를 추가
dict_1["version"] = 3.6
print(f'dict_1["version"] -> {dict_1["version"]}')

# 이미 존재하는 version 키 값으로 Dictionary에
# 데이터를 추가
# (이미 존재하는 version 키 값은 추가되지 않고
# 해당 키 값의 데이터를 수정합니다)
dict_1["version"] = 3.7
print(f'dict_1["version"] -> {dict_1["version"]}')






