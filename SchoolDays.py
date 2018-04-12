#!/usr/bin/env python

import datetime
from dateutil import rrule
import time
import json
#############################
# Calculate School days left
#############################
def SchoolDays():
    lastDay = datetime.date(2018, 6, 8)
    today = datetime.date.today()
    holiday = datetime.date(2018, 5, 28)
    if today > holiday:
        days_count = get_working_days(today, lastDay)
        return "There are %s school days left" % days_count
    else:
        days_count = get_working_days(today, lastDay) - 1
        return "There are %s school days left" % days_count
def get_working_days(date_start_obj, date_end_obj):
    weekdays = rrule.rrule(rrule.DAILY, byweekday=range(0, 5), dtstart=date_start_obj, until=date_end_obj)
    weekdays = len(list(weekdays))
    if int(time.strftime('%H')) >= 18:
        weekdays -= 1
    return weekdays
################################
# Builders
################################

def build_response(message, session_attributes={}):
    response = {}
    response['version'] = '1.0'
    response['sessionAttributes'] = session_attributes
    response['response'] = message
    return response

def build_PlainSpeech(body):
    speech = {}
    speech['type'] = 'PlainText'
    speech['text'] = SchoolDays()
    return speech

def build_SimpleCard(title,body):
    card = {}
    card['type'] = 'Simple'
    card['title'] = title
    card['content'] = body
    return card

################################
# Responses
################################

def statement(title,body):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = True
    return build_response(speechlet)

################################
# Launch
################################

def on_launch(event,context):
    return statement("title",SchoolDays())

################################
# Program Entry
################################

def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event,context)
    #elif event['request']['type'] == "IntentRequest":
    #    return intent_router(event,context)