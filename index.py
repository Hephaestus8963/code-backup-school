from Lib.Pokemon import Pickachu
import time


starter = Pickachu()

for i in range(25):
    starter.feed()
    time.sleep(5)
