import requests
import os

def telegram_bot_send_text(bot_message):
    bot_token = os.environ.get("BOT_TOKEN")
    bot_chatID = os.environ.get("BOT_CHATID")

    if not bot_token or not bot_chatID:
        print("Error: Telegram BOT_TOKEN or BOT_CHATID environment variables are not set.")
        return {"ok": False, "error": "Missing Telegram credentials"}

    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID \
                + '&parse_mode=Markdown&text=' + bot_message
    
    bot_response = requests.get(send_text)
    return bot_response.json()

api_key = os.environ.get("API_KEY")

if not api_key:
    print("Error: OpenWeatherMap API_KEY environment variable is not set.")
    exit() 


parameters = {
    "lat": 14.676208,  # Latitude for Quezon City, Philippines
    "lon": 121.043861, # Longitude for Quezon City, Philippines
    "appid": api_key, 
    "cnt": 4, # time intervals (4 * 3 hours = 12 hours)
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status() 
weather_data = response.json()

will_rain = False 

# The 'forecast' API returns 3-hour intervals, so 4 intervals cover 12 hours
for interval in range(4): # Loop for the next 4 (3-hour) intervals
    if 'list' in weather_data and len(weather_data['list']) > interval:
        weather_id = (weather_data['list'][interval]['weather'][0]['id'])
        if weather_id < 700:
            will_rain = True
            break 

# Check the correct variable 'will_rain'
if will_rain:
    message = "🌧 It's going to rain today, bring an umbrella with you."
    telegram_bot_send_text(message)
else:
    print("No rain expected in the next 12 hours.")
