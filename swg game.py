import random
name =str(input('enter ur name:\n'))
dsr=0
cscr=0
hscr=0
snake=1
water=2
gun=3
li=[snake,water,gun]
i=0
while i<5:
    human=int(input('press 1 for snake\n2 for water\n3for gun:\n'))
    com=random.choice(li)
    i+=1
    if human==1 and com==1:
        print('draw')
        dsr+=1
    elif human==1 and com==2:
        print('you won')
        hscr+=1
    elif human==1 and com==3:
        print('lose')
        cscr+=1
    elif human==2 and com==1:
        print('lose')
        cscr+=1
    elif human==2 and com==2:
        print('draw')
        dsr+=1
    elif human==2 and com==3:
        print('win')
        hscr+=1
    elif human==3 and com==1:
        print('won')
        hscr+=1
    elif human==3 and com==2:
        print('lose')
        cscr+=1
    else:
        print('draw')
        dsr+=1

print(f"score of computer is {cscr}")
print(f"score of {name} is  {hscr}")
print(f"number of same choice is {dsr}")
if cscr>hscr:
    print(f"the result of match is {name} lose")
elif hscr>cscr:
    print(f"the result of match is {name} won")
else:
    print('the result of the match is draw')