# Deep Forest in Python
Developed by Meng Wang, be based on much work of Pierre-Yves.

Author is researching on Finacial Machine Learning.

*Status* : under active development.

## What's New
version 0.1.0 : original version

* You can use GCForestClassifier or GCForestRegressor to solve the correspondence problem;
* You can input estimators which have scikit-learn API ( the classification should have .fit, .predict, .predict_proba, and the regression should have .fit, .predict ) with Function make_estimator. When it is used, the param is_customer will be True, and cross-validation in Multi Grain Scanning and each cascade layer.
* You can Adding/Training Layers by kings of scoring, even defining your scoring strategy from scikit-learn metric functions
* You can choose the method of cross-validation between 'group' and 'sequence', which can approach to problems either classification or regression.


## Presentation
**gcForest** is a deep forest algorithm suggested in Zhou and Feng 2017 ( [https://arxiv.org/abs/1702.08835](https://arxiv.org/abs/1702.08835) ). It uses a multi-grain scanning approach for data slicing and a cascade structure of multiple random forests layers (see paper for details).

The present **gcForest** implementation has been first developed as a Classifier and designed such that the multi-grain scanning module and the cascade structure can be used separately. 

Then the **gcForest** Regressor is developed basic on Classifier.  To be honest, the Regressor needs continuous improvement.

You can find the official release of the code used in Zhou and Feng 2017 [here](https://github.com/kingfengji/gcforest)，
and the popular version developed by Pierre-Yves [here](https://github.com/pylablanche/gcForest),


## Prerequisites

The present code has been developed under python3.x. You will need to have the following installed on your computer to make it work :

* Python 3.x
* Numpy >= 1.12.0
* Scikit-learn >= 0.20.0
* jupyter >= 1.0.0 (only useful to run the tuto notebook)

You can install all of them using `pip` install :

```sh
$ pip3 install -r requirements.txt
```

## Using gcForest

The syntax uses the scikit learn style with a `.fit()` function to train the algorithm and a `.predict()` function to predict new values class. You can find two examples in the examples.py.


## Saving and Loading Models

Using `sklearn.externals.joblib` you can easily save your model to disk and load it later. Just proceed as follow :<br>
To save :
```python
from sklearn.externals import joblib
joblib.dump(gcf, 'name_of_file.sav')
```
To load :
```python
joblib.load('name_of_file.sav')
```

## Notes
Thanks for Pierre-Yves Lablanche's work, I could complete the code in several days.

Even though I have tested it on several cases, I cannot still certify that it is a 100% bug free obviously.

**Feel free to test it and send me your feedback about any improvement and/or modification! Thanks so much**

### Known Issues

**Memory comsuption when slicing data**
There is now a short naive calculation illustrating the issue in the notebook.
So far the input data slicing is done all in a single step to train the Random Forest for the Multi-Grain Scanning. The problem is that it might requires a lot of memory depending on the size of the data set and the number of slices asked resulting in memory crashes.<br>
*The memory consumption when slicing data is more complicated than it seems. A StackOverflow related post can be found [here](https://stackoverflow.com/questions/43822413/numpy-minimum-memory-usage-when-slicing-images).
The main problem is the non-contiguous aspect of the sliced array with the original data forcing a copy to be made in memory.*

**OOB score error**
During the Random Forests training the Out-Of-Bag (OOB) technique is used for the prediction probabilities. It was found that this technique can sometimes raises an error when one or several samples is/are used for all trees training.<br>
*A potential solution consists in using cross validation instead of OOB score although it slows down the training. Now you can set is_customer=True, and cv estimator will be used.*


## License
This project is Open Source
