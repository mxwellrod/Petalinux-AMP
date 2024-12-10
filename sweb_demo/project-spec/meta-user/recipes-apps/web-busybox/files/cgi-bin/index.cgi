#!/bin/sh

#
# Working principle of CGI script:
# 1) Webserver(busybox) detects script as an executable(bin/sh)
# 2) Receives a request, runs the script, and sends the script's HTML output
# 3) Browser interprets HTML and shows it as a webpage
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

# Print HTML document with server data

printf '<!DOCTYPE html>\n'
printf '<html lang="en">\n'
printf '<head>\n'
printf '<meta http-equiv="content-type" content="text/html; charset=UTF-8">\n'
printf '<title>Zybo WebServer</title>\n'
printf '<link rel="stylesheet" href="style.css">\n'
printf '</head>\n'

printf '<body>\n'
printf '<h1>Hello from your Zybo WebServer...</h1>\n'
printf '<img src="../zybo.png" alt="Missing Image">\n'

# Server info - Use a structured <dl> for better styling
printf '<div class="server-info">\n'
printf '<dl>\n'

# System Info
printf '<dt>System</dt>\n'
printf '<dd>Hostname: %s</dd>\n' "${sys_host}"
printf '<dd>Time: %s</dd>\n' "${sys_time}"
printf '<dd>Uptime: %.2f seconds</dd>\n' ${sys_up}

# CPU Info
printf '<dt>CPU</dt>\n'
printf '<dd>Model: %s</dd>\n' "${cpu_model}"
printf '<dd>Cores: %d</dd>\n' ${cpu_cores}
printf '<dd>Load: %.2f</dd>\n' ${sys_load}

# Memory Info
printf '<dt>Memory</dt>\n'
printf '<dd>Total: %d Mb</dd>\n' ${mem_total}
printf '<dd>Used: %d Mb</dd>\n' ${mem_used}
printf '<dd>Free: %d Mb</dd>\n' ${mem_free}

# Network Info
printf '<dt>Network</dt>\n'
printf '<dd>MAC Address: %s</dd>\n' "${net_mac}"
printf '<dd>Local IP: %s</dd>\n' "${net_ip_loc}"
printf '<dd>External IP: %s</dd>\n' "${net_ip_ext}"

printf '</dl>\n'
printf '</div>\n'

printf '</body>\n'
printf '</html>\n'



