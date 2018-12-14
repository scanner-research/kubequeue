from celery import group
from tasks import app
import json
from tqdm import tqdm
import time
import argparse

from tasks import add_one
TASK = add_one
ARGS = [(i,) for i in range(10)]

parser = argparse.ArgumentParser()
parser.add_argument('--result-id')
args = parser.parse_args()

if args.result_id is not None:
    group_result = app.GroupResult.restore(args.result_id)
else:
    job = group([TASK.s(*args) for args in ARGS])
    group_result = job.apply_async()
    group_result.save()
    print('Result ID: {}'.format(group_result.id))

bar = tqdm(total=len(ARGS))
completed = 0
while not group_result.ready():
    new_completed = group_result.completed_count()
    if new_completed > completed:
        bar.update(new_completed - completed)
        completed = new_completed
    else:
        time.sleep(1.0)

outputs = group_result.get()
print(outputs)

print('Done!')
