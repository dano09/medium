from datetime import date, datetime


'''
GIST 1 Conversions
'''

''' (1) Date to String '''
d = date(2018, 12, 6)
d.strftime('%Y-%m-%d')
# '2018-12-06'
d.strftime('%y-%b-%a')  # Alternate formatting
# '18-Dec-Thu'


''' (2) Datetime to String '''
d = datetime(2018, 12, 6, 20, 21, 3, 63)
str(d)
# '2018-12-06 20:21:03.000063'
d.strftime("%Y-%m-%d %H:%M:%S")     # Military
# '2018-12-06 20:21:03'
d.strftime("%Y-%m-%d %I:%M:%S %p")  # 12-hour
# '2018-12-06 08:21:03 PM'


''' (3) String to Date '''
datetime.strptime('2018-12-06', '%Y-%m-%d').date()
# datetime.date(2018, 12, 6)
datetime.strptime('2018-12-06 20:30:10.75', '%Y-%m-%d %H:%M:%S.%f').date()
# datetime.date(2018, 12, 6)


''' (4) String to Datetime '''
datetime.strptime('2018-12-06', '%Y-%m-%d')
# datetime.datetime(2018, 12, 6, 0, 0)
datetime.strptime('2018-12-06 20:30:10.75', '%Y-%m-%d %H:%M:%S.%f')
# datetime.datetime(2018, 12, 6, 20, 30, 10, 750000)




'''
GIST 2 TimeZones
'''
import pytz

datetime.now()  # Date and time for your current Timezone
# datetime.datetime(2018, 12, 18, 16, 26, 6, 170817)

datetime.utcnow()  # Date and time for UTC Timezone
# datetime.datetime(2018, 12, 18, 21, 25, 43, 627817)

datetime.now(tz=pytz.UTC)
# datetime.datetime(2018, 12, 18, 21, 25, 44, 463817, tzinfo=<UTC>)

# Change timezones
tokyo_tz = pytz.timezone('Asia/Tokyo')
datetime.now(tz=tokyo_tz)
# datetime.datetime(2018, 12, 19, 6, 43, 55, 463817, tzinfo=<DstTzInfo 'Asia/Tokyo' JST+9:00:00 STD>)
# Another way
tokyo_tz.localize(datetime.now())  # timezone.localize(naive_dt) = aware_dt
# datetime.datetime(2018, 12, 18, 16, 52, 14, 798817, tzinfo=<DstTzInfo 'Asia/Tokyo' JST+9:00:00 STD>)

# Common timezones
len(pytz.common_timezones)
# 439

# All timezones
len(pytz.all_timezones)
# 591

pytz.common_timezones[:5]
# ['Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara']

# US/Eastern
# US/Pacific
# Europe/London
# America/New_York
# Asia/Hong_Kong
# Asia/Tokyo
# Asia/Calcutta  ( New Delhi)

# List of Countries and timezones @ https://gist.github.com/mjrulesamrat/0c1f7de951d3c508fb3a20b4b0b33a98

# ISO Format
d = datetime.now()
d.isoformat()
# '2018-12-18T16:29:54.397817'


'''
GIST 2 Business Dates
'''
