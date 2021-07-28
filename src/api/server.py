

from flask import Flask, request, render_template
import os,sys
import argparse
import json
from flask import Flask
import pymysql
from sqlalchemy import create_engine
dir = os.path.dirname
src_path = dir(dir(dir(__file__)))
sys.path.append(src_path)

from SRC.utils_.apis_tb import read_json, return_json



app = Flask(__name__)

@app.route("/") 
def home():
    """ Default path """
    return "Easy Tour"

def main():
    
    settings_file = dir(__file__) + os.sep + "jason.json"
    
    # Load json from file
    json_readed = read_json(fullpath=settings_file)

    DEBUG = json_readed["debug"]
    HOST = json_readed["host"]
    PORT_NUM = json_readed["port"] 

    app.run(debug=DEBUG, host=HOST, port=PORT_NUM)

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--x", type=str, help="password") # Important! --> type

if __name__ == "__main__": 

    # To run in cmd : python C:\Users\xyang\OneDrive\Escritorio\ARCHIVOS\THEBRIDGE\Data-Science-Bootcamp-21\ENTREGABLES\00_POYECTO_ML\src\api\server.py -x "Pablo"
    args = vars(parser.parse_args())
    print(args.values())
    if args["x"] == "Tripulaciones5": 
        main()
    else:
        print("wrong password")