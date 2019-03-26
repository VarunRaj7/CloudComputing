# RESTFUL WEB SERVICES

## Weather Forecast Services

### Contents

1. All About Code

2. Resources

3. References

### 1. All About Code

Weather data available in the file HW2/Restfulapi/daily.csv is used to build the api. The code works like this:

1. When the services are started the api will load all the data from the file and loads into the two lists of dictionary namely, res1, which conatins all the dates for which weather details are available, and res2, which conatins the temperature details for every date, in the code.

2. All the HTTP methods manipulate these two variables, for instance if "get" method is used to get the data relating to a particular date then the search begins like this: the matched date value in the res2(list of dictionary) is acquired and returned to the user.

3. In the similar manner every method, operates on these two variables and respond corespondingly.

4. However, the scenario is different while forecasting. That is, though the same variable are used but the **MOVING AVERAGE** algorithm is used to predict the temperatures which are not available from 02-15-2018 to 02-29-2018, this is done by the function forecast() in the code. 

#### 2. Resources:

1. http://ec2-18-216-188-121.us-east-2.compute.amazonaws.com/historical/ or
   http://18.216.188.121:80/historical/
  
    Method: **GET**
  
    Input Parameters: No input parameters
  
    Response Content type: application/json
  
    Response Code:
  
    Code | Description
    -----|-------------
    HTTP 200 | Succesful Operation 
    HTTP 400 | Operation Failed
    
    Output parameters and their respective datatypes:
    
    Parameter | Datatype
    -----|-------------
    DATE | String
    
    Example Response:
    
    ![S1](https://github.uc.edu/rayabavj/CloudComputing/blob/master/HW2/Restfulapi/S1.PNG)

2. http://ec2-18-216-188-121.us-east-2.compute.amazonaws.com/historical/{DATE} or
   http://18.216.188.121:80/historical/{DATE}
   
    Method: **GET**
  
    Input Parameters: DATE
    
    Input Parameter Datatype: string
  
    Response Content type: application/json
  
    Response Code:
  
    Code | Description
    -----|-------------
    HTTP 200 | Succesful Operation 
    HTTP 400 | Date not found
    
    Output parameters and their respective datatypes: 
    
    Parameter | Datatype
    -----|-------------
    DATE | String 
    TMAX | Number
    TMIN | Number
    
    Example Response:
    
    ![S2](https://github.uc.edu/rayabavj/CloudComputing/blob/master/HW2/Restfulapi/S2.PNG)
    
3. http://ec2-18-216-188-121.us-east-2.compute.amazonaws.com/forecast/{DATE} or
   http://18.216.188.121:80/forecast/{DATE}
  
    Method: **GET**
  
    Input Parameters: DATE
    
    Input Parameter Datatype: string
  
    Response Content type: application/json
  
    Response Code:
  
    Code | Description
    -----|-------------
    HTTP 200 | Succesful Operation 
    HTTP 400 | Date not found (Within 2/29/2018)
    
    Output parameters and their respective datatypes: 
    List of the following parameters for the seven days from the date given in input
    
    Parameter | Datatype
    -----|-------------
    DATE | String 
    TMAX | Number
    TMIN | Number
    
    Example Response:
    
    ![S3](https://github.uc.edu/rayabavj/CloudComputing/blob/master/HW2/Restfulapi/S3.PNG)

4. http://ec2-18-216-188-121.us-east-2.compute.amazonaws.com/historical/{DATE} or 
   http://http://18.216.188.121:80/historical/{}DATE
  
    Method: **DELETE**
  
    Input Parameters: DATE
    
    Input Parameter Datatype: string
  
    Response Content type: application/json
  
    Response Code:
  
    Code | Description
    -----|-------------
    HTTP 200 | Succesful Operation 
    HTTP 400 | Date not found
    
    Output Parameter: No output Parameter
    
    Example Response:
    
    ![S2](https://github.uc.edu/rayabavj/CloudComputing/blob/master/HW2/Restfulapi/S4.PNG)

5. http://ec2-18-216-188-121.us-east-2.compute.amazonaws.com/historical/ with data {DATE:<>,TMAX:<>,TMIN:<>} or
   http://http://18.216.188.121:80/historical/ with data {DATE:<>,TMAX:<>,TMIN:<>}
  
    Method: **POST**
  
    Input Parameters and their respective datatype:

    Parameter | Datatype
    -----|-------------
    DATE | String 
    TMAX | Number
    TMIN | Number
  
    Response Content type: application/json
  
    Response Code:
  
    Code | Description
    -----|-------------
    HTTP 201 | Succesful Operation 
    HTTP 400 | Date not found
    
    Output parameters and their respective datatypes: 
    
    Parameter | Datatype
    -----|-------------
    DATE | String 
    
    Example Response:
    
    ![S5](https://github.uc.edu/rayabavj/CloudComputing/blob/master/HW2/Restfulapi/S5.PNG)
    
    HW2 Evaluation Code result:
    
    https://github.uc.edu/rayabavj/CloudComputing/blob/master/HW2/Restfulapi/HW2_testing_code_output.PNG

#### 3. Refernces:

These are only references for coding in python. None of them provide the entire code in any form.

http://flask-restful-cn.readthedocs.io/en/0.3.5/quickstart.html

https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search

https://stackoverflow.com/questions/17149561/how-to-find-a-value-in-a-list-of-python-dictionaries

https://stackoverflow.com/questions/30491841/python-flask-restful-post-not-taking-json-arguments

https://stackoverflow.com/questions/14524322/how-to-convert-a-date-string-to-different-format

https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python

https://stackoverflow.com/questions/3240458/how-to-increment-the-day-in-datetime-python

https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python


