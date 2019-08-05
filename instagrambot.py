from instagram_private_api import Client, ClientCompatPatch
import base64
user_name = 'sarahroberts3009'
password = 'tkfkfhqjcm'

api = Client(user_name, password)
results = api.feed_timeline()
# items = results.get('items', [])
#
# with open("./instagram/cat1.jpg", "rb") as imageFile:
#     str = base64.b64encode(imageFile.read())
#     print (str)
#     # byteString = unicode_string.encode(str)
#     api.post_photo(str, (436,436), caption='my cat! #cat #kitten')
def get_user_with_hashtag (hashtag):
    rank_token = api.generate_uuid()
    tagged = api.feed_tag(hashtag, rank_token)
    items = tagged.get('items', [])
    # paginate here
    userIds = []
    for item in items:
        print(item['user']['username'])
        userIds.append(item['user']['username'])
    print(userIds)
    return userIds

like_count = 0
liked_feed = api.feed_liked()
# print(len(liked_feed['items']))
# print(liked_feed['items'][0].keys())

# for item in items:
#     if like_count < 20:
#     # Manually patch the entity to match the public api as closely as possible, optional
#     # To automatically patch entities, initialise the Client with auto_patch=True
#         ClientCompatPatch.media(item)
#         print(item['id'])
#         api.post_like(item['id'], 'feed_timeline')
#         like_count += 1

get_user_with_hashtag('blockchain')
