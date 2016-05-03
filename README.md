# pyAdwin

ADWIN is an adaptive sliding window algorithm for detecting change and keeping updated statistics from a data stream, and use it as a black-box in place or counters in learning and mining algorithms initially not designed for drifting data. [Reference: The Adwin Software](http://adaptive-mining.sourceforge.net/?page_id=20)

Implementation based on C ++ implementations in this repository [Adwin C++](https://github.com/abifet/adwin)

## Prerequisites

* Python > 2.7

## Install

* Clone this repository in your project folder

```
git clone https://github.com/rsdevigo/pyAdwin.git
```

* Access the pyAdwin folder and execute the setup.py

```
cd pyAdwin && sudo python setup.py install
```

## Example

```
from pyadwin import Adwin

#Delta's standard of 0.01 , but Adwin builder can receive a floating point as the delta parameter.
adwin = Adwin()

data_stream = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.7]

for data in data_stream:
  if (adwin.update(data))
    print "Change has been detected in data: "+str(data)
    print adwin.getEstimation() # Prints the next value of the estimated form of data_stream
```
