# 무작위로 뽑기 위해서 random 이라는걸 사용
# random은 그냥 사용할 수 없고 어딘가에서 불러와야 한다. -> import 사용

import random

# lunch라고 하는 변수에 점심메뉴 3가지를 담아보자.
# 점심메뉴 추천 받습니다.

lunch = ['김치찌개', '된장찌개', '제육볶음']

for i in lunch:
    print(i)

# lunch 전체 출력
# lunch 중에 3번째 요소 출력

print(lunch)
print(lunch[2])

# lunch가 가지고 있는 값 중 하나를 무작위로 골라서 menu라는 변수에 담는다

menu = random.choice(lunch)
print(menu)