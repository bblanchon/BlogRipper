#!/bin/bash

DIR=output

function crawl {
	SPIDER=$1
	TITLE=$2
	FILE="$DIR/$SPIDER.md"
	echo "$TITLE" > $FILE
	echo "=" >> $FILE
	scrapy crawl $SPIDER -t md -o $FILE
}

crawl "ericlippert_msdn" "Eric Lippert (MSDN)"
crawl "jonskeet" "Jon Skeet"