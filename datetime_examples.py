from datetime import date, datetime, timedelta


'''
GIST 1 Conversions and formatting
'''

''' (1) Date to String '''
d = date(2018, 12, 6)   # datetime.date(2018, 12, 6)
d.strftime('%Y-%m-%d')  # '2018-12-06'
d.strftime('%y-%b-%a')  # '18-Dec-Thu'

''' (2) Datetime to String '''
d = datetime(2018, 12, 6, 20, 21, 3, 63)  # datetime.datetime(2018, 12, 6, 20, 21, 3, 63)
str(d)                                    # '2018-12-06 20:21:03.000063'
d.strftime("%Y-%m-%d %H:%M:%S")           # '2018-12-06 20:21:03'
d.strftime("%Y-%m-%d %I:%M:%S %p")        # '2018-12-06 08:21:03 PM'

''' (3) String to Date '''
day = '2018-12-06'                                          # '2018-12-06'
day_time = '2018-12-06 20:30:10.75'                         # '2018-12-06 20:30:10.75'
datetime.strptime(day, '%Y-%m-%d').date()                   # datetime.date(2018, 12, 6)
datetime.strptime(day_time, '%Y-%m-%d %H:%M:%S.%f').date()  # datetime.date(2018, 12, 6)

''' (4) String to Datetime '''
datetime.strptime(day, '%Y-%m-%d')                   # datetime.datetime(2018, 12, 6, 0, 0)
datetime.strptime(day_time, '%Y-%m-%d %H:%M:%S.%f')  # datetime.datetime(2018, 12, 6, 20, 30, 10, 750000)

''' (5) Working with ISO 8601  '''
import dateutil.parser
datetime.today().isoformat('#')                  # '2018-12-18#20:02:26.475230'
datetime.today().isoformat('#', 'minutes')       # '2018-12-18#20:03'
datetime.today().isoformat('#', 'microseconds')  # '2018-12-18#20:03:49.658230'
di = datetime.now().isoformat()                  # '2018-12-18T19:56:44.100229'
dateutil.parser.parse(di)                        # datetime.datetime(2018, 12, 18, 19, 56, 44, 100229)

'''
GIST 2 TimeZones
'''
import pytz

''' (1) List of Timezones '''
len(pytz.common_timezones)  # 439
len(pytz.all_timezones)     # 591
pytz.common_timezones[:5]   # ['Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara']

# US/Eastern
# US/Pacific
# Europe/London
# America/New_York
# Asia/Hong_Kong
# Asia/Tokyo
# Asia/Calcutta  ( New Delhi)
# List of Countries and timezones @ https://gist.github.com/mjrulesamrat/0c1f7de951d3c508fb3a20b4b0b33a98


''' (2) Current Timezone and UTC '''
datetime.now()             # datetime.datetime(2018, 12, 18, 18, 51, 53, 451229)
datetime.utcnow()          # datetime.datetime(2018, 12, 18, 23, 51, 57, 346229)
datetime.now(tz=pytz.UTC)  # datetime.datetime(2018, 12, 18, 23, 52, 3, 378229, tzinfo=<UTC>)


''' (3) Change Timezones '''
tokyo_tz = pytz.timezone('Asia/Tokyo')
datetime.now(tz=tokyo_tz)          # datetime.datetime(2018, 12, 19, 6, 43, 55, 463817, tzinfo=<DstTzInfo 'Asia/Tokyo' JST+9:00:00 STD>)
tokyo_tz.localize(datetime.now())  # datetime.datetime(2018, 12, 18, 16, 52, 14, 798817, tzinfo=<DstTzInfo 'Asia/Tokyo' JST+9:00:00 STD>)
# from newyork to london
# from london to hong kong

'''
GIST 3 Time Delta and modifying time
'''

''' (1) Time Delta Constructor '''
# (days, seconds, microseconds)
timedelta(weeks=1, days=3, hours=5, minutes=6, seconds=4, milliseconds=10, microseconds=7)  # datetime.timedelta(10, 18364, 10007)
timedelta(days=5, hours=5, minutes=10)                                                      # datetime.timedelta(5, 18600)
timedelta(days=1, microseconds=10)                                                          # datetime.timedelta(1, 0, 10)
# Resolution is microseconds
timedelta().resolution                                                                      # datetime.timedelta(0, 0, 1)

''' (2) Modifying date with timedelta '''
date.today()                      # datetime.date(2018, 12, 18)
date.today() - timedelta(1)       # datetime.date(2018, 12, 17)
date.today() + timedelta(days=1)  # datetime.date(2018, 12, 19)
timedelta()

''' (3)  Modifying date without timedelta '''
dt = datetime(year=2000, month=4, day=24, hour=18, minute=30)  # datetime.datetime(2000, 4, 24, 18, 30)
dt.replace(year=2050, month=2)                                 # datetime.datetime(2050, 2, 24, 18, 30)


'''
GIST 4 Business Dates
'''
import pandas as pd
from pandas.tseries.offsets import BDay
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay


''' (1) Pandas TimeStamp '''

''' (2) Pandas DatetimeIndex '''

''' (3) Get Range of business days '''
# Include Holidays
pd.date_range('2018-12-23', '2018-12-26', freq=BDay())              # DatetimeIndex(['2018-12-24', '2018-12-25', '2018-12-26'], dtype='datetime64[ns]', freq='B')

# Exclude Holidays
us_bd = CustomBusinessDay(calendar=USFederalHolidayCalendar())
pd.DatetimeIndex(start='2018-12-23', end='2018-12-26', freq=us_bd)  # DatetimeIndex(['2018-12-24', '2018-12-26'], dtype='datetime64[ns]', freq='C')


