# usna_guest_login


This python script will automatically log you onto the USNA guest network.

**setup the required packages:**
```
sudo apt install chromium-chromedriver
python3 -m venv LoginVENV
source LoginVENV/bin/activate
cd usna_guest_login
pip install -r requirements.txt
```

**Run the script:**
```
python3 USNA_auto_login.py myguestusername myguestpassword
```



I recommend setting up the script to run in Crontab at a set interval to keep your device online.
