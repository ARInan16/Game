g=int(input('how many item you want to add\n'))
u=int(input('which comprehension  you want to do\n1 for list\n2 for set \n 3 for dict\n'))
it=str(input('input your items\n'))
list=it.split( )
if u==1:
    ls=[item for item in list]
    print(ls)
elif u==2:
    ur={item for item in list}
    print(ur)
elif u==3:
    dt={item:f"item {i}" for item in list}
else:
    print('sorry')