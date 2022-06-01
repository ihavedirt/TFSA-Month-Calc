space = 21000
input = 800
total = 0
months = 0

while space > total:
    months += 1
    if months % 12 == 0:
        space += 6000
    total += input
    
    print('months: ' + str(months))
    print('total: ' + str(total))
    print('space: ' + str(space))
    print()
    
print('years: ' + str(months/12))