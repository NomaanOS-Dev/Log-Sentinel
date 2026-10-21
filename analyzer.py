import re

class LogAnalyzer:
    def __init__(self):
        self.patterns = {
            "Failed SSH Login": r"Failed password for (?:invalid user )?(\w+) from ([0-9.]+)",
            "SQL Injection Attempt": r"(?i)(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|OR 1=1|' OR '1'='1)",
            "HTTP Error Status (4xx/5xx)": r'HTTP/1\.[01]"\s+([45]\d\d)',
            "Suspicious Exec Command": r"(?i)(/bin/bash|/bin/sh|wget|curl|chmod \+x)",
            "IP Address": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
        }

    def scan_log(self, log_text):
        results = {}
        for category, pattern in self.patterns.items():
            matches = re.findall(pattern, log_text)
            if matches:
                results[category] = {
                    "count": len(matches),
                    "samples": matches[:5]
                }
        return results
