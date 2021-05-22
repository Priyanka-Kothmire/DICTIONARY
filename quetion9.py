# list="MISSISSIPPI"
# dict={} 
# b=[]
# i=0
# while i<len(list):
#         j=0
#         count=0
#         k=[]
#         while j<len(list):
#                 if list[i]==list[j]:
#                         count=count+1
#                 j=j+1
#         k.append(list[i])
#         k.append(count)
#         if k not in b:
#             b.append(k)
#         i=i+1
#         dict.update(b)
# print(dict) 



j="MISSISSIPPII"
i=0
a=b=c=d=0
e={}
while i<len(j):
    if j[i]=="M":
        a=a+1
    if j[i]=="I":
        b=b+1
    if j[i]=="S":
        c=c+1
    if j[i]=="p":
        d=d+1
    i=i+1
l=("M:",a,"I:",b,"S:",c,"P:",d)
print(l)



