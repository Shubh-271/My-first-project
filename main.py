# python program for inventory management
from add import add
from display import display
from find import find
from modify import modify
from delete import delete
from dasplaying import dasplaying
from time import sleep
while True:
    print("🙏🏻🙏🏻SHREE RAM GENERAL STORE INVENTORY🙏🏻🙏🏻")
    print("*****************************************************")
    print("1:Add an inventory\n2:Delete an inventory\n3:Display the records\n4:Modify the records\n5:find the detail of particular product\n6:Exit python\n7:Exit the program\n8:display using panda\n9:want to sleep")
    c1=int(input("enter the number whose command you want to execute:"))
    if c1 in (1,2,3,4,5,8):
        print("**********************output*********************")
    if c1==7:
        text=("output cancelled")
        width=74
        cent=text.center(width)
        print("\n",cent)
        text2=("since you have quit the program")
        cent2=text2.center(width)
        print(cent2)
        break
    elif c1==1:
        add()
    elif c1==6:
        text=("output cancelled")
        width=74
        cent=text.center(width)
        print("\n",cent)
        text2=("since you have quit the interpreter")
        cent2=text2.center(width)
        print(cent2)
        quit()
    elif c1==3:
        display()
    elif c1==4:
        modify()
    elif c1==2:
        delete()
    elif c1==5:
        find()
    elif c1==8:
        dasplaying()
    elif c1==9:
        n=int(input("time in seconds:"))
        print("            you can have a power nap of",n,"seconds")
        sleep(n)
    else:
        print("-----------------------------------------ERROR----------------------------------------")
        print("you have not chose the correct option pick between 1 to 8 only")
    print("-----------------------------------------END----------------------------------------\n\n")




    
