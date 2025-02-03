import dns.resolver


class dns_rec:    
    def get_dns_records(target):
        records = {}
        for record_type in ['A', 'MX', 'NS', 'TXT']:
            try:
                records[record_type] = [r.to_text() for r in dns.resolver.resolve(target, record_type)]
            except:
                records[record_type] = []
        return records