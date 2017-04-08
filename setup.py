#!/usr/bin/python

import os
import sqlite3
from datetime import datetime

PATH = os.getcwd()
datadir = os.getcwd() + os.sep + 'data' + os.sep
if not os.path.exists(datadir + 'pomodoro.db'):
    if not os.path.exists(datadir):
        os.mkdir('data')

    conn = sqlite3.connect(datadir + 'pomodoro.db')
    cur = conn.cursor()

    # create table userdata
    cur.execute('''
        CREATE TABLE userdata (yesterday_streak int, streak int, reset_time text)
    ''')

    cur.execute("INSERT INTO userdata VALUES (?, ?, ?)", (0, 0, datetime.now().strftime("%Y-%m-%dT%H:%M")))

    conn.commit()
    conn.close()
