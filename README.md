## Norapi
# sorry, links are broken already
### create a virtual environment and run:


_pip install -r requirements.txt_

* scraper.py --- this is the main controller
  * get_patterns.py --- this is a module that contains a regex pattern
    * scraper.py reads the sauce.json to get the url of the specified anime i need
    * after reading the url in sauce.json,it performs some operation and writes the results to anime_data.json
 *  app.py is a flask app
    * it reads the data from anime_data.json and returns it as a json api
    * the static folder just contains a favicon.ico file, i needed to add it because any time i run app.py, it returns err 500
    ### already deployed norapi to heroku, here's the sauce:
         https://norapi.herokuapp.com/
## PREVIEW:
![api](https://user-images.githubusercontent.com/71889751/99081702-7fecae00-25c3-11eb-9b36-c464742cf6e9.png)

#### btw i scraped these data from https://animelist.pw/ and for the image url in sauce.json, i got it from http://takanimelist.live/
###      if you need tips in creating a virtual environment, check here: https://www.youtube.com/watch?v=APOPm01BVrk&ab_channel=CoreySchafer
