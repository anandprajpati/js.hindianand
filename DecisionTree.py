import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import graphviz
print(pd.read_excel("C:/Users/Sumeet Maurya/Documents/PlayTennis.csv.xlsx"))
playtennis=pd.read_excel("C:/Users/Sumeet Maurya/Documents/PlayTennis.csv.xlsx")
Le=LabelEncoder()
playtennis['outlook']=Le.fit_transform(playtennis['outlook'])
playtennis['temp']=Le.fit_transform(playtennis['temp'])
playtennis['humidity']=Le.fit_transform(playtennis['humidity'])
playtennis['windy']=Le.fit_transform(playtennis['windy'])
playtennis['play']=Le.fit_transform(playtennis['play'])
print(playtennis)
y=playtennis['play']
x=playtennis.drop(['play'],axis=1)
clf=tree.DecisionTreeClassifier(criterion='entropy')
clf=clf.fit(x,y)
tree.plot_tree(clf)
dot_data=tree.export_graphviz(clf,out_file=None)
graph=graphviz.Source(dot_data)
print(graph)
x_pred=clf.predict(x)
print(x_pred)
print(x_pred==y)
'''import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import graphviz
import matplotlib.pyplot as plt
print(pd.read_excel("C:/Users/Sumeet Maurya/Documents/PlayTennis.csv.xlsx"))

playtennis = pd.read_excel("C:/Users/Sumeet Maurya/Documents/PlayTennis.csv.xlsx")

Le = LabelEncoder()
for column in ['outlook', 'temp', 'humidity', 'windy', 'play']:
    playtennis[column] = Le.fit_transform(playtennis[column])
print(playtennis)
y = playtennis['play']
x = playtennis.drop(['play'], axis=1)
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(x, y)
plt.figure(figsize=(12, 8))
tree.plot_tree(clf, feature_names=x.columns, class_names=['No', 'Yes'], filled=True)
plt.show()
dot_data = tree.export_graphviz(clf, out_file=None,
                                 feature_names=x.columns,
                                 class_names=['No', 'Yes'],
                                 filled=True, rounded=True,
                                 special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("playtennis_tree") 
graph.view()

x_pred = clf.predict(x)
print("All predictions correct?:", np.array_equal(x_pred, y_pre))'''

