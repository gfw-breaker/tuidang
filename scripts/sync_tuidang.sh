#!/bin/bash
# author: gfw-breaker

channels="nf3104"

cd /tuidang/scripts

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

base_url="https://github.com/gfw-breaker/tuidang/blob/master"
for d in $(ls ../pages/); do
    for f in $(ls -t ../pages/$d | grep 'md$'); do
		a_path="../pages/$d/$f"
		a_url="$base_url/pages/$d/$f"
		if [ ! -f $a_path.png ]; then
			echo $a_path
			echo $a_url
			qrencode -o $a_path.png -s 4 $a_url
		fi
    done
done

git pull
git add ../pages/
git push
