## Norapi
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
