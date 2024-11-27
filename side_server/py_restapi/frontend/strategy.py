from flask_restful import Resource, reqparse
from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql
from datetime import datetime
from connection import get_db_connection
import pandas as pd

class PE(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.pe_top = 10
        self.pe_strategy = 'pe'
    def get(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        query = sql.SQL('''
            SELECT * FROM public.block_code3_deatil where strategy = %s order by da desc limit %s;
        ''')
        cursor.execute(query, (self.pe_strategy, self.pe_top))
        conn.commit()
        result = cursor.fetchall()
        if result:
            data = [{'da': pd.to_datetime(row[1]).strftime("%Y-%m-%d"), 'code': row[0], 'cl': row[2]} for row in result]
            return jsonify(data)
        else:
            return {"message": "Database Error"}
        
class TwseBullbear(Resource):
    def __init__(self):
        pass
    def get(self):
        day = request.args.get('day')
        query = sql.SQL(f'''
            SELECT * FROM public.block_code3_deatil
            WHERE strategy = 'TWSE bullbear' AND da >= NOW() - INTERVAL '{day} days'
            order by da desc;
        ''')
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
            if not result:
                return {"message": "no correct db response for /price"}
            data = [{
                'da': pd.to_datetime(row[1]).strftime("%Y-%m-%d"), 
                'signal': row[4],
            } for row in result]
            print(data)
            return jsonify(data)
        except Exception as e:
            return jsonify({"error message for twse bullbear":str(e)})
    