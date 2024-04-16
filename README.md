# cyphercon2024_badge_serial
Reverse engineering the badge serial protocol

hyr0n likes emacs.

i do not

EvilMog Likes Nano

# Tools
|tool|purpose|syntax|
|---|---|---|
|badge_score.py|calculates the badge id's to send to a badge to get an arbitrary score|python3 badge_score.py|
|badge2.py|spams badge ids to a badge|python3 badge2.py 'serialport' --delay 500 badge_start badge_end|
|badge3.py|spams a csv list of badge ids to a badge|python3 badge3.py --delay 500 'serialport' '1,2,3'|
|badge_trade7.py|spoofs trades to make a badge green|python3 badge_trade7.py --port 'serialport' --local_id 11 --local_item=23|
|badge_checksum.py|calculates the badge checksum for the firmware files|use output in .hex file|

# badge firmware
inside the firmware file you will find a line such as `:020000005200ac` replace that line with the output of the badge_checksum.py file, you can write the badge firmware with pickitminus and a clone pickit 3 or pickit 3.5. This allows you to set a badge ID

# Badge ID Ranges
|range|type|value|
|---|---|---|
|0 - 537|general|10|
|538 - 613|VIP|20|
|614 - 699|Speaker|100|
|700 - 730|Vendor|1000|
|731 - 756|Founder|10000|
|757 - 767|Lifetime|100000|
