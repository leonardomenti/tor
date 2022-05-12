# An evaluation of TOR

![tor](./images/tor-logo.jpg)

## TODO
- (Jorre) Tor vs normal connection using different amount of data [1, 2, 5, 10, ...]
- (Leo) Stability of Tor: return  (time, Mbps) : (time, dl//(time.perf_counter() - start) / 100000)
- (Jorre) Avarage time of sending packets - histogram

- AWS ec2 instance (we want to run the code from different countries to see where the tor infrastructure is better)
- How to Set a Specific Country in a Tor Browser: https://www.wikihow.com/Set-a-Specific-Country-in-a-Tor-Browser

## Authors

- **Leonardo Menti**
- **Jorre De Backer**

## Introduction

Tor (The Onion Router) is a free and open source software that provide
anonymous communication over the internet. It is based on the onion routing
protocol, an anonymization technique of communications in a 
telecommunications network.


## What you need

`brew install tor`

`pip install 'requests[socks]'`
