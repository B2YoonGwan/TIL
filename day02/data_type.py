number = 3
print(type(number))

string = '문자열'
print(type(string))

boolean = True
print(type(boolean))

string_number = '58'
print(type(int(string_number)))

name='홍길동'
print(f'{name}입니다. 반갑습니다.')


"""
여러줄 주석입니다.
리스트
"""
# 리스트 선언
my_list = ['java', 'python']

# 리스트 원소 접근
print(my_list[0]) # 첫 번째 원소

# 리스트 원소 변경
# my_list의 첫 번째 요소를 'django'라는 문자열로 바꾸고 싶다.
my_list[0] = 'django'
print(my_list)

# 리스트 길이
print(len(my_list))

"""
딕셔너리
"""

# 딕셔너리 선언
my_info = {
    'name' : '윤관',
    'age' : 28
}
print(my_info)

# 딕셔너리 원소 접근
print(my_info['name'])
# 가지고 있지 않은 key로 접근하면 keyerror가 발생
# print(my_info['김구현'])
# 딕셔너리는 원소 접근 방법이 2가지가 있다.
# 딕셔너리가 가지고 있는 get함수
print(my_info.get('name'))
# 가지고 잇지 않은 key로 접근하면 None 반환 유연하지만 대괄호로 불러오는게 오류를 확인하기 쉬움.
print(my_info.get('location'))

# 딕셔너리 원소 변경
my_info['name'] = '홍길동'
print(my_info)

"""
딕셔너리 실습
"""
coin = {
    'BTC': {
        'opening_price': '44405000',
        'closing_price': '38806000',
        'min_price': '36640000',
        'max_price': '44999000',
        'prev_closing_price': '44404000',
        'fluctate_24H': '-7463000',
        'fluctate_rate_24H': '-16.13',
    },
    'ETH': {
        'opening_price': '1458000',
        'closing_price': '1229000',
        'min_price': '1100000',
        'max_price': '1490000',
        'prev_closing_price': '1458000',
        'fluctate_24H': '-275000',
        'fluctate_rate_24H': '-18.28',
    },
    'XRP': {
        'opening_price': '364.5',
        'closing_price': '311.9',
        'min_price': '284.2',
        'max_price': '372.7',
        'prev_closing_price': '364.2',
        'fluctate_24H': '-90.6',
        'fluctate_rate_24H': '-22.51',
    },
}

# 2-1. 코인의 정보에서 BTC의 최대 가격을 출력하시오.
print(coin['BTC']['max_price'])

# 2-2. BTC의 시가와(opening price) XRP의 시가를 더한 결과를 출력하시오.
a = coin['BTC']['opening_price']
b = coin['XRP']['opening_price']
print(int(a)+float(b))














