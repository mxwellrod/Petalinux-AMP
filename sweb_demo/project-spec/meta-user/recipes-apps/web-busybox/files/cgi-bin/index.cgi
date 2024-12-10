#!/bin/sh

#
# Working principle of CGI script:
# 1) Webserver(busybox) detect script as an executable(bin/sh)
# 2) Receive a request, runs script, and take script html output
# 3) Browser interprets HTML code and show it as a web page
#

# 1: HTTP header ending with a blank line
printf "Content-type: text/html\r\n\r\n"

# Webserver information using system commands
sys_host=$(hostname)
sys_time=$(date)
sys_load=$(awk '{print $1}' /proc/loadavg)
sys_up=$(awk '{print $1}' /proc/uptime)
cpu_model=$(grep model /proc/cpuinfo | cut -d : -f2 | tail -1 | sed 's/\s//')
cpu_cores=$(grep -c ^processor /proc/cpuinfo)
mem_total=$(free -m | awk 'NR==2{print $2}')
mem_used=$(free -m | awk 'NR==2{print $3}')
mem_free=$(free -m | awk 'NR==2{print $4}')
net_mac=$(cat /sys/class/net/eth0/address)
net_ip_loc=$(ip a | grep inet | grep -vw lo | grep -v inet6 | cut -d \/ -f1 | sed 's/[^0-9\.]*//g')
net_ip_ext=$(wget -q -O- http://ipecho.net/plain)

# print HTML document with server data

printf '<!DOCTYPE html>'
printf '<html lang="en">'
printf '<head>'
printf '<meta http-equiv="content-type" content="text/html; charset=UTF-8">'
printf '<title>Zybo webserver</title>'
printf '</head>'

printf '<body>'
printf 'Hello from your Zybo webserver...'
printf '<br>'
printf '<img src="../zybo.png" alt="Missing Image!">'

# Server info
printf '<br>System<br>'
printf 'Hostname: %s<br>' "${sys_host}"
printf 'Time: %s<br>' "${sys_time}"
printf 'Uptime: %.2f seconds<br>' ${sys_up}

printf '<br>CPU<br>'
printf 'Model: %s<br>' "${cpu_model}"
printf 'Cores: %d<br>' ${cpu_cores}
printf 'Load: %.2f<br>' ${sys_load}

printf '<br>Memory<br>'
printf 'Total: %d Mb<br>' ${mem_total}
printf 'Used: %d Mb<br>' ${mem_used}
printf 'Free: %d Mb<br>' ${mem_free}

printf '<br>Network<br>'
printf 'MAC Address: %s<br>' "${net_mac}"
printf 'Local IP: %s<br>' "${net_ip_loc}"
printf 'External IP: %s<br>' "${net_ip_ext}"


printf '</body>'
printf '</html>'


