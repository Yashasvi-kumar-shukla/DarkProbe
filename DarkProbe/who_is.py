import whois


class who_is:
    def get_whois_info(target):
        try:
            w = whois.whois(target)
            return w
        except Exception as e:
            return f"Error fetching WHOIS: {e}"