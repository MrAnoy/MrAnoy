import urllib.request
import json
import re
import datetime
import random

# Fallback hacker quotes in case the API is down
fallback_quotes = [
    "The quieter you become, the more you are able to hear.",
    "There is no patch for human stupidity.",
    "Talk is cheap. Show me the code.",
    "System integrity breached. Rebuilding firewalls.",
    "Data is the new oil. Encryption is the new pipeline.",
    "I read your code... it was terrifying.",
    "In a world full of variables, be a constant."
]

try:
    # Try fetching a random tech quote from a free API
    url = "https://api.quotable.io/quotes/random?tags=technology"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        quote = data[0]['content']
except Exception:
    # If API fails, use a random fallback quote
    quote = random.choice(fallback_quotes)

# Clean up quote length for the terminal
if len(quote) > 75:
    quote = quote[:72] + "..."

# Open and read the README file
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Replace the DAILY_LOG line using Regex
new_log_line = f'[+] DAILY_LOG     : "{quote}"'
readme = re.sub(r'\[\+\] DAILY_LOG\s+: ".*"', new_log_line, readme)

# Replace the LAST_UPDATE line with the current time
current_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
new_update_line = f'[+] LAST_UPDATE   : {current_time}'
readme = re.sub(r'\[\+\] LAST_UPDATE\s+: .*', new_update_line, readme)

# Write the updated content back
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("Status updated successfully!")
