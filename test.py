from pyadwin import Adwin

#Delta's standard of 0.01 , but Adwin builder can receive a floating point as the delta parameter.
adwin = Adwin()

data_stream = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.7]

for data in data_stream:
  if (adwin.update(data)):
    print "Change has been detected in data: "+str(data)
  print adwin.getEstimation() # Prints the next value of the estimated form of data_stream
