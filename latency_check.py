from tcp_latency import measure_latency
import os

os.chdir("C:\\Users\\dragon\\Desktop\\Latency-Check")
urlss = open('urls.txt')

for url in urlss:
    #latency = measure_latency(host=url)
    #measure_latency(host=url, port=443)
    url = url.strip() # Remove trailing newline character
    latency = measure_latency(host=url, port=443)
    print(url)
    print(latency)
