from flask_restful import Resource, reqparse
from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql
from datetime import datetime
from connection import get_db_connection


class Login(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', required=True, help='Volume is required')
        self.parser.add_argument('pwd', required=True, help='Adjusted price is required')

    def get(self):
        email = request.args.get('email')
        pwd = request.args.get('pwd')
        if not email or not pwd:
            return 'Invalid Credential', 401
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = sql.SQL("""
                SELECT * FROM public.user_credential where email = %s AND pwd = %s;
            """)
            cursor.execute(query, (email, pwd))
            conn.commit()
            result = cursor.fetchone()
            if result:
                return {"message": "user found"}, 200
            else: 
                return {"message": "User email and passowrd combination doesn't exist"}, 401
        except Exception as e:
            print(e)
            return {"message": "Database Error"}, 500

class Register(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str, required=True, help='Volume is required')
        self.parser.add_argument('pwd', type=str, required=True, help='Adjusted price is required')
        self.parser.add_argument('username', type=str, required=True, help='Volume is required')
        self.parser.add_argument('phoneNumber', type=str, required=True, help='Volume is required')

    def post(self):
        args = self.parser.parse_args()
        email = args['email']
        pwd = args['pwd']
        username = args['username']
        phoneNumber = args['phoneNumber']
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            select_query = sql.SQL("""
                SELECT * from public.user_credential where username = %s AND email = %s limit 1;
            """)
            cursor.execute(select_query, (username, email))
            conn.commit()
            result = cursor.fetchone()
            if result:
                print("No duplicated user_credential, start registering")
                insert_query = sql.SQL("""
                INSERT INTO public.user_credential (username, email, pwd, phoneNumber, plan1, plan2, plan3, plan4, plan5)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                """)
                cursor.execute(insert_query, (username, email, pwd, phoneNumber, "NULL", "NULL", "NULL", "NULL", "NULL"))
                conn.commit()
                return {"messaage": "register success"}, 200
            else:
                print("Username or email existed")
                return {"message": "user existed"}, 400
        except Exception as e:
            return {'message': e}, 500
        

'''
INSERT INTO public.user_credential (username, email, pwd, phoneNumber, plan1, plan2, plan3, plan4, plan5)
                VALUES ('test','test','test','test','test','test','test','test','test')

'''