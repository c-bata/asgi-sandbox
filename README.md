# asgi-sandbox


```
$ ab -n 10 -c 5 http://127.0.0.1:8000/sync/
This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /sync/
Document Length:        18 bytes

Concurrency Level:      5
Time taken for tests:   10.057 seconds
Complete requests:      10
Failed requests:        0
Total transferred:      1830 bytes
HTML transferred:       180 bytes
Requests per second:    0.99 [#/sec] (mean)
Time per request:       5028.514 [ms] (mean)
Time per request:       1005.703 [ms] (mean, across all concurrent requests)
Transfer rate:          0.18 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       1
Processing:  1010 3621 1713.9   5015    5031
Waiting:     1009 3620 1714.0   5015    5031
Total:       1010 3621 1713.8   5015    5031

Percentage of the requests served within a certain time (ms)
  50%   5015
  66%   5016
  75%   5019
  80%   5019
  90%   5031
  95%   5031
  98%   5031
  99%   5031
 100%   5031 (longest request)
```

```
$ ab -n 10 -c 5 http://127.0.0.1:8000/
This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /
Document Length:        19 bytes

Concurrency Level:      5
Time taken for tests:   3.054 seconds
Complete requests:      10
Failed requests:        0
Total transferred:      1840 bytes
HTML transferred:       190 bytes
Requests per second:    3.27 [#/sec] (mean)
Time per request:       1527.203 [ms] (mean)
Time per request:       305.441 [ms] (mean, across all concurrent requests)
Transfer rate:          0.59 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:  1013 1020   2.6   1021    1022
Waiting:     1012 1020   2.8   1021    1022
Total:       1013 1020   2.7   1021    1023

Percentage of the requests served within a certain time (ms)
  50%   1021
  66%   1021
  75%   1021
  80%   1021
  90%   1023
  95%   1023
  98%   1023
  99%   1023
 100%   1023 (longest request)
```