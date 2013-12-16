#!/bin/bash

DIR=output

function crawl {
	SPIDER=$1
	TITLE=$2
	(
		echo "$TITLE"
		echo "="
		date
		echo
		scrapy crawl $SPIDER -t md -o -
		echo
		echo "http://blog.benoitblanchon.fr/"
	) > $DIR/$SPIDER.md
}

crawl "ericlippert_msdn" "Eric Lippert (MSDN)"
crawl "jonskeet" "Jon Skeet"