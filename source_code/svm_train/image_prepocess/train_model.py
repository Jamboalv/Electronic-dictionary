import numpy as np
from sklearn import svm   
import os
import numpy as np
import math
from sklearn.externals import joblib 

x = np.load("../data/array.npy")
y = np.load("../data/newLabel.npy")
y = y.reshape(y.shape[0],1)

data = np.hstack( (x,y) )
np.random.shuffle(data)
belta = 0.8

data_train = data[0:int(data.shape[0]*belta)]
data_test = data[int(data.shape[0]*belta):data.shape[0]*1]
x_train = data_train[:,0:data_train.shape[1]-2]
y_train = data_train[:,data_train.shape[1]-1]
y_train = y_train.reshape(y_train.shape[0])

x_test = data_test[:,0:data_test.shape[1]-2]
y_test = data_test[:,data_test.shape[1]-1]
y_test = y_test.reshape(y_test.shape[0])

clf = svm.SVC(kernel = 'rbf')
clf.fit(x_train,y_train)
joblib.dump(clf,'../model/rbfsvm.modle')

predict_y = clf.predict(x_test)
predict_y = np.array(predict_y)
y_test = np.array(y_test)
error = predict_y - y_test
print 'error: ',  100.0*error[error != 0].shape[0]/error.shape[0], '%'



