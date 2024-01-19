import os

for url in ["google.com", "facebook.com", "reddit.com"]:
    os.popen(f'start msedge "{url}"')