Readme file for Collection of Metroplis Activities dataset v1.0

Data File: 
stream.txt

Number of activites: 
6

Activities IDs:
0, Stationary
1, Walking
2, Running
3, Driving
4, Upstairs
5, Downstairs

Sampling Rate:
20Hz (20 samples every 1s)

Data Format Description:
Each line is a piece of time series data. The first value is the activity ID of the time series. The second value is the number of data point N. The rest of the line are the N consecutive data points. Each data point is a tuple of 4 elements (accX, accY, accZ, timestamp). Therefore, each line contains 2+4*N values.

Parsing:
Sample code to parse the data is provided in 'sample.py'.
