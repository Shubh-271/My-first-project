def find():
    import os
    import csv
    try:
        f=open("inventory.csv","r")
        z=csv.reader(f)
        found=[]
        a=input("enter the product name of which you want the details:")
        next(z)
        for i in z:
            if a in i:
                found.extend(i)
                print('["name","selling price","cost price","in stock"]')
                print(found)
        if found==[]:
            text=("no such product is there")
            width=75
            cent=text.center(width)
            print("\n",cent,"\n")
        f.close()
    except:
        text=("Firstly add an Entry")
        width=75
        cent=text.center(width)
        print("\n",cent,"\n")




        
            

