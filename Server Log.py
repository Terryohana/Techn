
def most_active_ips(logfile):
    ips = {}
    for line in logfile:
        ip = line.split(',')[2]
        if ip in ips:
            ips[ip] += 1
        else:
            ips[ip] = 1
    sorted_ips = sorted(ips.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_ips[:10]

    