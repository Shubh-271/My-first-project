#f=open("inventory.csv","r")
def dasplaying():
    try:
        import pandas as pd
        df=pd.read_csv('inventory.csv')
        print(df)
    except:
        text=("Firstly add an Entry")
        width=75
        cent=text.center(width)
        print("\n",cent,"\n")
