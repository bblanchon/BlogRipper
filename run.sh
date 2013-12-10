echo "All Eric Lippert's posts" > ericlippert.md
echo "=" >> ericlippert.md
scrapy crawl ericlippert -t md -o ericlippert.md
