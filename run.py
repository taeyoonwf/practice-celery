from tasks import add
import time

results = [add.apply_async(args=[4, i]) for i in range(30)]
done_count = 0
while done_count < len(results):
    time.sleep(1)
    done_count = [res.ready() for res in results].count(True)
    print(f'{done_count}/{len(results)}')