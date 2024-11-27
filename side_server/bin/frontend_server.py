from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)


class HelloDatabase(Resource):
    def get(self):
        return {"Hello": "Database"}

@app.route('/login', methods=['GET'])
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    if email and password:
        query = text('SELECT * FROM user_information WHERE user_email = :email AND user_password = :password LIMIT 2')
        with Session['user']() as session:
            result = session.execute(query, {'email': email, 'password': password}).fetchall()
        if result:
            return 'Login successful', 200
        else:
            return 'Invalid credentials', 401
    else:
        return 'Email and password parameters are required', 400

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    username = data.get('username', '')
    email = data.get('user_email', '')
    password = data.get('user_password', '')
    phone_number = data.get('user_phone_number', '')

    if not all([username, email, password, phone_number]):
        return 'All fields are required', 400

    query = text('INSERT INTO user_information (username, user_email, user_password, user_phone_number) VALUES (:username, :email, :password, :phone_number)')
    with Session['user']() as session:
        session.execute(query, {'username': username, 'email': email, 'password': password, 'phone_number': phone_number})
        session.commit()

    return 'Registration successful', 200

@app.route('/trend', methods=['GET'])
def trend():
    query = text("SELECT * FROM trend WHERE da='2024-01-01' AND strategy = 'trend' ORDER BY rank ASC LIMIT 10")
    with Session['strategy']() as session:
        result = session.execute(query).fetchall()
    trend_data = [{'da': row[0].strftime('%Y-%m-%d'), 'codename': row[1], 'strategy': row[2], 'rank': row[3]} for row in result]
    return jsonify(trend_data), 200

@app.route('/price', methods=['GET'])
def price():
    start = request.args.get('start')
    stock_list = request.args.get('symbols', '')
    symbols = stock_list.split(',')
    quoted_symbols = [f"'{symbol}'" for symbol in symbols]
    sql_in_clause = ', '.join(quoted_symbols)
    query = text(f"SELECT * FROM daily_price WHERE da >= :start AND symbol IN ({sql_in_clause}) LIMIT 10000")
    
    with Session['daily_price']() as session:
        result = session.execute(query, {'start': start}).fetchall()
    
    trend_stock_price = [{'da': row[0].strftime('%Y-%m-%d'), 'codename': row[1], 'symbol': row[2], 'industry': row[3], 'op': row[4], 'hi': row[5], 'lo': row[6], 'cl': row[7]} for row in result]
    return jsonify(trend_stock_price), 200

@app.route('/fundamentals', methods=['GET'])
def fundamentals():
    stock_list = request.args.get('symbols', '')
    symbols = stock_list.split(',')
    quoted_symbols = [f"'{symbol}'" for symbol in symbols]
    sql_in_clause = ', '.join(quoted_symbols)
    query = text(f"SELECT * FROM tw WHERE symbol IN ({sql_in_clause})")
    
    with Session['strategy']() as session:
        result = session.execute(query).fetchall()
    
    trend_stock_fundamentals = [{'symbol': row[0], 'codename': row[1], 'industry': row[2]} for row in result]
    return jsonify(trend_stock_fundamentals), 200

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
