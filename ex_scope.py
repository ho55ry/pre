#--------------------------------------------------
# 스코프(scope) : 변수가 존재 할 수 있는 범위
#--------------------------------------------------
# 변수 종류
# ┌ 전역 변수 (Global Variable) : 파일 전체에서 사용되는 변수. 같은 파일에 존재하는 함수, 클래스 등. 함께 사용
# └ 지역 변수 (Local Variable)  : 특정 영역 안에서만 사용 가능
# 전역 변수명과 지역 변수명이 동일한 경우
# 지역 변수(같은 영역안에 있는 변수)가 우선 순위
#--------------------------------------------------
year=2022
month=12

def showToday(day):
    #전역 변수 사용 알림해줘야됨
    global year      #global year 안쓰면
    year += 1        #지역 변수안에 year 없어서 오류 발생
    print(f'오늘은 {year}년 {month}월 {day}일 입니다.')

print(f'[Before]year=>{year}')

showToday(26)

print(f'[After]year=>{year}')
#print('day : ', day)  #day는 지역 변수라서 undefined





