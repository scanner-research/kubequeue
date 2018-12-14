from celery import group
from tasks import foobar, app
import json
from tqdm import tqdm
import time
import argparse

TASK = foobar
ARGS = [(i,) for i in range(10)]

parser = argparse.ArgumentParser()
parser.add_argument('--result-id')
args = parser.parse_args()

if args.result_id is not None:
    result = app.GroupResult.restore(args.result_id)
else:
    job = group([TASK.s(*args) for args in ARGS])
    result = job.apply_async()
    result.save()
    print('Result ID: {}'.format(result.id))

bar = tqdm(total=len(ARGS))
completed = 0
while not result.ready():
    new_completed = result.completed_count()
    if new_completed > completed:
        bar.update(new_completed - completed)
        completed = new_completed
    else:
        time.sleep(1.0)

print('Done!')
