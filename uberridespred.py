


import numpy as np
import pandas as pd
import pickle



dataset=pd.read_csv('taxi.csv')
dataset.head()




dataset.isnull().sum()





X=dataset.iloc[:,0:4].values
y=dataset.iloc[:,4].values



from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)




from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_train,y_train)


print("Train score:",reg.score(X_train,y_train))
print("Test score:",reg.score(X_test,y_test))



pickle.dump(reg,open('taxi.pkl','wb'))





model=pickle.load(open('taxi.pkl','rb'))



pred=model.predict([[80,1770000,6000,85]])[0].round(2)
pred






