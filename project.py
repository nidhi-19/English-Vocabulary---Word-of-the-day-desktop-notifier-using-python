import time
import random
import pandas as pd
from plyer import notification
# Code to read excel and convert to dictionary
df = pd.read_excel("wordlist.xlsx", index_col=0)
df = df.where(pd.notnull(df), None)

l = df.to_dict()["Meaning"]
keylist = list(l.keys())
vallist = list(l.values())
c = len(keylist)
#Code to generate random No
randNo = random.randint(0,c)
a= keylist[randNo]
b= vallist[randNo]

# Code to pop notification
if __name__ == "__main__":
    
    notification.notify(
        title =f" WORD OF THE DAY IS {str(a)}",
        message = f" Meaning: {str(b)} ",
        app_icon = "D:\wod.ico",
        timeout=10
        )
        