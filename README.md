# Python Flask and Machine Learning

## Aims of this assignment

- Väljaettmaskininlärningsproblem
- Optimeralösningen
- LevereralösningenviaettRESTAPI

## Solution

1. Machine Learning aims to address Titanic machine learning problem
 - In order to deal with the machine learning problem, I grasped the database from Vanderbilt University

``` https://biostat.app.vumc.org/wiki/pub/Main/DataSets/titanic.txt ```

 - In order to increase the accuracy rate, any missing data has been replaced with the mean value. The specific steps taken to achieve this are outlined in the Jupyter notebook.
 - To address this problem, a decision tree was used. Instead of using information entropy, Gini Index was applied as it provided an advantage in this particular situation.
    Provost and Fawcett (2013) state that the Gini score remains unchanged regardless of the class chosen by people. The sum of probabilities for all classes is always equal to zero, making a Gini score of zero the purest possible score.
 ![GiniImage](https://github.com/niuniu268/machineLearning/blob/master/imgs/Gini.png)

- Created a decision tree through the website: 
``` http://www.webgraphviz.com/?source=post_page ```

![image1](https://github.com/niuniu268/machineLearning/blob/master/imgs/image1.png)

2. Optimization (Please read through the file, titanic.ipnb)

 - Bootstrap aggregation (Begging)
 - Random forest
 - Cross validation

3. REST Api
 - visit ``` 127.0.0.1:5000```
 
![web1](https://github.com/niuniu268/machineLearning/blob/master/imgs/Screenshot1.png)

 - input age, gender and class and then gain the result

![web2](https://github.com/niuniu268/machineLearning/blob/master/imgs/Screenshot2.png)

## Reference

    Provost, F., & Fawcett, T. (2013). Data Science for Business: What you need to know about data mining and data-analytic thinking. Köln, CA: O`Reilly.
