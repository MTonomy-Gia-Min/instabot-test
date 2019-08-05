#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from instabot_py import InstaBot
import json



# iterate through usernames/pw to do all actions
def mass_action(credentials, usernames_to_follow):
    for cred in credentials:
        print(cred)

        bot = InstaBot(
            login=cred["username"],  # Enter username (lowercase). Do not enter email!
            password=cred["password"],
            like_per_day=1000,
            comments_per_day=0,
            tag_list=["crypto", "cryptocurrency", "blockchain", "finance", "money", "media", "film", "entertainment", "music", "follow4follow", "f4f", "l:212999109"],
            tag_blacklist=["rain", "thunderstorm"],
            user_blacklist={},
            max_like_for_one_tag=50,
            follow_per_day=300,
            follow_time=1 * 60 * 60,
            unfollow_per_day=300,
            unlike_per_day=0,
            unfollow_recent_feed=True,
            # If True, the bot will also unfollow people who dont follow you using the recent feed. Default: True
            time_till_unlike=3 * 24 * 60 * 60,  # 3 days
            unfollow_break_min=15,
            unfollow_break_max=30,
            user_max_follow=0,
            # session_file=False, # Set to False to disable persistent session, or specify custom session_file (ie ='myusername.session')
            user_min_follow=0,
            log_mod=0,
            proxy="",
            # List of list of words, each of which will be used to generate comment
            # For example: "This shot feels wow!"
            comment_list=[
                ["this", "the", "your"],
                ["photo", "picture", "pic", "shot"],
                ["is", "looks", "is 👉", "is really"],
                [
                    "great",
                    "super",
                    "good",
                    "very good",
                    "good",
                    "wow",
                    "WOW",
                    "cool",
                    "GREAT",
                    "magnificent",
                    "magical",
                    "very cool",
                    "stylish",
                    "beautiful",
                    "so beautiful",
                    "so stylish",
                    "so professional",
                    "lovely",
                    "so lovely",
                    "very lovely",
                    "glorious",
                    "so glorious",
                    "very glorious",
                    "adorable",
                    "excellent",
                    "amazing",
                ],
                [".", "🙌", "... 👏", "!", "! 😍", "😎"],
            ],
            # Use unwanted_username_list to block usernames containing a string
            # Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
            # 'free_followers' will be blocked because it contains 'free'
            unwanted_username_list=[
                "second",
                "stuff",
                "art",
                "project",
                "love",
                "life",
                "food",
                "blog",
                "free",
                "keren",
                "photo",
                "graphy",
                "indo",
                "travel",
                "art",
                "shop",
                "store",
                "sex",
                "toko",
                "jual",
                "online",
                "murah",
                "jam",
                "kaos",
                "case",
                "baju",
                "fashion",
                "corp",
                "tas",
                "butik",
                "grosir",
                "karpet",
                "sosis",
                "salon",
                "skin",
                "care",
                "cloth",
                "tech",
                "rental",
                "kamera",
                "beauty",
                "express",
                "kredit",
                "collection",
                "impor",
                "preloved",
                "follow",
                "follower",
                "gain",
                ".id",
                "_id",
                "bags",
            ],
            unfollow_whitelist=[],
        )
        # bot.follow_by_username(usernames=usernames_to_follow)
        bot.like_all_media_by_username(usernames=usernames_to_follow)
        # bot.like_all_media_by_username(usernames=usernames_to_follow)



    return
# follow all users in the list
def follow_by_username(bot, usernames):
    for user in usernames:
        print(user)
        id = bot.get_user_id_by_username(user)
        print(id)


# follow all users that has ever liked any of my posts if I haven't followed them already
def follow_users_that_like_my_posts(bot):
    return

# like & comment on posts that have specific tags
def like_and_comment_posts(bot, tags):
    return

# find users who posts relating to specific tags and send DMs
def dm_users_with_tags(bot, tags):
    return


# if the user that the bot DM'd didn't reply, arbitrarily comment on one of their posts to check their inbox
def comment_to_follow_up(bot, user_id):
    return
