#!/bin/bash

set -e

if [ $1 = 'beat' ]; then
    celery -A celery_app.app beat
elif [ $1 = 'worker' ]; then
    celery -A celery_app.app worker
elif [ $1 = 'flower' ]; then
    flower -A celery_app.app --port=5555 --persistent=True --db="${BADC_FLOWER_DB:-/opt/tmp/flower.db}" --state_save_interval=5
elif [ $1 = 'webapp' ]; then
    gunicorn -b :5000 --worker-class sync run:app
else
    celery -A celery_app.app worker -B
fi