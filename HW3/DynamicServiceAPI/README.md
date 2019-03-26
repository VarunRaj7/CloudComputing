# Dynamic Weather Service API with UI
### Contents
1. How to use the API?
2. All About the Code
3. Resources
4. References
### 1. How to use the API?
This weather service api can be used to get the maximum and minimum temperature for a period of seven days given the starting date. Moreover, it compares the results from the Weather Underground data for the same data and same days. In order to access the services, click the link below:

http://18.188.80.28/

The api is also provided with the attractive user interface as shown below:
![SS1](https://github.com/VarunRaj7/CloudComputing/blob/master/HW3/DynamicServiceAPI/SS1.PNG)

Upon clicking the calender icon beside the input form, a datepicker will pop up as shown below:
![SS2](https://github.com/VarunRaj7/CloudComputing/blob/master/HW3/DynamicServiceAPI/SS2.PNG)

Select the date and hit submit button below the input form. A sample result is shown below:
![SS3](https://github.com/VarunRaj7/CloudComputing/blob/master/HW3/DynamicServiceAPI/SS3.PNG)

You can also hover over the result to experience the pop-up animation as shown below:
![SS4](https://github.com/VarunRaj7/CloudComputing/blob/master/HW3/DynamicServiceAPI/SS4.PNGG)

### CAUTION: DO NOT MAKE MORE THAN 1 REQUEST PER MINUTE, OTHERWISE THE WEATHER UNDERGROUND KEYID WILL BE DISABLED 

### 2. All About the Code
This section consists of two parts, one for the code in the app.py and the other for the code in the home.html.

#### app.py code description:

This code is almost same as the code in the HW2 but with two changes:

1. The code to forecast for the temperature that is not given in the daily.csv is predicted using **Moving Average**, which is now changed to the **Polynomial Regression of degree '5'**. However, the code to obtain the weights/coefficients are given in the python file: https://github.uc.edu/rayabavj/CloudComputing/blob/master/HW03/DynamicServiceAPI/PolynomialRegression.py. 

	Only, the 2017 maximum and minimum temperatures are used as the training data for this regression. 

2. The second change is: another resource called wuforecast is added to the api to call the services of **Weather Underground**. You have to replace <yourwundergroundKeyID> in the code with your keyID that you get to access these services of wunderground.

#### home.html code description:

This section mainly illustrates about the JavaScript in home.html file. The code starts with the function to check if the data is fully loaded, then the fucntion to activate datepicker upon clicking the calender icon is describe as follows:

	$btn.on('click', function(){
			dp.show();
			$input.focus();
			});

After that, the submit click function consists of two $.getJSON function to call the two resources namely, "/forecast/<date>" and "/wuforecast/<date>" to get the maximum temperature and minimum temperature for the seven days begining with the given date from these resources.

It also consists of "$("#chartContainer").CanvasJSChart(options);" to plot the information obtained from these resources on the graph with the custom settings given in the variable options.

### 3. Resources:
All the resources are same as in HW2 (https://github.uc.edu/rayabavj/CloudComputing/blob/master/HW2/Restfulapi/README_REST.md), except the new added resource as described in section 2 is described here:

1. http:///wuforecast/{DATE} or
   http:///wuforecast/{DATE}
  
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
    WUTMAX | Array of Number
    WUTMIN | Array of Number
    
    Example response for this resource:
    ![SS5](https://github.com/VarunRaj7/CloudComputing/blob/master/HW3/DynamicServiceAPI/SS5.PNG)

### 4. References:

https://stackoverflow.com/questions/22259847/application-not-picking-up-css-file-flask-python

http://browardschools.com/calendars

https://stackoverflow.com/questions/620305/convert-year-month-day-to-day-of-year-in-python

https://www.w3schools.com/jquery/default.asp

http://t1m0n.name/air-datepicker/docs/

https://canvasjs.com/jquery-charts/line-chart/

