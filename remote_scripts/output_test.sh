#!/bin/bash

homesec="pi@the.ip.address"

ssh $homesec python gpio_status.py 2>/dev/null > /tmp/before.txt

while true ; do
	sleep 0.5
	ssh $homesec python gpio_status.py 2>/dev/null > /tmp/now.txt
	diff /tmp/before.txt /tmp/now.txt > /tmp/diff.txt
	output=$(cat /tmp/diff.txt | wc -l)
	if [ $output -ne 0 ] ; then
		diff_pin=$(grep Pin /tmp/diff.txt | sed 's/^.*Pin/Pin/' | head -n 1 | awk '{print tolower($0)}')
		echo $diff_pin
		espeak -a 200 "$diff_pin"
		sleep 1
	fi
done
