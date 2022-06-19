from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise HousingException("We are testing custum exception")
    except HousingException as e:
            housing=HousingException(e,sys)
            logging.info(housing.error_message)
            logging.info("We are testing logging module")
            #logging.error(housing.get_detail_error_message(housing.error_message,housing.error_details))    

    return "Working on CICD pipeline."


if __name__=="__main__":
    app.run(debug=True)
