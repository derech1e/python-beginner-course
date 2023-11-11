from neu import algo
import time


start = time.time()

algo.ggt(5, 2)

end = time.time()
print(end - start)

start = time.time()

algo.euklid(5, 2)

end = time.time()
print(end - start)

