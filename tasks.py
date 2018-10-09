from celery import Celery
import os
import subprocess as sp

if 'MASTER_SERVICE_HOST' in os.environ:
    host = '{}:{}'.format(
        os.environ['MASTER_SERVICE_HOST'], os.environ['MASTER_SERVICE_PORT'])
else:
    host = sp.check_output(['./master-ip.sh']).decode('utf-8').strip()

redis = 'redis://{}'.format(host)
app = Celery('tasks', broker=redis, backend=redis)
