#!/bin/bash

function crawl {
	echo "$2" > $1.md
	echo "=" >> $1.md
	scrapy crawl $1 -t md -o $1.md
}

crawl "ericlippert_msdn" "Eric Lippert (MSDN)"