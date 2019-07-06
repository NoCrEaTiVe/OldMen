from instagram import Account, Media, WebAgent

agent = WebAgent()
account = Account("islambek.temirbek")

media1, pointer = agent.get_media(account)
media2, pointer = agent.get_media(account, pointer=pointer, count=50, delay=1)
print(account.full_name)
for i in media1:
    print(i.location.name)