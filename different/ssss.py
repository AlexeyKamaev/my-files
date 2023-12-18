set1 = frozenset('beegeek')
set2 = set('stepik')

set3 = set1 & set2
l = list(set2)

while l != ['s','t','e','p','i','k']:
    set2 = set2 | set()
    l = list(set2)
    
else:
    print(set2)
    print(l)