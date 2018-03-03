# Example of python build-in module: datetime
from datetime import datetime, timedelta, timezone
# From "datatime" module import "datetime" class and class "timedelta"
import re

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2020, 11, 11, 11, 11)
print(dt)

t = dt.timestamp()
print(datetime.fromtimestamp(t))  # local time
print(datetime.utcfromtimestamp(t))  # UTC time

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
print(now.strftime('%Y, %m %d %M:%H'))
print(now.strftime('%A, %B %d, %Y %H:%M'))

now = datetime.now()
print(now + timedelta(hours=25))
print(now - timedelta(days=3.5))

tz_utc_8 = timezone(timedelta(hours=8))  # create timezone UTC +8:00
now = datetime.now()

# force timezone to be UTC +8:00 do not change time
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)


def to_timestamp(dt_str, tz_str):

    tz_re = re.compile(r'^\w{3}([\-\+])0?([0-9]|1[0-2])')
    a = tz_re.match(tz_str).group(1)
    b = tz_re.match(tz_str).group(2)

    if a == '-':
        tz = timezone(timedelta(hours=-int(b)))
    elif a == '+':
        tz = timezone(timedelta(hours=int(b)))

    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    dt = dt.replace(tzinfo=tz)
    return dt.timestamp()


# test
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
