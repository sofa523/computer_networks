import subprocess
import csv


domains = ['google.com', 'ya.ru', 'vk.com', 'bbc.com', 'x.com']

results = []
for domain in domains:
    ipsv4 = subprocess.run(['dig', '+short', domain], capture_output=True, text=True)
    ips = ipsv4.stdout.strip().split('\n')

    result = subprocess.run(['traceroute', '-n', '-m', '15', ips[0]], capture_output=True, text=True)
    results.append({'domain': domain, 'ip': ips[0], 'traceroute': result.stdout})

with open('task_10.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['domain', 'ip', 'traceroute'])
    writer.writeheader()
    writer.writerows(results)