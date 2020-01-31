
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import time
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("username", help="your guest username")
parser.add_argument("password", help ="your guest password")
args = parser.parse_args()



url='https://portal.usna.edu/guest/usna_guestlogin.php'
username = args.username
password = args.password


def login(username,password):
  chrome_options = Options()
  chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
#  chrome_options.add_argument("--headless")
  chrome_options.add_argument("-disable-gpu")
  chrome_options.add_argument('--no-sandbox')
#  chrome_driver = '/usr/lib/chromium-browser/chromedriver'
#  driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(url)
  time.sleep(4)
  driver.execute_script(f"$(':input',' [id$=weblogin_user]').val('{username}');")
  driver.execute_script(f"$(':input',' [id$=weblogin_password]').val('{password}');")
  driver.execute_script(f"$(':input',' [id$=weblogin_visitor_accept_terms]').click();")

  driver.execute_script(f"$(':input',' [id$=weblogin_visitor_accept_terms]').prop('checked',true);")

  time.sleep(2)
  driver.execute_script(f"$('form').submit();")
  time.sleep(3)
  driver.close()
  return 'completed logging in!'

def internet_on():
  try:  r = requests.get("https://www.google.com", timeout=4)
  except: return False
  if r.status_code ==requests.codes.ok and r.headers['Server']== 'gws':
    return True
  return False 

if __name__== "__main__":
  attempts = 0
  while True:
    attempts +=1
    if attempts>10:
      break
    if (internet_on()):
      print("internet is ON")
      break
    else:
      print("internet is OFF")
      try: print(login(username,password))
      except: print("error logging in")
    time.sleep(10)
