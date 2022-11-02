import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

veggie = pd.read_csv('./dataset.csv')
veggie = veggie.drop(['수집일'], axis=1)

veggie = veggie.replace("1,011", 1011)
veggie = veggie.replace("1,004", 1004)
veggie = veggie.replace("1,039", 1039)
veggie = veggie.replace("1,020", 1020)
veggie = veggie.replace("1,003", 1003)
veggie = veggie.replace("1,010", 1010)
veggie = veggie.replace("1,014", 1014)
veggie = veggie.replace("1,012", 1012)
veggie = veggie.replace("1,009", 1009)
veggie = veggie.replace("1,019", 1019)
veggie = veggie.replace("1,025", 1025)
veggie = veggie.replace("1,023", 1023)
veggie = veggie.replace("1,018", 1018)
veggie = veggie.replace("1,051", 1051)
veggie = veggie.replace("1,021", 1021)
veggie = veggie.replace("1,030", 1030)
veggie = veggie.replace("1,002", 1002)
veggie = veggie.replace("1,013", 1013)

veggie = veggie.fillna(0)

data = veggie[['외부 일사량', '내부온도', '내부습도', '내부CO2', '지습']].to_numpy()
target = veggie['품목명'].to_numpy()
train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)

from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_jobs=-1, random_state=42)

def random_forest