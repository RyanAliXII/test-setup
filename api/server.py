from flask import Flask,jsonify
from flask.views import MethodView
from v1 import register_v1
from mongoengine import connect
from models.product import Product
from setup import initialize
from helpers.utils import CustomJSONEncoder
def create_app():
    app = Flask(__name__)
    app.json_encoder = CustomJSONEncoder
    app.register_blueprint(register_v1('/api/v1'))
    print(f'''     
  
  /$$$$$$  /$$$$$$$  /$$$$$$        /$$$$$$  /$$$$$$$$ /$$$$$$$  /$$    /$$ /$$$$$$  /$$$$$$  /$$$$$$$$
 /$$__  $$| $$__  $$|_  $$_/       /$$__  $$| $$_____/| $$__  $$| $$   | $$|_  $$_/ /$$__  $$| $$_____/
| $$  \ $$| $$  \ $$  | $$        | $$  \__/| $$      | $$  \ $$| $$   | $$  | $$  | $$  \__/| $$      
| $$$$$$$$| $$$$$$$/  | $$        |  $$$$$$ | $$$$$   | $$$$$$$/|  $$ / $$/  | $$  | $$      | $$$$$   
| $$__  $$| $$____/   | $$         \____  $$| $$__/   | $$__  $$ \  $$ $$/   | $$  | $$      | $$__/   
| $$  | $$| $$        | $$         /$$  \ $$| $$      | $$  \ $$  \  $$$/    | $$  | $$    $$| $$      
| $$  | $$| $$       /$$$$$$      |  $$$$$$/| $$$$$$$$| $$  | $$   \  $/    /$$$$$$|  $$$$$$/| $$$$$$$$
|__/  |__/|__/      |______/       \______/ |________/|__/  |__/    \_/    |______/ \______/ |________/
                                                                                                       
                                                                                                       
                                                                                                       
 /$$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$$                   /$$    /$$$$$$   /$$$$$$   /$$$$$$          
| $$__  $$ /$$__  $$| $$__  $$|__  $$__/                 /$$$$   /$$$_  $$ /$$$_  $$ /$$$_  $$         
| $$  \ $$| $$  \ $$| $$  \ $$   | $$          /$$      |_  $$  | $$$$\ $$| $$$$\ $$| $$$$\ $$         
| $$$$$$$/| $$  | $$| $$$$$$$/   | $$         |__/        | $$  | $$ $$ $$| $$ $$ $$| $$ $$ $$         
| $$____/ | $$  | $$| $$__  $$   | $$                     | $$  | $$\ $$$$| $$\ $$$$| $$\ $$$$         
| $$      | $$  | $$| $$  \ $$   | $$          /$$        | $$  | $$ \ $$$| $$ \ $$$| $$ \ $$$         
| $$      |  $$$$$$/| $$  | $$   | $$         |__/       /$$$$$$|  $$$$$$/|  $$$$$$/|  $$$$$$/         
|__/       \______/ |__/  |__/   |__/                   |______/ \______/  \______/  \______/          
                                                                                                       
                                                                                                                                                             
    
    ''')  
    connect(host="mongodb://root:example@mongodb:27017/shop?authSource=admin")
    initialize()
    return app
        # app.run(port=1000,host="0.0.0.0",debug=True)
