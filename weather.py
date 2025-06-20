# # # https://www.google.com/search?q=weather+jalandhar
# # # user agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36
# # #span id= wob_tm
# from requests_html import HTMLSession
# import speech_to_text

# s=HTMLSession()
# query="jalandhar"
# url =f'https://www.google.com/search?q=weather+jalandhar'
# r= s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'})
# temp= r.html.find('span#wob_tm', first=True).text
# print(temp)

# unit= r.html.find('div.vk_bk wob-unit span.wob_t', first=True).text
# print(unit)
# desc= r.html.find('div.vk_bk wob-unit span.wob_t', first=True).text

from pyowm.owm import OWM


def weather():
    owm = OWM("e51925a7054af5b6c5e09f9cde6fe1c5")  # Replace with your key
    mgr = owm.weather_manager()

# Get weather for a city
    city = "Jalandhar"
    weather = mgr.weather_at_place(city).weather
    w=(f"Temperature: {weather.temperature('celsius')['temp']}°C")
    return w
    
    
weather()

