# -*- coding: utf-8 -*-
"""
MNIST datasets demo for gcforest
"""
from keras.datasets import mnist
from xgboost import XGBClassifier

from gcForestClassifier import GCForestClassifier
from gcForestRegressor import GCForestRegressor

if __name__ == "__main__":
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train, X_test = X_train.reshape(X_train.shape[0], -1), X_test.reshape(X_test.shape[0], -1)
    
    gc = GCForestClassifier(shape_1X=784, window=782)
    gc.fit(X_train, y_train)
    y_gc = gc.predict(X_test)
    """
    pxg = XGBClassifier(n_estimators=10, learning_rate=0.1)
    gc.make_estimator(pxg, name='pxg', est_type='mgs')
    gc.make_estimator(pxg, name='cxg', est_type='cascade')
    gc.fit(X_train, y_train)
    """
    
    gr = GCForestRegressor(shape_1X=784, window=782, cv_method='sequence', scoring='explained_variance')
    gr.fit(X_train, y_train)
    y_gr = gr.predict(X_test)
    
    