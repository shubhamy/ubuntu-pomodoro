#!/usr/bin/python

import os, subprocess
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

"""
Creating .desktop file
"""

if not os.path.exists(PATH + os.sep + 'ubuntu-pomodoro.desktop'):
    with open('ubuntu-pomodoro.desktop', 'w+') as f:
        text = "[Desktop Entry]" + "\n" \
                "Version=1.0" + "\n" \
                "Name=Ubuntu Pomodoro" + "\n" \
                "Exec={0}/main.py" + "\n" \
                "Path={0}/" + "\n" \
                "Icon={0}/icons/icon.png" + "\n" \
                "Terminal=false" + "\n" \
                "Type=Application" + "\n" \
                "Categories=Utility;"
        f.write(text.format(PATH))
    f.close()
    os.system("chmod +x ubuntu-pomodoro.desktop")
