# Python Flask and Machine Learning

## Aims of this assignment

- Väljaettmaskininlärningsproblem
- Optimeralösningen
- LevereralösningenviaettRESTAPI

## Solution

1. Machine Learning aims to address Titanic machine learning problem
 - In order to deal with the machine leanring problem, I grasped the database from Vanderbilt University

``` https://biostat.app.vumc.org/wiki/pub/Main/DataSets/titanic.txt ```

 - For the sake of the higher accurate rate, the omitted data is replaced by the mean. The specific procedures are listed by Jupyter notebook

 - The approach to address this problem is decision tree. In comparision with information entropy, I applied Gini Index when I taken the advantage of Gini Index into account.

    According to Provost and Fawcett (2013), the gini score is not varied in response to arbitrary class which people take. The sum of the probabilities of all arbitrary classes is always equal to zero. Therefore a gini score of zero is the most pure score possible

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