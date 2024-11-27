from flask_restful import Resource, reqparse
from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql
from datetime import datetime
from connection import get_db_connection