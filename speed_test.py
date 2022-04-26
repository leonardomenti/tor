import speedtest

def test(s):
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

source = "127.0.0.1:9050"
st = speedtest.Speedtest(source_address=source)
d, u, p = test(st)
st .get_best_server()
print('Test with Tor')
print('Download: {:.2f} Kb/s\n'.format(d / 1024))
print('Upload: {:.2f} Kb/s\n'.format(u / 1024))
print('Ping: {}\n'.format(p))

for i in range(3):
    s = speedtest.Speedtest()
    d, u, p = test(s)
    print('Test #{}\n'.format(i+1))
    print('Download: {:.2f} Kb/s\n'.format(d / 1024))
    print('Upload: {:.2f} Kb/s\n'.format(u / 1024))
    print('Ping: {}\n'.format(p))
