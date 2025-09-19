def modify():
    import os
    import csv
    try:
        r=open("inventory.csv","r")
        z=csv.reader(r)
        next(z)
        rows=[]
        a=input("enter the product name of which you want the change the details of:")
        for i in z:
            rows.append(i)
        for p in rows:
            if a in p:
                newname=input("Enter the new name:")
                newsp=input("Enter the new selling price:")
                newcp=input("Enter the new cost price:")
                newstock=input("Enter the no. of product available:")
                rows[rows.index(p)]=[newname,newsp,newcp,newstock]
        if rows==[]:
            text=("No Such Product Is There")
            width=75
            cent=text.center(width)
            print("\n",cent,"\n")
            r.close()
    except:
        text=("Firstly add an Entry")
        width=75
        cent=text.center(width)
        print("\n",cent,"\n")
    else:
        w=open("inventory.csv","w")
        y=csv.writer(w)
        y.writerows(rows)
        w.close()
    finally:
        print()

    





