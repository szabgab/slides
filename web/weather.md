# Weather App
{id: weather-app}

## Weather App background
{id: weather-app-background}

* [appid](http://openweathermap.org/appid)
* [daily forcast](http://api.openweathermap.org/data/2.5/forecast/daily?APPID=YOURAPIKEY)
* [API](http://openweathermap.org/api)
* Sign up at [Open Weather Map](http://openweathermap.org/)
* Sign in

![](examples/weather/examples.html)


## Weather App - steps
{id: weather-app-steps}

1. Sekeleton
1. Include dependenices, Add dependencies to App
1. Add routing
1. Update form to have ng-click and ng-model , set the url to include the name, if there was a name
1. In the controller Grab the value from
1. The temratures are in Kelvin. Add buttons so the users can select if they want to see the temratures in Kelvin, Fahrenheit, or Celsius.  Round the numbers to 1 digit after the decimal point.  C = K - 273.15;  F = kelvin * 9/5 - 459.67; 
1. Allow the user to see 1, 3, 5 days. Show buttons that will set this value. (The measurement are currently every 3 hours)



## Weather App Skeleton
{id: weather-app-skeleton}
![](examples/weather/1/index.html)
![](examples/weather/1/app.js)
![](examples/weather/1/city.html)
![](examples/weather/1/main.html)




