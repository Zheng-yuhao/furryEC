from celery import Celery
from datetime import timedelta
from celery.schedules import crontab

broker = 'redis://127.0.0.1:6379/1'
backend = 'redis://127.0.0.1:6379/2'
app = Celery(__name__, broker=broker, backend=backend, include=[
    'celery_task.home_banner_tsk1'
])

app.conf.timezone = 'Asia/Shanghai'
app.conf.enable_utc = False


app.conf.beat_schedule = {
    'add-task':{
        'task': 'celery_task.home_banner_tsk1.banner_update',
        'schedule': timedelta(seconds=10),
        # 'args':(300,) # if the function has args.
    }
}

