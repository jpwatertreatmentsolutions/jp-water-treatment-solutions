#!/bin/sh
# Usage: ./set-domain.sh https://www.yourdomain.com
# Replaces the placeholder domain in canonicals, Open Graph, structured data, sitemap and robots.txt.
[ -z "$1" ] && echo "Usage: $0 https://www.yourdomain.com" && exit 1
D="${1%/}"
grep -rl "https://YOUR-DOMAIN.com" --include=*.html --include=*.xml --include=*.txt . | xargs sed -i "s#https://YOUR-DOMAIN.com#$D#g"
echo "Domain set to $D"
