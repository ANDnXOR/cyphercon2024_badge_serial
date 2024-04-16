# cyphercon2024_badge_serial
Reverse engineering the badge serial protocol

hyr0n likes emacs.

i do not

# Tools
|tool|purpose|syntax|
|---|---|---|
|badge_score.py|calculates the badge id's to send to a badge to get an arbitrary score|python3 badge_score.py|
|badge2.py|spams badge ids to a badge|python3 badge2.py 'serialport' --delay 500 badge_start badge_end|
|badge3.py|spams a csv list of badge ids to a badge|python3 badge3.py --delay 500 'serialport' '1,2,3'|
|badge_trade7.py|spoofs trades to make a badge green|python3 badge_trade7.py --port 'serialport' --local_id 11 --local_item=23|
