#1
#N=6
#msg = []

#for i in range(N):
#    msg.append(input('입력하세요: '))
#msg.reverse()
#print('정렬결과 : ', msg)
#print('가장 높은 문자열: ', msg[0]) #max(msg)
#print('가장 낮은 문자열: ', min(msg)) #msg[-1]

#2
#16진수(x들어감), 2진수 표현(b들어감) //8진수는o
#hex.()하면 되는데 10진수만 됨 
#가나다를 10진수로 바꿔주기
#print(hex(ord('가'))+hex(ord('나'))+hex(ord('다')))
#print(bin(ord('가'))+bin(ord('나'))+bin(ord('다')))
#가나다 입력하면 가,나,다로 인식시켜서 10진수로 변환해서 16진수,2진수로 변환
#data=input('입력하세요: ')
#data=list(data)
#print(data)
#for i in data:
#    print(hex(ord(i)),end='')
#print()
#for i in data:
#    print(bin(ord(i)),end='')



#3
data='123,42,98,18'
A=[]
for i in data:
    if i.isdigit():  #10진수냐 물어보는거 or isnumeric 숫자냐
#A.append(i) 숫자만 담아주기
#담아놓고 보면 문자로 담김
        A.append(int(i)) #숫자로 담김
print('A: ', A)
print('합: ',sum(A))
print('큰수: ',max(A)) 
print('작은수: ',min(A))


#4
num=40 #int(input())
for i in range(1,num+1):
    if i%10 in [2,4,8]:
        print('#',end='') #출력후에 단바꾸기 없음
    elif i%20 ==0:
        print(i)
    else: print(i,end='')

#5
month=0 #int(input())
data=['0','Jan','Feb','Mar','Apr','May','Jun','Jur','Aug','Sep','Oct','Nov','Dec'] #1~12 매칭하기 좋게
if month in [3,4,5]:
    print(data[month],'spring')
elif month in [6,7,8]:
    print(data[month],'summer')
elif month in [9,10,11]:
    print(data[month],'fall')
elif month in [12,1,2]:
    print(data[month], ', winter')
else: print("잘못된 데이터입니다")

#6


#8
#import re
#string =  'Happy New Year 2023!'
#numbers = re.sub(r'[^0-9]', '', string)
#list_a=list(set(numbers))
#print(list_a)
#isdigit 사용
string = input()
dd= ['0','1','2','3','4','5','6','7','8','9']
A=[]
for i in range(0,len(string)):
    if string[i] in dd :
        if int(string[i]) not in A:
            A.append(int(string[i]))
print(A)

#12
국어=[90,82,77,94,78]
수학=[89,71,100,82,99]
윤리=[98,80,92,93,91]
국사=[99,91,90,71,83]
print(f'[국어] 최고점수: {max(국어)} 최저점수: {min(국어)}')
print(f'[수학] 최고점수: {max(수학)} 최저점수: {min(수학)}')
print(f'[윤리] 최고점수: {max(윤리)} 최저점수: {min(윤리)}')
print(f'[국사] 최고점수: {max(국사)} 최저점수: {min(국사)}')