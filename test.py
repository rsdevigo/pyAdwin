from pyadwin import Adwin

# Delta's standard of 0.01 , but Adwin builder can receive a floating point as the delta parameter.
adwin = Adwin(0.01)

data_stream = [1] * 30
data_stream.extend([2] * 15)

for data in data_stream:
    if (adwin.update(data)):
        print "Change has been detected in data: " + str(data)
    print adwin.getEstimation()  # Prints the next value of the estimated form of data_stream
