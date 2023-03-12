import time
import board
import adafruit_dht
from datetime import datetime
#Initialize the dht device with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)
while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9/5) + 32
        humidity = dhtDevice.humidity
        
        time1 = datetime.now()
        mydate = time1.strftime("\"%d/%m/%Y\"")
        mytime = time1.strftime("\"%H:%M:%S\"")
        
        data = "{\"temp_f\":\""+str(temperature_f)+"\",\n \"temp_c\":\""+str(temperature_c)+"\",\n \"humid\":\""+str(humidity)+"\",\n \"time\":"+str(mytime)+",\n \"date\":"+str(mydate)+"}"
        
        file = open("datajson.json", 'w')
        file.write(data)
        file.close()
        
        print("Temp: {:.1f} F / {:.1f} C   Humidity: {}% "
              .format(temperature_f, temperature_c, humidity))
    except RuntimeError as error:
        #Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
    time.sleep(2.0)
