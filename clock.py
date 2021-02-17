"""Cron job for tweeting"""

from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()
scheduler.add_job(lambda: print("This job is run every minute"), "cron", minute=1)


@sched.scheduled_job('interval', seconds=30)
def timed_job():
    print('This job is run every 30 seconds.')


@sched.scheduled_job('cron', minute=2)
def timed_job():
    print('This job is run every 2 minutes.')


scheduler.start()
