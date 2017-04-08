import os

PATH = os.getcwd()
datadir = os.getcwd() + os.sep + 'data' + os.sep
if not os.path.exists(datadir + 'log.db'):
    if not os.path.exists(datadir):
        os.mkdir('data')

    f = open(datadir + 'log.db', 'w+')
    f.close()
