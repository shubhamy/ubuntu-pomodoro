#!/usr/bin/python

import os
import sqlite3
from datetime import datetime
import time

PATH = os.getcwd()
datadir = os.getcwd() + os.sep + 'data' + os.sep
if not os.path.exists(datadir + 'pomodoro.db'):
    if not os.path.exists(datadir):
        os.mkdir('data')

    conn = sqlite3.connect(datadir + 'pomodoro.db')
    cur = conn.cursor()

    # create table userdata
    cur.execute('''
        CREATE TABLE userdata (datestamp text, streak int)
    ''')

    cur.execute("INSERT INTO userdata VALUES (?, ?)", (datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), 0,))
    cur.execute("INSERT INTO userdata VALUES (?, ?)", ('current', 0,))

    conn.commit()
    conn.close()
