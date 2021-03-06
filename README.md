<p align="center"><img src ="https://github.com/yennanliu/analysis/blob/master/doc/wire.jpg" width="800" height="400"></p>

<h1 align="center">ANALYSIS</h1>

<p align="center">
<!--- travis -->
<a href="https://travis-ci.org/yennanliu/analysis"><img src="https://travis-ci.org/yennanliu/analysis.svg?branch=master"></a>
<!--- PR -->
<a href="https://github.com/yennanliu/analysis/pulls"><img src="https://img.shields.io/badge/PRs-welcome-6574cd.svg"></a>
<!--- notebooks Rmotr -->
<a href="https://notebooks.rmotr.com/yennanliu/analysis-63895a56"><img src="https://img.shields.io/badge/launch-Rmotr-cd201f.svg"></a>
<!--- notebooks mybinder -->
<a href="https://mybinder.org/v2/gh/yennanliu/analysis/master"><img src="https://img.shields.io/badge/launch-Jupyter-5eba00.svg"></a>
<!--- notebooks google colab -->
<a href="https://colab.research.google.com/github/yennanliu/analysis/blob/master/ML_/ML_Basic_L1_L2_Regularization.ipynb"><img src="https://img.shields.io/badge/launch-Google%20Colab-45aaf2.svg"></a>
</p>

> As `DS application demo` part of the "Daas (Data as a service) repo", this repo using jupyter notebook (mainly) as media showing step-by-step analysis and ML/DL approaches on various data science subjects. The idea is : demo how does a data scientist deal with a new dataset, pre-process the data, do exploration analysis (EDA), then running suitable model and offering suggestions with business feasibility and acceptable statistical errors. (i.e. DS workflow : business understanding -> data preprocess -> EDA -> data understanding -> analysis/modeling ). Main focus of this project: 1) Statistics/ML analysis 2) ML theory/algorithms explanation 3) Spark op/ML demo

