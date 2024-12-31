import time
import os
# import schedule

def execute_movie_scrapper_fun():
    os.system("python movie_scrapper.py")


execute_movie_scrapper_fun()    

# schedule.every(1).minutes.do(execute_movie_scrapper_fun)


# while True:
#     schedule.run_pending()
#     time.sleep(1)



