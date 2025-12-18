n = list(map(int, input().split()))
dictionary = {'positives': 0, 'negatives': 0, 'zeros': 0}
for i in n:
    if i > 0:
        dictionary['positives'] += 1
    elif i < 0:
        dictionary['negatives'] += 1
    else:
        dictionary['zeros'] =+ 1
print(dictionary)