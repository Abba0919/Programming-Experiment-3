# Programming-Experiment-3

### Intended Learning Outcomes
1. To identify the codes and functions incorporated in the Pandas library
2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

## Problem 1:

Using knowledge obtained from the experiment and demonstrations:

a. Load the corresponding .csv file into a data frame named cars using pandas

### Input: 
```python
import pandas as pd
#Load the corresponding .csv file into a data frame named cars using pandas
cars = pd.read_csv('cars.csv')
cars
```

### Output:
![Screenshot 2024-09-18 231631](https://github.com/user-attachments/assets/1dfb2022-c3d1-4a28-a4fd-ef004d590d66)


b. Display the first five and last five rows of the resulting cars.

### Input:
```python
#Display the first five rows of the resulting cars
cars.head()
#Display the last five rows of the resulting cars
cars.tail()
```

### Output:

![head](https://github.com/user-attachments/assets/7d2665e7-acd7-4dfa-97e2-a6672a1b2eb0)


![image](https://github.com/user-attachments/assets/7f033d72-fb53-49db-b8a8-7f1ae7c28f71)

## Problem 2:

Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
indexing operations.

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

### Input:
```python
import pandas as pd
#Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
cars[1::2].head()
cars = pd.read_csv('cars.csv')
cars
```

### Output:

![a](https://github.com/user-attachments/assets/9da6b6a9-4e91-4614-8255-1a70f8a97bf0)

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

### Input: 
```python
#Display the row that contains the Model of Mazda RX4
cars.loc[cars['Model']=='Mazda RX4']
```

### Output:
![b](https://github.com/user-attachments/assets/ecc9e39d-4e69-4726-a5fe-a20a59db5240)

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

### Input:
```python
#Display how many cylinders does Camaro Z28 have
cars.loc[[23],['Model', 'cyl']]
```

### Output:
![c](https://github.com/user-attachments/assets/9ce49135-4b9d-4dbe-b93f-72130aa1400a)

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

### Input:
```python
#Display how many cylinders and gears does the 3 models have
cars.loc[[1, 28, 18],['Model', 'cyl', 'gear']]
```

### Output:
![d](https://github.com/user-attachments/assets/fc87593d-d1f8-4e68-abd1-f80eaef70dcf)

## Author: Merwin Abba B. Llorin

