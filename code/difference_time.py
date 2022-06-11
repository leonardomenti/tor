import io
import sys
import time
import requests
import matplotlib.pyplot as plt, numpy as np

def time_diff(size=5, ipv="ipv4", port=80):
 
    if size == 1024:
        size = "1GB"
    else:
        size = f"{size}MB"

    url = f"http://{ipv}.download.thinkbroadband.com:{port}/{size}.zip"
    
    print('\nConnecting to: ', url)
    print('*** TOR ***')
    print('Size: ', size)

    with io.BytesIO() as f:
        start = time.perf_counter()
        
        session = requests.session()
        session.proxies = {
            'http':  'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'
        }
        r = session.get(url, stream=True)

        total_length = r.headers.get('content-length')
        dl = 0
        if total_length is None: # no content length header
            f.write(r.content)
        else:
            for chunk in r.iter_content(1024):
                dl += len(chunk)
                f.write(chunk)
                done = int(30 * dl / int(total_length))

                elapsed_time = time.perf_counter() - start
                current_mbps = dl//(elapsed_time)/100000

                sys.stdout.write("\r[%s%s] %s Mbps" % ('=' * done, ' ' * (30-done), current_mbps))

    print('\nTime: ', time.perf_counter() - start, '\n')

    return time.perf_counter() - start

times = []

for i in range(100):
    times.append(time_diff(10))

# binning
times = np.array(times)
q25, q75 = np.percentile(times, [25, 75])
bin_width = 2 * (q75 - q25) * len(times) ** (-1/3)
bins = round((times.max() - times.min()) / bin_width)

# plotting
fig = plt.figure()
fig.suptitle('Difference of time', fontsize=20)   
plt.hist(times, bins=bins, facecolor='blue', alpha=0.5, label="tor", histtype='bar', ec='black', density=False, range=(times.min(), times.max()))

plt.xlabel('Time')
plt.ylabel('Frequency')
plt.legend(loc="upper left")
plt.show()
