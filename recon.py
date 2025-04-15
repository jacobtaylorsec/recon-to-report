from recon.dns_tools import get_dns_records 
from recon.geo import get_geolocation
from recon.port_scanner import scan_ports
from recon.reporter import create_markdown_report
from recon.whois_lookup import get_whois
import socket

def main():
    # Prompt for target domain
    domain = input("Enter target domain: ").strip()
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] Target IP: {ip}")
    except Exception as e:
        print(f"Error resolving domain: {e}")
        return
    
    # Execute recon steps
    print("[+] Running WHOIS lookup...")
    whois_data = get_whois(domain)

    print("[+] Running DNS enumeration...")
    dns_data = get_dns_records(domain)

    print("[+] Running IP geolocation...")
    geo_data = get_geolocation(ip)

    print("[+] Scanning ports...")
    ports = scan_ports(ip)

    print("[+] Creating report...")
    create_markdown_report(domain, ip, whois_data, geo_data, dns_data, ports)
    print("Recon complete. Report saved as 'report.md'.")

    if __name__ == "__main__":
        main()