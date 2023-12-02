username = input("What's ur un: ")

# Tab si Spatiu sunt numite "   Whitspace  "

clean_username = username.strip()
print(len(clean_username))
clean_username = clean_username.replace(
    " ",
    ''
)
print(len(clean_username))

print(f'Eu inregistrez username-ul "{clean_username}"')
