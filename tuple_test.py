print("아")
'''
my_tuple=("사과","메론","포도","토마토","사과") #변경하면 안되는 값을 튜플변수로 지정
#my_tuple.append("수박") #튜플변수 = 값 추가 불가
#my_tuple.remove("사과") #튜플변수 = 값 삭제 불가
print(my_tuple[0])
print(len(my_tuple)) #len = 변수의 길이를 알려줌
print("포도" in my_tuple) #my_tuple 변수 안에 "포도"가 있니?
print("샤인머스켓" in my_tuple) #my_tuple 변수 안에 "샤인머스켓"이 있니?
print("샤인머스켓" not in my_tuple) #my_tuple 변수 안에 "샤인머스켓"이 없니?
'''
my_tuple=("사과","메론","포도") #패킹
(f1,f2,f3)=my_tuple #언패킹
print(f1)
number=(1,2,3,4,5,6,7,8,9,10) #패킹
'''(n1,n2,*others)=number
print(n1)
print(n2)
print(others)
'''
(*others,n9,n10)=number
print(others)
print(n9)
print(n10)