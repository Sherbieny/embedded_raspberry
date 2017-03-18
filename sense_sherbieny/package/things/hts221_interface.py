#Following the API's example for humidity
from sense_hat import SenseHat

sense = SenseHat()
humidity = sense.get_humidity()
print("Humidity: %s %%rH" % humidity)

result = str(humidity)
sense.show_message(result, text_colour=[255,0,0])

