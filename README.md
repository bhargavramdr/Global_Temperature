# Global_Temperature
About 99 percent Accurate predictor of the Global Temperature.

## Here's how it looks:

![Screenshot (150)](https://user-images.githubusercontent.com/72303641/138690547-0f09db07-a85a-4f62-8168-3794fb98cfd1.png)

## Data Preparation
**We are going to import the data, and then take a look the data.**

![image](https://user-images.githubusercontent.com/72303641/138690797-57b877fc-3fbb-4270-9d1e-016c5d3d11bc.png)
![image](https://user-images.githubusercontent.com/72303641/138690826-d4cef55a-a29a-4c8f-8e00-1358a3c2737f.png)

 
## Handling missing values

![image](https://user-images.githubusercontent.com/72303641/138690870-ca5808ec-05a3-45ae-a092-5b58f8f2c180.png)


## Converting the temperature from Celsius to Fahrenheit
![image](https://user-images.githubusercontent.com/72303641/138690915-96429b72-51e2-4648-8d95-d613178e3fb1.png)


## Correlation matrix

![image](https://user-images.githubusercontent.com/72303641/138690960-6bba4e21-42a5-4f2d-ae8a-dde37db806e7.png)
 


## Dropping the useless columns
 
![image](https://user-images.githubusercontent.com/72303641/138691000-22d6bf88-e28a-40f0-abad-0898140c7c3a.png)

## Test train split
![image](https://user-images.githubusercontent.com/72303641/138691036-f7725c44-9715-4c0c-8461-db196c75ff28.png)

## Baseline Mean Absolute Error
**Before we can make and evaluate any predictions on our machine learning model to predict weather, we need to establish a baseline, a sane metric that we hope to beat with our model. If our model cannot improve from the baseline then it will fail and we should try a different model or admit that machine learning is not suitable for our problem:**
 
![image](https://user-images.githubusercontent.com/72303641/138691056-0e5195e8-5070-4c2e-a35d-bd3f2a0b8fbb.png)

## Prediction and Accuracy:
 
![image](https://user-images.githubusercontent.com/72303641/138691089-8ca4ca1f-51e9-45df-9f9d-1ee9dea87d69.png)


**Accuracy of 99.6 is not at all bad!**
