from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("sarahroberts3009", "tkfkfhqjcm")
InstagramAPI.login()  # login

photo_path = './cat2.jpg'
caption = "#cat #kitten"
InstagramAPI.uploadPhoto(photo_path, caption=caption)
rank_token = InstagramAPI.generate_uuid()
tagged = InstagramAPI.feed_tag('blockchain', rank_token)
print(tagged)
