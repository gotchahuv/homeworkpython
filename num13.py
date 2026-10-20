print('номер 13')
import time
class timer:
    def __enter__(self):
        self.start=time.perf_counter()
        return self
    def __exit__(self,
        exc_type,
        exc_value,
        exc_tb):
        end=time.perf_counter()
        print('Время',end-self.start)
with timer() as t:
    total=0
    for i in range(10000000):
        None
from contextlib import contextmanager
@contextmanager
def timer():
    start=time.perf_counter()
    yield
    end=time.perf_counter()
    print('Время',end-start)
with timer() as t:
    total=0
    for i in range(10000000):
        total+=i