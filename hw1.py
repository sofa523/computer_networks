import subprocess
import platform
import csv
import re
import statistics


def ping_domain(domen):
    # Определяем параметры в зависимости от ОС
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '4', domen]

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True, encoding='cp866')
        # print(output)

        # Парсим IP-адрес
        ip_match = re.search(r'\[?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\]?', output)
        ip = ip_match.group(1) if ip_match else "N/A"

        # Парсим TTL из первой строки ответа
        ttl_match = re.search(r'TTL=(\d+)', output, re.IGNORECASE)
        ttl = ttl_match.group(1) if ttl_match else "N/A"

        # Парсим все времена ответов
        time_matches = re.findall(r'время[=\s]*(\d+)\s*мс', output, re.IGNORECASE)
        if not time_matches:
            time_matches = re.findall(r'time[=<\s]*(\d+)\s*ms', output, re.IGNORECASE)

        rtt_times = []
        if time_matches:
            rtt_times = [int(t) for t in time_matches]
            avg_rtt = statistics.mean(rtt_times)
        else:
            avg_rtt = "N/A"

        # Парсим потерю пакетов
        loss_match = re.search(r'(\d+)%\s+потерь', output)
        if not loss_match:
            loss_match = re.search(r'(\d+)%\s+loss', output, re.IGNORECASE)
        loss = loss_match.group(1) + "%" if loss_match else "0%"

        # Определяем статус
        status = "Up" if loss == "0%" and avg_rtt != "N/A" else "Down"

        return [domen, ip, avg_rtt, ttl, loss, status]

    except Exception as e:
        return [domen, "Error", "N/A", "N/A", "100%", "Down"]


domains = [
    "google.com", "yandex.ru", "github.com", "cloudflare.com",
    "apple.com", "wikipedia.org", "microsoft.com", "vk.com",
    "amazon.com", "reddit.com"
]

header = ["Domain", "IP Address", "Avg RTT (ms)", "TTL", "Packet Loss", "Status"]

# Сохранение в CSV
with open('ping_results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for domain in domains:
        print(domain)
        result = ping_domain(domain)
        writer.writerow(result)
        print(f"Результат: {result}")

print("\nРезультаты сохранены в файл 'ping_results.csv'")
