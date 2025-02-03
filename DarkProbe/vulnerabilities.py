import shodan

class vulnerabilities:
    def scan_vulnerabilities(target,key):
        SHODAN_API_KEY = key
        shodan_api = shodan.Shodan(SHODAN_API_KEY)
        try:
            result = shodan_api.host(target)
            vulns = result.get("vulns", [])
            return vulns if vulns else "No vulnerabilities found"
        except Exception as e:
            return f"Error fetching vulnerabilities: {e}"