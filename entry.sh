#!/bin/sh
set -e

htpasswd -bc /etc/nginx/.htpasswd zix "$(cat /run/zix_pass.txt)"
htpasswd -b /etc/nginx/.htpasswd cat "$(cat /run/cat_pass.txt)"

exec nginx -g "daemon off;"