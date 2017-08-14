import pandas as pd
elements = []
state = ""
region = ""
editStr = "[edit]"
parens = " ("
with open('university_towns.txt','r') as input:
    for line in input:
        editpos = line.find(editStr)
        parenspos = line.find(parens)
        if editpos > 0:
            state = line[:editpos]
        else :
            if parenspos > 0 :
                region = line[:parenspos]
            else :
                region = line.strip()
            elements.append([state,region])

#df = pd.Dataframe