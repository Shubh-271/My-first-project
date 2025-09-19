def delete():
    import os
    import csv
    try:
        r=open("inventory.csv","r")
        z=csv.reader(r)
        rows=[]
        rows1=[]
        a=input("enter the product name which you want to delete:")
        for i in z:
            rows.append(i)
            original_len=len(rows)
        for p in rows:
            if a in p:
                del rows[rows.index(p)]
                print("the details of ",a,"is deleted")
            elif a not in p:
                rows1.append(p)
        if original_len==len(rows1):
            text=("no such product is there")
            width=75
            cent=text.center(width)
            print("\n",cent,"\n")
        r.close()
        w=open("inventory.csv","w")
        y=csv.writer(w)
        y.writerows(rows)
        w.close()
    except:
        text=("Firstly add an Entry")
        width=75
        cent=text.center(width)
        print("\n",cent,"\n")

    





