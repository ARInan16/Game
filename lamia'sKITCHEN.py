ls=['roti','sabji','mangso']
n=str(input('what you want to search\n'))
for item in ls :
    if item==n:
        print(n,'is available')
        break
else:
    print('your item is not available')