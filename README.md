# comfyNeedle
Inspired by the phrase "finding needle in a haystack", the Needle project helps answer a question: How can a Raspberry Pi be easily discovered through multiple networks (namely wifi &amp; hotspots)

# Problem statement

Given:
A Raspberry Pi 4 + Bullseye (32-bit) Raspberry Pi OS 
2 network connections: wifi connection #1 (wlan0) & hotspot connection #2 (wlan1)

Question:
How to do it so that, accross the 2 networks, there exists a universal identification that allows for ease of SSH connection establishment with 100% reliability

# Approach 1 - static IP

An ip address has a form of A.B.C.D (A to D being number from 0-255)
On a network, all connected devices tend to have the same first 3 numbers (A.B.C being the same)
D is the differentiating factor

[read more about this](https://docs.oracle.com/cd/E19683-01/806-4075/ipref-1/index.html)

Currently, on wlan0, all devices have ip the form of 10.0.0.x

Following [Tom's hardware](https://www.tomshardware.com/how-to/static-ip-raspberry-pi), Raspberry Pi static ip can be set. Here are some interesting behaviors:

1. When setting static ip, ip address will remain accross all networks (wlan0 and wlan1). 

2. If the static IP has the first 3 numbers (10.0.0) matching the router's ip, SSH connection is successful. If not, Raspberry Pi connection cannot be discovered by other devices -> no SSH established. However, web browsing on RPi is possible in both cases.

Edge case discovered: if a static IP is set for wlan0, it will also be applied for wlan1, causing SSH failure on wlan1.

Potential solution: Setting the last digit (D in 1.B.C.D) static.

This will work on a small-scale situation where IP overlapping is not likely, but not an industrial setting

Conclusion: not to be pursued unless no other way


