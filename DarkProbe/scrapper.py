import requests

class scrapper:
    def detect_technologies_from_headers(target):
        try:
            response = requests.get(f"http://{target}", timeout=5)
            headers = response.headers
            tech = []
            
            if 'server' in headers:
                tech.append(f"Server: {headers['server']}")
            if 'x-powered-by' in headers:
                tech.append(f"Powered by: {headers['x-powered-by']}")
            return tech if tech else "No technologies detected"
        except Exception as e:
            return f"Error fetching headers: {e}"