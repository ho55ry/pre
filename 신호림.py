#1
N=6
msg = []
for i in range(N):
   msg.append(input('입력하세요: '))
msg.reverse()
print('정렬결과 : ', msg)
print('가장 높은 문자열: ', msg[0]) #max(msg)
print('가장 낮은 문자열: ', min(msg)) #msg[-1]

#2
#16진수(x들어감), 2진수 표현(b들어감) //8진수는o
#hex.()하면 되는데 10진수만 됨 
#가나다를 10진수로 바꿔주기
#print(hex(ord('가'))+hex(ord('나'))+hex(ord('다')))
#print(bin(ord('가'))+bin(ord('나'))+bin(ord('다')))
#가나다 입력하면 가,나,다로 인식시켜서 10진수로 변환해서 16진수,2진수로 변환
data=input('입력하세요: ')
data=list(data)
print(data)
for i in data:
   print(hex(ord(i)),end='')
print()
for i in data:
   print(bin(ord(i)),end='')



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
num=int(input('게임 정수 입력: '))
for i in range(1,num+1):
    if i%10 in [2,4,8]:
        print('#',end='') #출력후에 단바꾸기 없음
    elif i%20 ==0:
        print(i)
    else: print(i,end='')

#5
month=int(input('좋아하는 월 입력: '))
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
def data(num,dan):
    print(format(num, ','),end='')
    print(dan)
data(12345678,'$')
data(907,'₩')


#7
num=int(input('약수 구하고 싶은 수 : '))
A=[]
for i in range(1,num+1):
    if num%i==0:
        A.append(i)
    else: pass
print(f'{num}의 약수: ',A)


# 8
string = input('메시지 입력: ')
dd= ['0','1','2','3','4','5','6','7','8','9']
A=[]
for i in range(0,len(string)):
    if string[i] in dd :
        if int(string[i]) not in A:
            A.append(int(string[i]))
print(A)

#10
num=int(input('팩토리얼 수 입력: '))
pre=num
answer=1
if num>0:
    while num:
        answer= answer*num
        num=num-1
    print(pre,'! =>',answer)
else:
    print('0! => 0')


#12
국어=[90,82,77,94,78]
수학=[89,71,100,82,99]
윤리=[98,80,92,93,91]
국사=[99,91,90,71,83]
print(f'[국어] 최고점수: {max(국어)} 최저점수: {min(국어)}')
print(f'[수학] 최고점수: {max(수학)} 최저점수: {min(수학)}')
print(f'[윤리] 최고점수: {max(윤리)} 최저점수: {min(윤리)}')
print(f'[국사] 최고점수: {max(국사)} 최저점수: {min(국사)}')



#테스트3
배트맨={90:'국어',89:'수학',98:'윤리',99:'국사'}
마징가={82:'국어',73:'수학',71:'윤리',91:'국사'}
피오나={78:'국어',99:'수학',91:'윤리',83:'국사'}
print('[배트맨] 최고 점수:',max(배트맨.keys()),배트맨.get(max(배트맨.keys())), ', 최저 점수:',min(배트맨.keys()),배트맨.get(min(배트맨.keys()))) 
print('[마징가] 최고 점수:',max(마징가.keys()),마징가.get(max(마징가.keys())), ', 최저 점수:',min(마징가.keys()),마징가.get(min(마징가.keys()))) 
print('[피오나] 최고 점수:',max(피오나.keys()),피오나.get(max(피오나.keys())), ', 최저 점수:',min(피오나.keys()),피오나.get(min(피오나.keys()))) 




