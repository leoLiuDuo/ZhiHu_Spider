# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class UserItem(Item):
    name = Field()
    id = Field()
    avatar_url = Field()
    headline = Field()
    description = Field()
    url = Field()
    url_token = Field()
    gender = Field()
    cover_url = Field()
    type = Field()
    badge = Field()

    answer_count = Field()
    articles_count = Field()
    commercial_question_count = Field()
    favorite_count = Field()
    favorited_count = Field()
    follower_count = Field()
    following_columns_count = Field()
    following_count = Field()
    marked_answer_count = Field()
    mutual_followees_count = Field()
    hosted_live_count = Field()
    participated_live_count = Field()

    locations = Field()
    educations = Field()
    employments = Field()
