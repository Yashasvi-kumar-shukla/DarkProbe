import requests

class injections:
    def detect_xss_sqli(target):
        test_payloads = {"XSS": "<script>alert('XSS')</script>", "SQLi": "' OR 1=1 --"}
        for vuln, payload in test_payloads.items():
            try:
                response = requests.get(f"http://{target}/?q={payload}", timeout=5)
                if payload in response.text:
                    return f"Possible {vuln} vulnerability detected!"
            except:
                continue
        return "No basic XSS or SQLi found"