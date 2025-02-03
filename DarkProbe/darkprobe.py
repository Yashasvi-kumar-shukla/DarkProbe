from tech_ennumerator import tech_ennumerator
from scrapper import scrapper
from who_is import who_is
from dns_rec import dns_rec
from injections import injections
from nmapscan import nmapscan
from vulnerabilities import vulnerabilities
import socket


def get_ip(target):
    try:
        ip = socket.gethostbyname(target)
        print(f"Resolved {target} to {ip}")
        return ip
    except socket.gaierror:
        print(f"Could not resolve {target}")
        return None


def run_recon_and_scan(target):
    print("[+] Running WHOIS Lookup...")
    whois_info = who_is.get_whois_info(target)
    print(whois_info)

    print("[+] Fetching DNS Records...")
    dns_records = dns_rec.get_dns_records(target)
    print(dns_records)

    print("[+] Scanning Open Ports...")
    ip = get_ip(target)
    open_ports = nmapscan.scan_ports(ip)
    print(open_ports)

    print("[+] Detecting Technologies...")
    tech_stack = tech_ennumerator.get_technologies_builtwith(target,key)
    tech_names = []
    for result in tech_stack['Results']:
        for path in result['Result']['Paths']:
            for tech in path.get('Technologies', []):  
                tech_names.append(tech)

    for tech in tech_names:
        print(f"\n- {tech}")

    print("[+] Scrapping HTTP headers and Meta Tags...")
    scrap = scrapper.detect_technologies_from_headers(target)
    print(scrap)

    print("[+] Scanning for Vulnerabilities...")
    vulns = vulnerabilities.scan_vulnerabilities(ip,sh_key)
    print(vulns)

    print("[+] Detecting XSS & SQL Injection...")
    injection_test = injections.detect_xss_sqli(target)
    print(injection_test)

if __name__ == "__main__":
    print(" - DarkProbe Recon Tool -")
    target = input("Enter target URL or IP for recon and analysis or 'quit' to exit: ").strip()
    key= input("Enter your BuiltWith api key: ").strip()
    sh_key = input("Enter your Shodan api key: ").strip()
    while target != 'quit':
          run_recon_and_scan(target)
          target = input("Enter target URL or IP for recon and analysis or 'quit' to exit: ").strip()
