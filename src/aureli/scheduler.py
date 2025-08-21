import time

def loop_every(seconds: int):
    next_t = time.time()
    while True:
        now = time.time()
        if now >= next_t:
            yield
            next_t = now + seconds
        else:
            time.sleep(min(1, next_t - now))
