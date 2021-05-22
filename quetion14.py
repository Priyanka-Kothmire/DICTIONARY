a={"bijender":45,"deepak":60,"param":20,"anjili":30,"roshini":50}
sorted_dict = dict( sorted(a.items(),
                           key=lambda item: item[1],
                           reverse=True))
                           
# print('Sorted Dictionary: ')
print(sorted_dict)



a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)



a={"bijender":45,"deepak":60,"param":20,"anjili":30,"roshini":50}

sorted_dict = dict( sorted(a.items(),
                           key=lambda item: item[1],
                           reverse=False))
                           
print('Sorted Dictionary: ')
print(sorted_dict)



# Dictionary of string and integers
word_freq = {
    '5' : 56,
    '4'    : 23,
    '3'  : 43,
    '3'   : 11,
    '1'  : 78,
}
# Iterate over a dictionary sorted by key in ascending order
for value in sorted(word_freq.items()):
    print(word_freq[value])









