import nmap

class nmapscan:
    def scan_ports(target):
        scanner = nmap.PortScanner()
        scanner.scan(target, '1-65535')
        return scanner[target].all_protocols()