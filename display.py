def display():
    import os
    import csv
    try:
        z=open("inventory.csv","r")
        f=csv.reader(z)
        for i in f:
            if i!=[]:
                print(i)
        z.close()
    except:
        text=("Firstly add an Entry")
        width=75
        cent=text.center(width)
        print("\n",cent,"\n")
    




        
            

