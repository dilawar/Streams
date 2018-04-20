import Stream
import math
import random
import numpy as np

def test_mean( ):
    s = Stream.Stream( )
    xs = [ ]
    for i in range(10000):
        x = random.random()*10-5
        s.add(x)
        xs.append(x)
    assert np.isclose(s.mean,sum(xs)/len(xs)), s.mean-sum(xs)/len(xs)


def main( ):
    test_mean()

if __name__ == '__main__':
    main()
