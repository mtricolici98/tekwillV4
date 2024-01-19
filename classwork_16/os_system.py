import os

email_titles = []
os.system(f'say You have {len(email_titles)} new emails:')

for title in email_titles:
    print(os.system(f'say {title}'))