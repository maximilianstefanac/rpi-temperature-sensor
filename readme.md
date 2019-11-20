# rpi-temperature-sensor
This small project is for using a Raspberry Pi to log temperature data of a DHT11 sensor and make it available using a HTTP interface.

## temperature-app.py
Flask app with HTTP interface. It reads the temperature data from the local SQLite Database.

## temperature-job.py
Job which inserts data from the connected DHT11 sensor to the database. It uses the [Adafruit_Python_DHT Library](https://github.com/adafruit/Adafruit_Python_DHT)

## Installation
1. clone this repository
2. open a terminal / bash in the local copy of the git repository
3. install python dependencies using pip `pip install -r requirements.txt`

## CRON job
execute 
1. open crontab `crontab -e`
2. append following code `*/5 * * * * python /home/pi/git/rpi-temperature-sensor/temperature-job.py` you may have to adjust the path of your cloned repository
3. restart cron deamon `/etc/init.d/cron restart` or restart the raspberry pi `sudo reboot`