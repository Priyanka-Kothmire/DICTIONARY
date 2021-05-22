from collections import Counter
my_dict = {
    "a":50, 
    "b":58, 
    "c":56,
    "d":40, 
    "e":100, 
    "f":20
    }
a=[]
k=Counter(my_dict)
# 3 highest value
high=k.most_common(3)
# print("Dictionary with 3 highest value :")
# print("keys:values")
for i in high:
    a.append(i[0])
    # print(i[0],":",i[1]," ")
print(a)
    # print(i[0])
