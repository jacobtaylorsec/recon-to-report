from datetime import datetime

def create_markdown_report(domain, ip, whois_data, geo, dns, ports):
    """
    Generates a Markdown report (report.md) that contains:

    - Target IP and geolocation
    - WHOIS information
    - DNS records
    - Open ports and their banners
    """
    with open("report.md", "w", encoding="utf-8") as f:
        f.write(f"# Recon Report for {domain}\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write("## Target IP Address\n")
        f.write("```\n")
        f.write(f"{ip}\n")
        f.write("```\n\n")

        f.write("## Geolocation\n")
        f.write("```\n")
        f.write(f"{geo}\n")
        f.write("```\n\n")

        f.write("## WHOIS Information\n")
        f.write("```\n")
        f.write(str(whois_data))
        f.write("\n```\n\n")

        f.write("## DNS Records\n")
        for record_type, data in dns.items():
            f.write(f"### {record_type} Records\n")
            f.write("```\n")
            f.write(str(data))
            f.write("\n```\n")

        f.write("\n## Open Ports and Banners\n")
        for port, banner in ports:
            f.write(f"- Port {port}: {banner}\n")

        f.write("\n---\n")
        f.write("Report generated using a custom Python reconnaissance tool.\n")