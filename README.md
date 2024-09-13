## run backend
> $ docker run -p 6379:6379 -d redis/redis-stack

## run a celery worker with 4 child processes
> $ celery -app tasks worker --concurrency 4 --pool threads --loglevel=INFO

## run example code
> $ python run.py
