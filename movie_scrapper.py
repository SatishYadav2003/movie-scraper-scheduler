import os
from dotenv import load_dotenv
from helper.helper_methods import execute_driver,check_and_notify_user

load_dotenv()

driver,service = execute_driver()


try:
  driver.get(os.getenv("MP4_MOVIEZ_LINK"))  
  check_and_notify_user()
except Exception as e:
  print("Something went wrong we will scrap again after 1 minutes: ",e)    
finally:
  driver.close()



