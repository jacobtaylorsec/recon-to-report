import dns.resolver

def get_dns_records(domain):
    """
    Retrieves DNS records for A, MX, NS, and TXT.
    Returns a dictionary containing the records.
    """
    records = {}
    try:
        records['A'] = [r.address for r in dns.resolver.resolve(domain, 'A')]
        records['MX'] = [str(r.exchange) for r in dns.resolver.resolve(domain, 'MX')]
        records['NS'] = [str(r.target) for r in dns.resolver.resolve(domain, 'NS')]
        records['TXT'] = [str(r.strings) for r in dns.resolver.resolve(domain, 'TXT')]
    except Exception as e:
        records['error'] = str(e)
    
    return records