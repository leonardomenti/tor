# An evaluation of TOR

![tor](./images/tor-logo.jpg)

## Authors

- **Leonardo Menti**
- **Jorre De Backer**

## Introduction

Tor (The Onion Router) is a free and open source software that provide
anonymous communication over the internet. It is based on the onion routing
protocol, an anonymization technique of communications in a 
telecommunications network.

## TODO
- Tor vs normal connection using different amount of data [1, 2, 5, 10, ...]
- Stability of Tor: return  (time, Mbps) : (time, dl//(time.perf_counter() - start) / 100000)
- AWS ec2 instance (we want to run the code from different countries to see where the tor infrastructure is better)
- how we can use the browser?
## AFTER
- Latency vs number of hops
- 
## What you need

`brew install tor`

`pip install 'requests[socks]'`
