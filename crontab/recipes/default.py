from kokki import *

Package("cron")

'''
Example Usage:

CronJob("creating a cron job that runs every fifteen minutes",
    minute='0,15,30,45',
    user='root',
    command='echo "Hello World!"')
'''
