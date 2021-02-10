import pandas as pd
from apyori import apriori
data = pd.read_excel("D:\\Syllabus\\Online Retail\\movies.xlsx")
observations = []
for i in range(len(data)):
 observations.append([str(data.values[i,j]) for j in range(13)])

associations = apriori(observations, min_length = 2, min_support = 0.2, min_confidence = 0.2, min_lift = 3)
associations = list(associations)
print(associations[0])