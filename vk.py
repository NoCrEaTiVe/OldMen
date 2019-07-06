import requests
token = '2c3233b12c3233b12c3233b1f02c59b56b22c322c3233b17112c7455c983a2581564817'
version = 5.101
def take_posts(inputId):
    owner_id = inputId

    # 
    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v' : version,
                                'owner_id': owner_id, 
                                #'count' : 1 
                                })
    postCount = response.json()['response']['count']
    #print(postCount)
    likeCount = response.json()['response']['items']
    print(likeCount)

    response = requests.get('https://api.vk.com/method/users.get',
                            params={
                                'access_token': token,
                                'v' : version,
                                'user_ids': owner_id, 
                                
                            })
    data = response.json()['response']
    for info in data:
        #print(len(info))
        first_name = info['first_name']
        last_name = info['last_name']

    response = requests.get('https://api.vk.com/method/friends.get',
                            params={
                                'access_token': token,
                                'v' : version,
                                'user_id': owner_id, 
                                
                            })
    friends = response.json()['response']['count']
    #print(friends)




    #print(data)

#take_fullName(182811862)
take_posts(182811862)