from flask_restful import Resource, reqparse
from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql
from datetime import datetime
from connection import get_db_connection
import pandas as pd

class PRICE(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('symbols', required=True, help='symbols is required')
        self.start_thumbnail_da = '2024-01-01'
    def get(self):
        codes = request.args.get("codes")
        if not codes:
            return jsonify({"message": "No codes provided"})
        code_list = codes.split(',')
        if not code_list:
            return jsonify({"message": "No codes provided"})
        
        query = sql.SQL('''
            SELECT * FROM public.price
            WHERE code IN ({}) AND da >= '2024-01-01'
            ORDER BY da ASC;
        ''').format(
            sql.SQL(',').join(sql.Placeholder() * len(code_list))
        )
        print(query)
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(query, code_list)
            result = cursor.fetchall()
            if not result:
                return {"message": "no correct db response for /price"}
            data = [{
                'da': pd.to_datetime(row[0]).strftime("%Y-%m-%d"), 'code': row[-1], 
                'vol': row[2],
                'op': row[3],
                'hi': row[4],
                'lo': row[5],
                'cl': row[6],
            } for row in result]
            print(data[:5])
            return jsonify(data)
        except Exception as e:
            return jsonify({"message": str(e)})


class IntradayData(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('symbols', required=True, help='symbols is required')
    def get(self):
        codes = request.args.get("codes")
        if not codes:
            return jsonify({"message": "No codes provided"})
        code_list = codes.split(',')
        code_list = [f"'{i}.TW'" for i in code_list]
        code_list = ",".join(code_list)
        if not code_list:
            return jsonify({"message": "No codes provided"})
        
        query = sql.SQL(f'''
            SELECT da, code, vol, op, hi, lo, cl FROM public.stock_price
            WHERE code IN ({code_list}) AND da >= '2024-06-25' and da <= '2024-06-25 12:00:00'
            ORDER BY da ASC;
        ''')
        print(query)
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(query, code_list)
            result = cursor.fetchall()
            print(result)
            if not result:
                return {"message": "no correct db response for /intraday_data"}
            data = [{
                'da': pd.to_datetime(row[0]).strftime("%Y-%m-%d %H:%M:%S"), 'code': row[1][:-3], 
                'vol': row[2],
                'op': row[3],
                'hi': row[4],
                'lo': row[5],
                'cl': row[6],
            } for row in result]
            print(data[:5])
            return jsonify(data)
        except Exception as e:
            return jsonify({"message": str(e)})


class DetailedPrice(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('symbols', required=True, help='symbol is required')
        self.parser.add_argument('freq', required=True, help='Freq is required')
    
    def get(self):
        codes = request.args.get('codes')
        day = request.args.get('day')
        if not codes:
            return jsonify({"message": "No codes provided"})
        query = sql.SQL(f'''
            SELECT * FROM public.price
            WHERE code = '{codes}' AND da >= NOW() - INTERVAL '{day} days'
            order by da asc;
        ''')
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            if not result:
                return {"message": "no correct db response for /price"}
            data = [{
                'da': pd.to_datetime(row[0]).strftime("%Y-%m-%d"), 'code': row[-1], 
                'vol': row[2],
                'op': row[3],
                'hi': row[4],
                'lo': row[5],
                'cl': row[6],
            } for row in result]
            return jsonify(data)
        except Exception as e:
            return jsonify({"message": str(e)})

class Maincode(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('codes', required=True, help='symbol is required')
    def get(self):
        codes = request.args.get('codes')
        if not codes:
            return jsonify({"message": "No codes provided"})
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(f"select cname from public.maincode where code = '{codes}';")
            conn.commit()
            cname = cursor.fetchone()[0]
            
            if not cname:
                return {"message": "no correct db response for /maincode"}
            return jsonify({"cname":cname})
        except Exception as e:
            return jsonify({"message": str(e)})
        
