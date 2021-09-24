################################################################################

import psutil
import sys
import logging

from apscheduler.schedulers.blocking import BlockingScheduler

################################################################################

ps_count_initial = 0

def ps_print():
#   print(psutil.pids())
    ps_count = 0
    print('[*] Processes')
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print(proc.info)
        ps_count += 1
    print('[*] Total:', ps_count)
    print()
    return ps_count

def log_print(text):
    print(text)
    logging.debug(text)

################################################################################

print("Hello world!")
sys.stdout.flush()

ps_count_initial = ps_print()

################################################################################

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=15)
def timed_job_15s():
    log_print('This job is run every fifteen seconds.')
    ps_current = ps_print()
    if ps_current > ps_initial:
        return
    os.system("python worker.py")

@sched.scheduled_job('interval', minutes=3)
def timed_job_3m():
    log_print('This job is run every three minutes.')

#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
@sched.scheduled_job('cron', hour=17)
def scheduled_job():
    log_print('This job is run every weekday at 5pm.')


sched.start()

################################################################################