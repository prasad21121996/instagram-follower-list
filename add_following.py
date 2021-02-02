import instaloader

L = instaloader.Instaloader()
username=''
password=''

L.login(username, password)        

profile_id = ''

profile = instaloader.Profile.from_username(L.context, profile_id)
followees = profile.get_followees()
followers = profile.get_followers()

for x in followers:
    print(x.username)
