#!/usr/bin/env python

import datetime
from dateutil import rrule
import time

def SchoolDays():
    lastDay = datetime.date(2018, 6, 8)
    today = datetime.date.today()
    holiday = datetime.date(2018, 5, 28)
    #delta = (lastDay - today)
    #print "%s days of school left" % delta.days
    if today > holiday:
        print get_working_days(today, lastDay)
    else:
        print get_working_days(today, lastDay) - 1
def get_working_days(date_start_obj, date_end_obj):
    weekdays = rrule.rrule(rrule.DAILY, byweekday=range(0, 5), dtstart=date_start_obj, until=date_end_obj)
    weekdays = len(list(weekdays))
    if int(time.strftime('%H')) >= 18:
        weekdays -= 1
    return weekdays

if __name__ == "__main__":
    SchoolDays()
