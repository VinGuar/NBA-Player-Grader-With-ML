from scipy import stats
import pandas as pd




def percentile(stats1, year):

    df = pd.read_csv("Book2.csv")
    df = df.drop('birth_year', axis=1)
    df = df.dropna()

    df = df[df.season == year]

    for key in stats1:
        current = stats1[key]
        array =  list(df[key.lower()])
        percent = stats.percentileofscore(array, current)
        stats1[key] = percent

    return stats1
