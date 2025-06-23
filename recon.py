from recon.dns_tools import get_dns_records
from recon.geo import get_geolocation
from recon.port_scanner import scan_ports
from recon.reporter import create_markdown_report
from recon.whois_lookup import get_whois
import socket

def main():
    while True:
        domain = input("Enter target domain (or 'quit' to exit): ").strip()
        if domain.lower() == 'quit':
            print("Exiting...")
            break

        try:
            ip = socket.gethostbyname(domain)
            print(f"[+] Target IP: {ip}")
        except Exception as e:
            print(f"Error resolving domain: {e}")
            continue
        
        try:
            print("[+] Running WHOIS lookup...")
            whois_data = get_whois(domain)

            print("[+] Running DNS enumeration...")
            dns_data = get_dns_records(domain)

            print("[+] Running IP geolocation...")
            geo_data = get_geolocation(ip)

            print("[+] Scanning ports...")
            ports = scan_ports(ip)
        except Exception as e:
            print(f"Error during reconnaissance: {e}")
            continue

        print("[+] Creating report...")
        create_markdown_report(domain, ip, whois_data, geo_data, dns_data, ports)
        print("Recon complete. Report saved as 'report.md'.\n")

if __name__ == "__main__":
    main()
