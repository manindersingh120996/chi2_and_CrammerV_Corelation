import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import seaborn as sns
def cramerV(label,x):
    confusion_matrix = pd.crosstab(label, x)
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    r,k = confusion_matrix.shape
    phi2 = chi2/n
    phi2corr = max(0,phi2-((k-1)*(r-1))/(n-1))
    rcorr = r - ((r - 1) ** 2) / ( n - 1 )
    kcorr = k - ((k - 1) ** 2) / ( n - 1 )
    try:
        if min((kcorr - 1),(rcorr - 1)) == 0:
            warnings.warn(
            "Unable to calculate Cramer's V using bias correction. Consider not using bias correction",RuntimeWarning)
            v = 0
            print("If condition Met: ",v)
        else:
            v = np.sqrt(phi2corr / min((kcorr - 1), (rcorr - 1)))
            print("Else condition Met: ",v)
    except:
        print("inside error")
        v = 0
    return v

def plot_cramer(df,column_of_interest):
    temp = {}
    cramer = pd.DataFrame(index=[column_of_interest],columns=df.columns)
    columns = df.columns
    for j in range(0,len(columns)):
        v = cramerV(df[column_of_interest],df[columns[j]])
        cramer.loc[:,columns[j]] = v
        if (column_of_interest==columns[j]):
            pass
        else:
            temp[columns[j]] = v
    cramer.fillna(value=np.nan,inplace=True)
    plt.figure(figsize=(20,1))
    sns.heatmap(cramer,annot=True,fmt='.2f')
    plt.show()
    print(sorted(temp, key=temp.get, reverse=True)[:5])
    
plot_cramer(df,'Column_name')