import dns.resolver

def get_dns_records(domain):
    """
    Retrieves DNS records for A, MX, NS, and TXT.
    Each record type is queried individually.
    Returns a dictionary with record types as keys and lists of results.
    """
    records = {}

    def resolve_record(record_type):
        try:
            answers = dns.resolver.resolve(domain, record_type)
            if record_type == 'A':
                return [r.address for r in answers]
            elif record_type == 'MX':
                return [str(r.exchange).rstrip('.') for r in answers]
            elif record_type == 'NS':
                return [str(r.target).rstrip('.') for r in answers]
            elif record_type == 'TXT':
                return [
                    ''.join(
                        txt.decode() if isinstance(txt, bytes) else txt
                        for txt in r.strings
                    )
                    for r in answers
                ]
        except dns.resolver.NoAnswer:
            return []  # No records of this type
        except dns.resolver.NXDOMAIN:
            return [f"{domain} does not exist."]
        except Exception as e:
            return [f"Error retrieving {record_type} records: {e}"]

    for record_type in ['A', 'MX', 'NS', 'TXT']:
        records[record_type] = resolve_record(record_type)

    return records