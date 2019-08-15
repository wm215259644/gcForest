#!usr/bin/env python
"""
Version : 0.1.0
Date : 8th August 2019
Author : Meng Wang
Email : wm215259644@163.com
Affiliation : Personal Development

Description :
Python3 implementation of the gcForest algorithm preesented in Zhou and Feng 2017
(paper can be found here : https://arxiv.org/abs/1702.08835 ).
It uses the typical scikit-learn syntax  with a .fit() function for training
and a .predict() function for predictions.
"""
from .gcForestClassifier import GCForestClassifier
from .gcForestRegressor import GCForestRegressor


__author__ = "Meng Wang"
__email__ = "wm215259644@163.com"
__version__ = "0.1.0"
