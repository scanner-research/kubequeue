from celery import Celery
import os
import subprocess as sp

if 'MASTER_SERVICE_HOST' in os.environ:
    host = '{}:{}'.format(
        os.environ['MASTER_SERVICE_HOST'], os.environ['MASTER_SERVICE_PORT'])
else:
    ip = sp.check_output(['./master-ip.sh']).decode('utf-8').strip()
    port = sp.check_output(['./master-port.sh']).decode('utf-8').strip()
    host = '{}:{}'.format(ip, port)

redis = 'redis://{}'.format(host)
app = Celery('tasks', broker=redis, backend=redis)
app.conf.tasks_ack_late = True  # For fault tolerance

