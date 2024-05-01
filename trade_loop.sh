#!/bin/bash

## Badge ID 252, by default, has items 0,6,8,12,21 with 21 being its sticky item
## This script loops through the badge trade script to trade for every missing item

for n in {1..5} 7 {9..11} {13..23}
do
echo $n
python badge_trade7.py --port /dev/ttyUSB0 --local_id 11 --local_item $n; done
done
