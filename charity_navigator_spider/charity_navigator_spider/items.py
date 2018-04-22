# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CharityNavigatorItem(scrapy.Item):

    charity_url = scrapy.Field()
    charity_name = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    organization_type = scrapy.Field()
    overall_score = scrapy.Field()
    financial_score = scrapy.Field()
    accountability_score = scrapy.Field()
    cn_advisory = scrapy.Field()
    total_contributions = scrapy.Field()
    other_revenue = scrapy.Field()
    program_expenses = scrapy.Field()
    administrative_expenses = scrapy.Field()
    fundraising_expenses = scrapy.Field()
    payments_to_affiliates = scrapy.Field()
    excess_or_deficit_for_year = scrapy.Field()
    net_assets = scrapy.Field()
    compensation_leader_compensation = scrapy.Field()
    compensation_leader_expense_percent = scrapy.Field()
    compensation_leader_title = scrapy.Field()
