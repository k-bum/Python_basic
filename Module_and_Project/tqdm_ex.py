from tqdm import tqdm
import time

for i in tqdm(range(10000)) :
    if i % 1000 == 0 :
        time.sleep(1)