* Daas (Data as a service) repo :  [Data infra build](https://github.com/yennanliu/data_infra_repo) -> [ETL build](https://github.com/yennanliu/XJob) -> [DS application demo](https://github.com/yennanliu/analysis)
* Airflow Heroku demo : [airflow-heroku-dev](https://github.com/yennanliu/airflow-heroku-dev)
* Mlflow Heroku demo : [mlflow-heroku-dev](https://github.com/yennanliu/mlflow-heroku-dev)

## Quick Start 
[Quick_start.md](https://github.com/yennanliu/analysis/blob/master/doc/quick_start.md)<br>

## File Structure 
```
├── DE_course       : Code for Udacity data engineer course 
├── DL_             : Deep learning relative projects  
├── DS_algorithms   : Build Data science model from scratch 
├── GPU             : GPU relative code 
├── ML_             : Machine learning relative projects  
├── README.md
├── R_              : R programming language relative projects 
├── SPARK_          : Pyspark basics/op/ML/ETL notebook demo projects
├── Statistics_     : Statistics relative projects 
├── archived        : Archived code/projects 
├── doc             : Doc for quick start, theory paper, pic.. and so on
├── ml_demo.py 
├── notebook        : Jupyter notebook relative projects (nb server/magic..)
├── project         : Archived projects 
├── pytorch_        : Pytorch relative projects 
├── tensorflow_     : Tensorflow relative projects
└── utility         : Utility scripts for ML/DL model tuning, DS plots...

```
## Main Projects 

[Machine Learning](https://github.com/yennanliu/analysis/tree/master/ML_)<br>

* [Gradian Decent](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/ML_/ML_Basic_Gradian_Decent.ipynb) - Main model optimization algorithms demo
* [Linear Regression](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/ML_/ML_Basic_LinearRegression.ipynb) - Simplest regression model 
* [Logistics Regression](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/ML_/ML_Basic_LogisticsRegression.ipynb) - Simplest classification model 
* [Support vector machine](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/ML_/ML_Basic_SVM.ipynb) -
* [Decision Tree](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/ML_/ML_Basic_Decision_Tree.ipynb) - Simple non-linear regression/classification model 
* [L1 L2 Regularization](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/ML_/ML_Basic_L1_L2_Regularization.ipynb) - Basic model tuning method


[Tensorflow Demo](https://github.com/yennanliu/analysis/tree/master/tensorflow_)<br>

* [TF Linear Regression](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/tensorflow_/TF_demo_LinearRegression_model.ipynb) - TF Linear Regression demo
* [TF Random Forest](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/tensorflow_/TF_demo_RandomForest_model.ipynb) - TF Random Forest Classification demo


[Statistics](https://github.com/yennanliu/analysis/tree/master/Statistics_)<br>

* [Confidence Intervals](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/Statistics_/Confidence_Intervals.ipynb) - Go through the confidence interval calculation from distributions 
* [AB TEST Part 1 ](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/Statistics_/AB_Testing_part1.ipynb) -  Hypothesis Test | P-value | T-test
* [AB TEST Part 2 ](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/Statistics_/AB_Testing_part2.ipynb) -  Bootstrapping
* [TIME SERIES Part 1 ](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/Statistics_/Time_Series_part1.ipynb) -  Stationary


[Spark](https://github.com/yennanliu/analysis/tree/master/SPARK_)<br>

*spark op intro* <br>
* [Pyspark Basic 1](http://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/SPARK_/Spark_notebook_basic_1.ipynb) - Basic spark ops (transform & action): RDD,Map,FlatMap, Reduce,filter, Distinct, Intersection
* [Pyspark Basic 2](http://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/SPARK_/Spark_notebook_basic_2.ipynb) -Basic spark ops : load csv,dataframe,SparkSQL, transformation in [RDD, dataframe, SparkSQL]
* [Pyspark Basic 3](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/SPARK_/Spark_DataFrame_OP_Intro.ipynb) -Basic spark ops : Spark DataFrame OP 

*spark ML intro* <br>
* [Pyspark LinearRegression nb step by step demo](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/SPARK_/Spark_ML_LinearRegression_Intro.ipynb) - Spark Linear Regression model tutorial 
* [Pyspark LogisticRegression nb step by step demo](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/SPARK_/Spark_ML_LogisticRegression_intro.ipynb) - Spark Logistic Regression model tutorial 
* [Pyspark Pipeline/Index/Encode nb step by step demo](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/ae94d7b2bccd3b94ee9001c4e44c7a0797b8d095/SPARK_/Spark_ML_Pipeline_Stringindexer_OneHotEncoder_Intro.ipynb) - Train a spark ML model via pipeline and preprocess (index/encoder)
* [Pyspark Tree models step by step demo](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/SPARK_/Spark_ML_DecisionTree_RandomForests_Intro.ipynb) - Train spark ML tree models (Decision tree/Random Forest/Gradient boosting)
* [Pyspark Kmeans models step by step demo](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/SPARK_/Spark_ML_Kmeans_Intro.ipynb) - Train spark ML cluster kmeans models 
* [Pyspark LinearRegression demo ](https://github.com/yennanliu/analysis/blob/master/SPARK_/Spark_ML_LinearRegression_demo.py) -  Train a linear model with Spark ML framework 
* [Pyspark LinearRegression Grid Search demo ](https://github.com/yennanliu/analysis/blob/master/SPARK_/Spark_ML_LinearRegression_GridSearch_demo.py) -  Train a Grid Search tuned linear model with Spark ML framework 
* [Pyspark Collaborative Filtering demo ](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/SPARK_/Spark_ML_Collaborative_Filtering_Intro.ipynb) -  Spark recommdation algorithm (ALS model) demo with movielens dataset

*spark APP* <br>
* [Pyspark Data Preprocess 1 : PTT ](https://github.com/yennanliu/analysis/blob/master/SPARK_/Spark_PTTdataMySQL_analysis.py) - Digest [PTT (批踢踢實業坊)](https://en.wikipedia.org/wiki/PTT_Bulletin_Board_System) data via Pyspark batch 
operations. [PTT](https://term.ptt.cc/)
* [Pyspark Data Preprocess 2 : UBER](https://github.com/yennanliu/analysis/blob/master/SPARK_/Spark_Uber_data_analysis.py)  Digest UBER data via Pyspark batch operations. 
* [Pyspark Streaming demo 1](https://github.com/yennanliu/analysis/blob/master/SPARK_/Spark_stream_demo.py) -  a simple word-count app data via Pyspark stream  


## Development 
- `dev` 
