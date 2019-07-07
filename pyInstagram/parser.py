from instagram import Account, Media, WebAgent
# from datetime import datetime
# ts = int("1284101485")

print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
agent = WebAgent()
account = Account("islambek.temirbek")#username
d={}#information about user
media1, pointer = agent.get_media(account)#last ten publication
media2, pointer = agent.get_media(account, pointer=pointer, count=account.media_count, delay=1)#other
places=[]#will be next time
cntfrslks=0
cntfrscmnt=0
cntforlikes= 0
cntforcomments=0
for s in media1:
    cntforlikes=cntforlikes+s.likes_count
    cntforcomments = cntforcomments+s.comments_count
    cntfrslks=+s.likes_count
    cntfrscmnt=+s.comments_count
    print(s.caption)
for i in media2:
    cntforlikes=cntforlikes+i.likes_count
    cntforcomments = cntforcomments+i.comments_count
    
ln = len(media2)+len(media1)
d["avgfstpublclks"]=cntfrslks//len(media1)
d["avgfstpublccomments"]=cntfrscmnt//len(media1)
d["averagecountoflikes"]=(cntforlikes//ln)
d["averagecountofcomments"]=(cntforcomments//ln)
d["nickname"]=account.username
d["mediacount"]=account.media_count
d["fullname"]=account.full_name
d["follows_count"]=account.follows_count
d["followers_count"]=account.followers_count
d["is_private"]=account.is_private
d["profile_pic_url_hd"]=account.profile_pic_url_hd
d["biography"]=account.biography
