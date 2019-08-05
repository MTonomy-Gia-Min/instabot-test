media_id = 19321108808463599769460219909
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
shortened_id = ''
while media_id > 0:
    remainder = media_id % 64
    # dual conversion sign gets the right ID for new posts
    media_id = (media_id - remainder)
    #remainder should be casted as an integer to avoid a type error
    shortened_id = alphabet[int(remainder)] + shortened_id

    print('https://instagram.com/p/' + shortened_id + '/')
