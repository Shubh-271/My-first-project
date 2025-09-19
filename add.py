def add():
    import os
    import csv
    reading=[]
    z=open("inventory.csv","a+",newline="")
    f=csv.writer(z)
    read=open("inventory.csv","r")
    reader=csv.reader(read)
    for pk in reader:
        reading.append(pk)
    try:
        if len(reading)==0:
            f.writerow(["name","selling price","cost price","in stock"])
    except:
        print("file not found")
    a=int(input("enter the no. of inventory you want to add:"))
    for i in range(a):
        name=input("name of product:")
        sp=int(input("enter the selling price of the product:"))
        cp=int(input("enter the cost price of the product:"))
        stock=int(input("enter how many pieces of the product are available:"))
        data=[name,str(sp),str(cp),str(stock)]
        f.writerow(data)
        print(data)
    read.close()
    z.close()
    



        
            
