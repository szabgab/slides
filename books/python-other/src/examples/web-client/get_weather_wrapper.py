from openweathermap import get_daily_forecast, APIError

try:
    #forecast = get_daily_forecast(49.24966, -123.11934)  # Vancouver, BC, Canada
    forecast = get_daily_forecast(34.8186, 31.8969)  # Rehovot, Israel
    #forecast = get_daily_forecast('Rehovot') 
    print(forecast)
except APIError as err:
    # Deal with missing/incorrect API key or failed requests
    print(err)

