from scipy import stats
import pandas as pd
import numpy as np
from itertools import chain
from unidecode import unidecode



def nopunct(word):

        punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''

        no_punct = ""
        for char in word:
            if char not in punctuations:
                no_punct = no_punct + char

        return no_punct





def percentile(stats1, year, name, boolean):
    #year = 1980
    df1 = pd.read_csv("Book2.csv")
    df1 = df1.drop('birth_year', axis=1)
    df1 = df1.fillna(0)
    df1["player"] = df1["player"].apply(nopunct)
    df1['player'] = df1['player'].str.lower()
    df1["player"] = df1["player"].apply(unidecode)
    name = nopunct(name)
    name = name.lower()
    name = unidecode(name)



    df = df1[df1.season == year]
    df = df.reset_index()


    playerDF = df[df.player == name]
    playerDF = playerDF.reset_index()
    position = playerDF.iloc[0]["pos"]

    if (position[:1] == "C"):
        position = "C"
    else:
        position = position[:2]

    if boolean == True:
        return position
    


    df = df[df.pos == position]
    df = df.reset_index()
    

    for key in stats1:
        current = stats1[key]
        header = df[df.columns[df.columns.str.contains(pat = key.lower())]] 
        array1 =  header.values.tolist()
        array1 = list(chain.from_iterable(array1))

      
        percent = stats.percentileofscore(list(array1), float(current))
        stats1[key] = percent

    return stats1

def fix2D(arr):
    x = 0
    arrNew = []
    while x < len(arr):
        str = arr[x][0]
        str = str[4:]
        str = str.replace("M", "")
        if str == "TO":
            str = "TOV"
        
        array = [str, arr[x][1]]

        arrNew.append(array)

        x+=1

    dictionary = dict(arrNew)
    return dictionary



def sorter(dictionary):
    myKeys = list(dictionary.keys())
    myKeys.sort()
    sortDict = {i: dictionary[i] for i in myKeys}
    return sortDict

        


def getMach(pos):
    if pos=="PG":
        pg = [('playFGA', -0.6150401765027368), ('play2PA', -0.587864365884284), ('playFTA', -0.43491558462527713), ('play3PA', -0.372335754008891), ('playTO', -0.2928814224610756), ('playPF', -0.21098437240768603), ('playBLK', 0.1607203258682319), ('play2PM', 0.16970767529741962), ('playSTL', 0.2307367083975762), ('playTRB', 0.3280044638238135), ('playFGM', 0.3860068254120804), ('play3PM', 0.3885696291049632), ('playAST', 0.4340716794242032), ('playFTM', 0.4986970041813066), ('playPTS', 0.5123155820884346)]
        return pg
    elif pos == "SG":
        sg = [('playFGA', -0.5394601807104613), ('play3PA', -0.4226450679851406), ('play2PA', -0.38847502768030084), ('playTO', -0.37851264541517937), ('playFTA', -0.3560830001350487), ('playPF', -0.19058922050186472), ('playSTL', 0.20076801251805312), ('play2PM', 0.21858355994425616), ('playBLK', 0.21884991319551686), ('playTRB', 0.22452380083770562), ('playAST', 0.3847809434667279), ('play3PM', 0.3867531084521919), ('playFGM', 0.389942298665165), ('playFTM', 0.43540004026663887), ('playPTS', 0.4440208814758081)]
        return sg   
    elif pos == "SF":
        sf = [('play2PA', -0.6949341852121492), ('playFGA', -0.5539534572415938), ('playFTA', -0.37271630971478287), ('play3PA', -0.32617368122717455), ('playTO', -0.292560060445031), ('playPF', -0.18966488922021896), ('playSTL', 0.2130443038796281), ('playBLK', 0.21956545401258257), ('play3PM', 0.252398868164148), ('play2PM', 0.29101695857098564), ('playTRB', 0.3296591587600502), ('playFGM', 0.37544977442064303), ('playAST', 0.4519355903475483), ('playFTM', 0.4692108137885785), ('playPTS', 0.48576316464987757)]
        return sf  
    elif pos == "PF":
        pf = [('playFGA', -0.481603346153922), ('play2PA', -0.4086075137909164), ('playFTA', -0.33928498367018256), ('play3PA', -0.2362922921301261), ('playTO', -0.22111994729848708), ('playPF', -0.1588337721367012), ('playSTL', 0.08743556501032963), ('playTRB', 0.2290695793540878), ('playBLK', 0.24163199883496972), ('play3PM', 0.2709024273789652), ('play2PM', 0.28199162905124636), ('playFGM', 0.3600807368975874), ('playFTM', 0.3696791716807797), ('playAST', 0.4294005020600464), ('playPTS', 0.4658518614032071)]
        return pf
    elif pos == "C":
        c = [('playFGA', -0.457832179033364), ('play3PA', -0.36380637111678527), ('play2PA', -0.32728140285931084), ('playTO', -0.2537699464438458), ('playPF', -0.06858812708365918), ('playFTA', 0.05099487092167494), ('playSTL', 0.07873503986931603), ('playFTM', 0.09525562326899843), ('play2PM', 0.23571383953609684), ('playTRB', 0.24661538427329757), ('play3PM', 0.28770826333841515), ('playPTS', 0.3187824588087106), ('playFGM', 0.32039212543291645), ('playBLK', 0.35344011274347376), ('playAST', 0.3791307874748197)]
        return c
    

def grader(perc, pos):
    
    x = 0
    posit = 0
    negat = 0
    machList = getMach(pos)
    machLearner = fix2D(machList)
    machLearner = sorter(machLearner)
    perc = sorter(perc)

    for key in perc:
        
        machNum = machLearner[key]
        percNum = perc[key]

        if machNum>0:
            posit+=percNum
            x += machNum*percNum
        else:
            negat+=(percNum*.25)
            x += machNum*percNum*.25



    x = x/(posit+negat)

    return x
     