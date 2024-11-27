from flask_restful import Resource, reqparse
from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql
from datetime import datetime
from connection import get_db_connection

class InsertRealTimeTop3(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('da', type=str, required=True, help='Date is required')
        self.parser.add_argument('code', type=str, required=True, help='Stock code is required')
        self.parser.add_argument('cl', type=float, required=True, help='Closing price is required')
        self.parser.add_argument('hi', type=float, required=True, help='High price is required')
        self.parser.add_argument('lo', type=float, required=True, help='Low price is required')
        self.parser.add_argument('op', type=float, required=True, help='Opening price is required')
        self.parser.add_argument('vol', type=int, required=True, help='Volume is required')
        self.parser.add_argument('adj', type=float, required=True, help='Adjusted price is required')

    def post(self):
        args = self.parser.parse_args()
        da = args['da']
        code = args['code']
        cl = args['cl']
        hi = args['hi']
        lo = args['lo']
        op = args['op']
        vol = args['vol']
        adj = args['adj']

        # check da datatype
        # try:
        #     da = datetime.strptime(da, '%Y-%m-%dT%H:%M:%S')
        # except ValueError:
        #     return {'message': 'Invalid date format. Use YYYY-MM-DDTHH:MM:SS'}, 400

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            # Insert data into the table
            insert_query = sql.SQL("""
                INSERT INTO public.realtime_top3 (da, code, cl, hi, lo, op, vol, adj)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """)
            cursor.execute(insert_query, (da, code, cl, hi, lo, op, vol, adj))

            # Commit the transaction
            conn.commit()
            return {'message': 'insert into realtime_top3 success'}, 201

        except psycopg2.Error as e:
            print(f"Database error: {e}")
            return {'message': 'Database error'}, 500
        finally:
            cursor.close()
            conn.close()

class InsertStockPrice(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('da', type=str, required=True, help='Date is required')
        self.parser.add_argument('code', type=str, required=True, help='Stock code is required')
        self.parser.add_argument('cl', type=float, required=True, help='Closing price is required')
        self.parser.add_argument('hi', type=float, required=True, help='High price is required')
        self.parser.add_argument('lo', type=float, required=True, help='Low price is required')
        self.parser.add_argument('op', type=float, required=True, help='Opening price is required')
        self.parser.add_argument('vol', type=int, required=True, help='Volume is required')
        self.parser.add_argument('adj', type=float, required=True, help='Adjusted price is required')

    def post(self):
        args = self.parser.parse_args()
        da = args['da']
        code = args['code']
        cl = args['cl']
        hi = args['hi']
        lo = args['lo']
        op = args['op']
        vol = args['vol']
        adj = args['adj']

        # check da datatype
        # try:
        #     da = datetime.strptime(da, '%Y-%m-%dT%H:%M:%S')
        # except ValueError:
        #     return {'message': 'Invalid date format. Use YYYY-MM-DDTHH:MM:SS'}, 400

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            # Insert data into the table
            insert_query = sql.SQL("""
                INSERT INTO public.stock_price (da, code, cl, hi, lo, op, vol, adj)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """)
            cursor.execute(insert_query, (da, code, cl, hi, lo, op, vol, adj))

            # Commit the transaction
            conn.commit()
            return {'message': 'insert into stock_price success'}, 201

        except psycopg2.Error as e:
            print(f"Database error: {e}")
            return {'message': 'Database error'}, 500
        finally:
            cursor.close()
            conn.close()

class InsertPrice(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('da', type=str, required=True, help='Date is required')
        self.parser.add_argument('code', type=str, required=True, help='Stock code is required')
        self.parser.add_argument('cl', type=float, required=True, help='Closing price is required')
        self.parser.add_argument('hi', type=float, required=True, help='High price is required')
        self.parser.add_argument('lo', type=float, required=True, help='Low price is required')
        self.parser.add_argument('op', type=float, required=True, help='Opening price is required')
        self.parser.add_argument('vol', type=int, required=True, help='Volume is required')
        self.parser.add_argument('adj', type=float, required=True, help='Adjusted price is required')
        self.parser.add_argument('wma_20', type=float, required=True, help='wma20')
        self.parser.add_argument('wma_50', type=float, required=True, help='wma50')
        self.parser.add_argument('wma_100', type=float, required=True, help='wma100')
        
    def post(self):
        args = self.parser.parse_args()
        da = args['da']
        code = args['code']
        cl = args['cl']
        hi = args['hi']
        lo = args['lo']
        op = args['op']
        vol = args['vol']
        adj = args['adj']
        wma20 = args['wma_20']
        wma50 = args['wma_50']
        wma100 = args['wma_100']

        # check da datatype
        # try:
        #     da = datetime.strptime(da, '%Y-%m-%dT%H:%M:%S')
        # except ValueError:
        #     return {'message': 'Invalid date format. Use YYYY-MM-DDTHH:MM:SS'}, 400

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            # Insert data into the table
            insert_query = sql.SQL("""
                INSERT INTO public.price (da, code, cl, hi, lo, op, vol, adj, wma_20, wma_50, wma_100)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """)
            cursor.execute(insert_query, (da, code, cl, hi, lo, op, vol, adj, wma20, wma50, wma100))

            # Commit the transaction
            conn.commit()
            return {'message': 'insert into price success'}, 201

        except psycopg2.Error as e:
            print(f"Database error: {e}")
            return {'message': 'Database error'}, 500
        finally:
            cursor.close()
            conn.close()


class InsertMaincode(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('code', type=str)
        self.parser.add_argument('cname', type=str)
        self.parser.add_argument('ename', type=str)
        self.parser.add_argument('round_lot', type=int)
        self.parser.add_argument('outstanding_shares', type=int)
        self.parser.add_argument('equity_float', type=float)
        self.parser.add_argument('is_download_data', type=bool)
        self.parser.add_argument('is_rt', type=bool, default=False)

    def post(self):
        args = self.parser.parse_args()
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            insert_query = sql.SQL("""
                INSERT INTO public.maincode (code, cname, ename, round_lot, outstanding_shares, equity_float, is_download_data, is_rt)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """)
            cursor.execute(insert_query, (
                args.get('code'),
                args.get('cname'),
                args.get('ename'),
                args.get('round_lot'),
                args.get('outstanding_shares'),
                args.get('equity_float'),
                args.get('is_download_data'),
                args.get('is_rt')
            ))
            conn.commit()
            return {'message': 'insert into maincode success'}, 201
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            conn.rollback()
            return {'message': 'Database error'}, 500
        finally:
            cursor.close()
            conn.close()

class InsertSignal(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('code', type=str, required=True, help='Code is required')
        self.parser.add_argument('da', type=str, required=True, help='Date is required')
        self.parser.add_argument('cl', type=float, required=True, help='Closing price is required')

    def get(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            insert_query = sql.SQL("""
                SELECT * from public.block_code3_deatil limit 10;
            """)
            cursor.execute(insert_query)
            conn.commit()
            return {'message': 'insert into block_code3 success'}, 201

        except psycopg2.Error as e:
            print(f"Database error: {e}")
            conn.rollback()
            return {'message': 'Database error'}, 500
    def post(self):
        args = self.parser.parse_args()
        code = args['code']
        da = args['da']
        cl = args['cl']

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            insert_query = sql.SQL("""
                INSERT INTO public.block_code3_deatil (code, da, cl)
                VALUES (%s, %s, %s)
            """)
            cursor.execute(insert_query, (code, da, cl))
            conn.commit()
            return {'message': 'insert into block_code3 success'}, 201
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            conn.rollback()
            return {'message': 'Database error'}, 500
        finally:
            cursor.close()
            conn.close()