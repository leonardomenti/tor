import sys, time, io, requests

def speed_test(size=5, ipv="ipv4", port=80, tor=False):
    
    if size == 1024:
        size = "1GB"
    else:
        size = f"{size}MB"

    url = f"http://{ipv}.download.thinkbroadband.com:{port}/{size}.zip"
    print(url)

    with io.BytesIO() as f:
        start = time.perf_counter()
        if tor:
            print("### TOR ###")
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

    print( f"\n{size} = {(time.perf_counter() - start):.2f} seconds")


speed_test()
speed_test(10)
speed_test(10, tor=True)
