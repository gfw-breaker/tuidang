#!/bin/bash
# author: gfw-breaker

channels="nf3104"

## create dirs
for channel in $channels ; do
	mkdir -p ../pages/$channel
done
	
## get feeds files
for channel in $channels ; do
	url="http://epochtimes.com/gb/$channel.htm"
	echo "getting channel: $url"
	python parse_tuidang.py $channel "$url"
done


