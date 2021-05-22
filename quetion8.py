dict={}
elements=int(input("enter the elements :"))

for i in range(elements):
    students=input("enter the name :")
    marks=int(input("enter the marks :"))
    dict.update({students:marks})
print(dict)


