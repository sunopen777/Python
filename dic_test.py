person={
    "이름":"나잖아",
    "나이":19,
    "키":170,
    "집주소":"달나라 달토끼동"}
print(person["이름"])
print(person)
person["몸무게"]=60
person["키"]=180
print(person)
del person["나이"]
print(person)
print (person.get("집주소"))
print("이름"in person)
print("나잖아" in person.values())
