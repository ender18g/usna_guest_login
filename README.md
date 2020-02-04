# usna_guest_login


This python script will automatically log you onto the USNA guest network.

**setup the required packages:**
```
git clone https://github.com/ender18g/usna_guest_login.git
sudo apt install chromium-chromedriver
python3 -m venv LoginVENV
source LoginVENV/bin/activate
cd usna_guest_login
pip install -r requirements.txt
```

**Run the script: (replace the command with your username/password)**
```
python3 USNA_auto_login.py myguestusername myguestpassword
```



I recommend setting up the script to run in Crontab at a set interval to keep your device online.
If you add the below lines to your crontab file, the script will run at startup and every hour.  The output will be logged to log.txt

 **Open Crontab and add the following lines to the file.  (update directory paths/username/password)**


```
sudo crontab -e
@reboot /home/pi/LoginVENV/bin/python /home/pi/usna_guest_login/usna_guest_login.py myusername mypw >> /home/pi/log.txt
0 * * * * /home/pi/LoginVENV/bin/python /home/pi/usna_guest_login/usna_guest_login.py myusername mypw >> /home/pi/log.txt
```
