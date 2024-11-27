from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS


from backend.backend import InsertStockPrice, InsertRealTimeTop3, InsertPrice, InsertMaincode, InsertSignal
from frontend.login import Login, Register
from frontend.strategy import PE, TwseBullbear
from frontend.fundamentals_price import PRICE, DetailedPrice, Maincode, IntradayData
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "Content-Type": "application/json"}})
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"Hello": "world"}

# backend
api.add_resource(InsertSignal, '/insert_signal')
api.add_resource(InsertMaincode, '/insert_maincode')
api.add_resource(InsertRealTimeTop3, '/insert_realtime_top3')
api.add_resource(InsertStockPrice, '/insert_stock_price')
api.add_resource(InsertPrice, '/insert_price')
api.add_resource(HelloWorld, "/hello")

# frontend(from dart flutter version)
api.add_resource(Login, "/login")
api.add_resource(Register, "/register")

# pages
api.add_resource(IntradayData, '/intraday_data')
api.add_resource(PE, "/strategy")
api.add_resource(PRICE, "/price")
api.add_resource(DetailedPrice, "/detailed_price")
api.add_resource(Maincode, "/maincode")
api.add_resource(TwseBullbear, "/strategy_twse")
if __name__ == "__main__":
    app.run(debug=True, port=8000)