import io
import sys
import time
import requests
import matplotlib.pyplot as plt

def download_speed(size=5, ipv="ipv4", port=80, tor=False):
    if size == 1024:
        size = "1GB"
    else:
        size = f"{size}MB"

    url = f"http://{ipv}.download.thinkbroadband.com:{port}/{size}.zip"
    
    print('\nConnecting to: ', url)
    if tor:
        print('*** TOR ***')
    print('Size: ', size)

    with io.BytesIO() as f:
        start = time.perf_counter()
        if tor:
            session = requests.session()
            session.proxies = {
                'http':  'socks5://127.0.0.1:9050',
                'https': 'socks5://127.0.0.1:9050'
            }
            r = session.get(url, stream=True)
        else:
            r = requests.get(url, stream=True)

        total_length = r.headers.get('content-length')
        dl = 0
        if total_length is None:
            f.write(r.content)
        else:
            sizes = []
            t = [] 
            xlim = 0
            for chunk in r.iter_content(1024):
                dl += len(chunk)
                f.write(chunk)
                done = int(30 * dl / int(total_length))

                elapsed_time = time.perf_counter() - start
                current_mbps = dl//(elapsed_time)/100000

                sys.stdout.write("\r[%s%s] %s Mbps" % ('=' * done, ' ' * (30-done), current_mbps))

            t.append(time.perf_counter() - start)
            sizes.append(size)

    return time.perf_counter() - start

sizes = [1, 2, 5, 10, 20, 30, 40, 50, 100, 200, 512, 1024]

times = []
times_tor = []

for size in sizes:
    times.append(download_speed(size))
    times_tor.append(download_speed(size, tor = True))

# plotting
fig = plt.figure()
fig.suptitle('Comparison', fontsize=20)   
plt.plot(sizes, times, "-b", label="normal connection")
plt.plot(sizes, times_tor, "-r", label="tor")
plt.xlabel('MB')
plt.ylabel('Time')
plt.legend(loc="upper left")
ax = plt.gca()
plt.xticks(sizes, sizes)
plt.show()
