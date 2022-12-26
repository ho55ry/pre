# ----------------------------------------------------------------------------------
# list, tuple => 저장 순서대로 파이썬에서 번호를 부여 (=index) 데이터 식별 위해서
# ----------------------------------------------------------------------------------
data='1 2 3 4 5'
#str => list
print(list(data))
print(data.split())
#split 거치고 나면 자동으로 list로 변환됨 (1개에서 여러개로 나뉘기 때문)
print(list(map(int,data.split())))

data2='1,2,3,4,5'
print(list(data))
print(data.split(','))
print(list(map(int,data.split())))

print(len(data)) # len : 요소의 수
print(len(data.split()))
print(len([]))
print(len([1,3,5]))

# ----------------------------------------------------------------------------------
# dict => {키1:값1, 키2:값2, 키3:값3}
#         index없음. key로 값 사용, key 중복 x (중복 사용 시 값이 변경됨. 오류나지는 않음)
# ----------------------------------------------------------------------------------

info={'name':'Shin',12:'Num',7:2023}

#key만 가져오고 싶다 => 메서드 keys()
keys=info.keys() # .keys() 위에 마우스 올려보면 method -> 어딘가에 포함되어 있음. 단독으로 못씀
print(keys)
# 출력시 dict_keys(['name', 12, 7]) 뜨긴 하는데 따로 리스트 만들어서 저장되는게 아니고 보여주기만 함 (메모리 문제)
for k in keys: print(k)

#value만 가져오고 싶다 => 메서드 values()
values=info.values()
print(values)
for v in values: print(v)

#key,value 다 가져오고 싶다 => 메서드 items()  => [(키,값),(키,값),(키,값)] 키,값 튜플로 묶어서 리스트 만들어 줌
all=info.items()
print(all)
for kv in all: print(kv)
for kv in all: print(kv[0],kv[1])   # all[0] = (kv[0],kv[1]) = ('name','Shin') 

# 언팩킹 => 묶음을 풀어서 가져오는 방법, 요소 갯수만큼 변수 필요
# tuple만 되는건 아니고 list도 가능
for a,b in all: print(a,b)

# dict 추가하기 => 키로 값 넣게
info['birth']='0507'
print(info)

# 존재하는 키 추가하면 값 변경됨
info[12]='Good'
print(info)