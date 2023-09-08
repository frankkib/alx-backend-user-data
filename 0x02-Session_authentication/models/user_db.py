#!/usr/bin/env python3
import sqlite3
from sqlite3 import Error

DATABASE_FILE = "my_user.db"


def create_connection():
    """Database connection"""
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def initialize_user_table(connection):
    """Database table"""
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error: {e}")

def insert_user(connection, username, email, password):
    """Function for insterting new user"""
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error: {e}")

def get_user_by_email(connection, email):
    """funtion for getting usser email"""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        user = cursor.fetchone()
        cursor.close()

        if user:
            user_data = {
                "id": user[0],
                "username": user[1],
                "email": user[2],
                "password": user[3]
            }
            return user_data
        else:
            return None
    except Error as e:
        print(f"Error: {e}")
        return None

