import requests

def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

session = get_tor_session()
tor_response = session.get("http://httpbin.org/ip")
normal_response = requests.get("http://httpbin.org/ip")

# IP visible through Tor
print('IP through Tor: ', tor_response.text)

# Following prints your normal public IP
print('IP without Tor: ', normal_response.text)

print('--------------------------------------')

print('Elapsed time using Tor: ', tor_response.elapsed.total_seconds())
print('Elapsed time without Tor: ', normal_response.elapsed.total_seconds())

print('--------------------------------------')

print(tor_response.status_code)
print(normal_response.is_redirect)