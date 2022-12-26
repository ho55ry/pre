# ---------------------------------------------------
# 람다 함수(lambda function) : 익명 함수 , 1줄 함수, 짧은 코드
# 문법 형식 : lambda 인자 : 실행코드
# ex) lambda x,y:x+y
# ---------------------------------------------------
# 입력 받은 숫자 모두 더해서 합계 출력하는 코드 
nums=input('원하는 수 만큼 숫자 입력 : (예시: 1 3 5 6 ...)') #str로 들어옴 '1 3 5 6 ...'
nums=nums.split() # '1 3 5 6 ...' => ['1','3','5','6', ...] 여전히 str
# [1,3,5,6, ...] 로 담고 싶음

#방법1 for문
#nums[0]=int(nums[0])
for idx in range(0,len(nums)):
    nums[idx]=int(nums[idx])
print('1 => ',nums)

#방법2 리스트 컴프리헨션
nums2=[int(n) for n in nums]
print('2 => ',nums2)

#방법3 내장함수 map(함수명,반복가능객체) => 반환값 : map 객체
nums3=list(map(str,nums)) #숫자만들거면 int
print('3 => ',nums3)

#추가 값*3을 결과로 반환하는 함수
def triple(num): return num*3

nums4=list(map(triple,nums))
print('4 => ',nums4)

# 자주 쓰는것도 아닌데 함수 만들기 싫다
nums5=list(map(lambda n:n*3,nums)) # n:n*3 에서 n은 인자 , n*3이 실행코드
print('5 => ',nums5)

