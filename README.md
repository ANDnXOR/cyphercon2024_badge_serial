# cyphercon2024_badge_serial
Reverse engineering the badge serial protocol

hyr0n likes emacs.

i do not

# Tools
|tool|purpose|syntax|
|---|---|---|
|badge_score.py|this calculates the badge id's to send to a badge to get an arbitrary score|python3 badge_score.py|
|badge2.py|this spams badge ids to a badge|python3 badge2.py '/dev/cu.usbserial-TG1101910' --delay 500 badge_start badge_end|
|badge3.py|this spams a csv list of badge ids to a badge|python3 badge3.py --delay 500 '/dev/cu.usbserial-TG1101910' '767,766,765,764,763,762,761,760,699,698,697,696,695,694,693,692'|
|badge_trade7.py|this tool facilitates trades to make a badge green|python3 badge_trade7.py --port '/dev/cu.usbserial-TG1101910' --local_id 11 --local_item=23|
