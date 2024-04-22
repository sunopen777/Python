'''singer_list=["뉴진스","트와이스"]
print(type(singer_list))
print(singer_list[0])
singer_list.append("아이유")
print(singer_list)
singer_list.insert(1,"르세라핌")
print(singer_list)
singer_list.insert(2,"싸이")
print(singer_list)
singer_list.insert(0,"심영")
print(singer_list)
print(singer_list[1:3])
sports=["야구","축구","농구"]
print("농구" in sports)
print("배구" in sports)
sports.remove("축구")
print(sports)
print(len(sports))
sports[0]="배드민턴"
print(sports)
'''
sports=["야구","축구","농구"]
sports.remove("축구")
sports.append("족구")
print(sports)
del sports[0]
print(sports)
sports.pop()
print(sports)
sports.append("족구")
sports.append("축구")
sports.append("배구")
print(sports)
sports.pop(1)
print(sports)
fruit=["strawberry","apple","banana"]
fruit.remove("apple")
print(fruit)
