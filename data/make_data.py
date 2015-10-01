#/usr/bin/python

#Make coordinate plane

import pandas
data_file = "data.tsv"
from cognitiveatlas.api import get_concept

# Retrieve concepts from the cognitive atlas
concepts = get_concept().pandas
concept_names = concepts["name"].tolist()
concept_definition = concepts["definition_text"].tolist()
concept_definition = [d.encode("utf-8") for d in concept_definition]
df=pandas.DataFrame(columns=["X","Y","concept","definition","id"])
nrows=30 #nrows and ncol for ~900 points
x=range(1,31)*30
y=[]
for i in range(1,31):
    y = y + [i]*30

len(y)==len(x)
df.X = x[0:810]
df.Y = y[0:810]
df.id = concepts["id"].tolist()
df.concept = concept_names
df.definition = concept_definition
df.to_csv("data.tsv",sep="\t",index=False)
