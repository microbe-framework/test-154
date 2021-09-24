################################################################################

import psutil
import sys
import logging

from apscheduler.schedulers.blocking import BlockingScheduler

################################################################################

print("hello world")
sys.stdout.flush()

#print(psutil.pids())
for proc in psutil.process_iter(['pid', 'name', 'username']):
    print(proc.info)

################################################################################

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=15)
def timed_job_15s():
    text = 'This job is run every fifteen seconds.'
    print(text)
    logging.debug(text)

@sched.scheduled_job('interval', minutes=3)
def timed_job_3m():
    text = 'This job is run every three minutes.'
    print(text)
    logging.debug(text)

#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
@sched.scheduled_job('cron', hour=17)
def scheduled_job():
    text = 'This job is run every weekday at 5pm.'
    print(text)
    logging.debug(text)


sched.start()

################################################################################