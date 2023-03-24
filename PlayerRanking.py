from scipy import stats
import pandas as pd
import numpy as np
from itertools import chain



def nopunct(word):

        punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''

        no_punct = ""
        for char in word:
            if char not in punctuations:
                no_punct = no_punct + char

        return no_punct





def percentile(stats1, year, name):
    #year = 1980
    df1 = pd.read_csv("Book2.csv")
    df1 = df1.drop('birth_year', axis=1)
    df1 = df1.fillna(0)
    df1["player"] = df1["player"].apply(nopunct)
    df1['player'] = df1['player'].str.lower()
    name = nopunct(name)
    name = name.lower()

    df = df1[df1.season == year]
    df = df.reset_index()
    la = df[df.tm == "LAL"]
    print(la)

    playerDF = df[df.player == name]
    playerDF = playerDF.reset_index()
    position = playerDF.iloc[0]["pos"]

    df = df[df.pos == position]
    df = df.reset_index()
    

    for key in stats1:
        current = stats1[key]
        header = df[df.columns[df.columns.str.contains(pat = key.lower())]] 
        print(header)
        array1 =  header.values.tolist()
        array1 = list(chain.from_iterable(array1))
        print(array1)

      
        percent = stats.percentileofscore(list(array1), float(current))
        stats1[key] = percent

    return stats1