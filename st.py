import sys, time, io, requests, json

def speed_test(size=5, ipv="ipv4", port=80, tor=False):
 
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
        if total_length is None: # no content length header
            f.write(r.content)
        else:
            for chunk in r.iter_content(1024):
                dl += len(chunk)
                f.write(chunk)
                done = int(30 * dl / int(total_length))
                sys.stdout.write("\r[%s%s] %s Mbps" % ('=' * done, ' ' * (30-done), dl//(time.perf_counter() - start) / 100000))

    return time.perf_counter() - start

sizes = [1, 2, 5, 10, 20, 30, 40, 50, 100, 200, 512, 1024]

res = {}
"""
print('\n')
for size in sizes[:2]:
    n = speed_test(size)
    t = speed_test(size, tor=True)
    
    res[size] = (n,t)

with open('results.json', 'w') as outfile:
    json.dump(res, outfile)
"""
speed_test(10, tor = True)