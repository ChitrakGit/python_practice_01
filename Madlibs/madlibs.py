from samples_madlib import code,hp,hungergames,zombie
import random

if __name__ == '__main__':
    madlibs = random.choice([code,hp,hungergames,zombie])
    madlibs.madlib()