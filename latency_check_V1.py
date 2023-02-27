from tcp_latency import measure_latency
from influxdb import InfluxDBClient
import influxdb
import subprocess, sys
import os
import re

os.chdir("/AUTOMATION/LATENCY-CHECK")
urlss = open('urls.txt')

for url in urlss:
    #latency = measure_latency(host=url)
    #measure_latency(host=url, port=443)
    url = url.strip() # Remove trailing newline character
    latencyd = measure_latency(host=url, port=443)
    print(url)
    print(latencyd)
    #latencys = latencyd.strip("[]")
    latencys = str(latencyd)[1: -1]
    print(latencys)
    try:

        connect = InfluxDBClient(host='localhost',
                               port=8086)
                                #username='admin',
                                #password='password'
        line = "Latency,domain=" + str(url) + " latency=" + str(latencys)
        #line = "Latency,domain=" + str(url) + " latency=" + str(latencyd[0]).strip('[]')
        #line = "Latency,domain=" + str(url) + " latency=" + str(latencyd[0])
        print(line)
        connect.write([line], {'db': 'LATENCYCHECK'}, 204, 'line')
        connect.close()
    except influxdb.exceptions.InfluxDBClientError:
        print("No data")
