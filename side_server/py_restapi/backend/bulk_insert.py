from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values
from connection import get_db_connection

class BulkInsertBlockCode3Detail(Resource):
    def post(self):
        data = request.json

        # Validate input data
        if not isinstance(data, list):
            return {'message': 'Data should be a list of records'}, 400

        if not all(
            isinstance(record, list) and len(record) == 3 for record in data
        ):
            return {'message': 'Each record should be a list with exactly 3 elements'}, 400
        
        try:
            # Connect to the database
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Define the SQL query
            insert_query = sql.SQL("""
                INSERT INTO public.block_code3_deatil (code, da, cl)
                VALUES %s
            """)
            
            # Execute the bulk insert
            execute_values(cursor, insert_query, data)
            
            # Commit the transaction
            conn.commit()
            return {'message': 'Bulk insert successful'}, 201
        
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            return {'message': 'Database error'}, 500
        
        finally:
            cursor.close()
            conn.close()