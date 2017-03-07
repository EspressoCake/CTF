#!/usr/bin/env python

from pwn import *

r = remote("ctf.crikeycon.com", 23776)

log.info("Solving. Please wait for the flag!")

while True:
    data = r.recv(1024)
    if "{" in data:
        log.info(data.split("\n")[1])
        r.close()
        break
    elif "correct" in data:
        continue
    else:
        evaluation = eval(''.join(data.split()[2:5]))
        r.send(str(evaluation))
