import io
import sys
import time
import requests
import matplotlib.pyplot as plt

def stability(size=5, ipv="ipv4", port=80, tor=False):
 
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
            mbps = []
            t = []
            xlim = 0
            for chunk in r.iter_content(1024):
                dl += len(chunk)
                f.write(chunk)
                done = int(30 * dl / int(total_length))

                elapsed_time = time.perf_counter() - start
                current_mbps = dl//(elapsed_time)/100000

                sys.stdout.write("\r[%s%s] %s Mbps" % ('=' * done, ' ' * (30-done), current_mbps))
                mbps.append(current_mbps)
                t.append(elapsed_time)
                xlim = elapsed_time

            if (tor):
                plt.plot(t, mbps, "-r", label="tor")
            else:
                fig = plt.figure()
                plt.plot(t, mbps, "-b", label="normal connection")
                fig.suptitle(size, fontsize=20)
            plt.xlabel('Time')
            plt.ylabel('Mbps')
            plt.legend(loc="upper left")
            ax = plt.gca()
            ax.set_xlim([0, xlim+0.5])
            #ax.set_ylim([ymin, ymax])
            if (tor):
                plt.show()

    return time.perf_counter() - start

sizes = [1, 2, 5, 10, 20, 30, 40, 50, 100, 200, 512, 1024]

res = {}

for size in sizes:
    stability(size)
    stability(size, tor = True)
    