# cyphercon2024_badge_serial
Reverse engineering the badge serial protocol

hyr0n likes emacs.

i do not

EvilMog Likes Nano

Gigawatts Likes VIM

# Tools
|tool|purpose|syntax|
|---|---|---|
|badge_score.py|calculates the badge id's to send to a badge to get an arbitrary score|python3 badge_score.py|
|badge2.py|spams badge ids to a badge|python3 badge2.py 'serialport' --delay 500 badge_start badge_end|
|badge3.py|spams a csv list of badge ids to a badge|python3 badge3.py --delay 500 'serialport' '1,2,3'|
|badge_trade7.py|spoofs trades to make a badge green|python3 badge_trade7.py --port 'serialport' --local_id 11 --local_item=23|
|badge_checksum.py|calculates the badge checksum for the firmware files|use output in .hex file|
|badge_info.py|Prints out your badge's ID, Type and Item number|python3 badge_info.py --port 'serialport'

# badge firmware
inside the firmware file you will find a line such as `:020000005200ac` replace that line with the output of the badge_checksum.py file, you can write the badge firmware with pickitminus and a clone pickit 3 or pickit 3.5. This allows you to set a badge ID

Badge ID 252 triggers a magic random number seed that always displays the easter egg `F33db0b0` message on power up. Trade some points with another badge to trigger this flag.

# Badge ID Ranges
|range|type|value|
|---|---|---|
|0 - 537|general|10|
|538 - 613|VIP|20|
|614 - 699|Speaker|100|
|700 - 730|Vendor|1000|
|731 - 756|Founder|10000|
|757 - 767|Lifetime|100000|

# Example Run

First calculate your path from your existing score to the score you want
```
$ python3 badge_score.py
Enter the current score on the scoreboard: 50
Enter the badge ID that cannot be used: 82
Enter a comma-separated list of badge IDs already used, or press enter for none:
Enter the target score you wish to reach: 800850
Debugging Info:
(767, 100000)
(766, 100000)
(765, 100000)
(764, 100000)
(763, 100000)
(762, 100000)
(761, 100000)
(760, 100000)
Total for 100000 point badges: 800000
(699, 100)
(698, 100)
(697, 100)
(696, 100)
(695, 100)
(694, 100)
(693, 100)
(692, 100)
Total for 100 point badges: 800
Overall total: 800800
New badges needed to reach the target score: 767,766,765,764,763,762,761,760,699,698,697,696,695,694,693,692
```

Next spam that to the badge
```
$ python3 badge3.py --delay 500 '/dev/cu.usbserial-TG1101910' '767,766,765,764,763,762,761,760,699,698,697,696,695,694,693,692'
Sent packet to badge ID: 767
Sent packet to badge ID: 766
Sent packet to badge ID: 765
Sent packet to badge ID: 764
Sent packet to badge ID: 763
Sent packet to badge ID: 762
Sent packet to badge ID: 761
Sent packet to badge ID: 760
Sent packet to badge ID: 699
Sent packet to badge ID: 698
Sent packet to badge ID: 697
Sent packet to badge ID: 696
Sent packet to badge ID: 695
Sent packet to badge ID: 694
Sent packet to badge ID: 693
Sent packet to badge ID: 692
```

This will give you an arbitrary score
