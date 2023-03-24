from scipy import stats
import pandas as pd

df = pd.read_csv("perc.csv")


def percentile(stats1):

    for key in stats1:
        current = stats1[key]
        array =  list(df[key])
        percent = stats.percentileofscore(array, current)
        stats1[key] = percent

    return stats1
