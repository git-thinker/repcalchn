## Repcalchn

本项目提供公历日期与时间向法国共和历转换的功能，支持汉语（简体中文）和法语。A script that converts date and time to the French Republican systems used by the French Republic, supports Simplified Chinese and French.

This repo borrows heavily from [dekadans/repcal](https://github.com/dekadans/repcal).

A script that converts date and time to the systems used by the French Republic, the calendar from 1793 to 1805 and decimal time for about a year between 1794 and 1795.
More information can be found on [Wikipedia](https://en.wikipedia.org/wiki/French_Republican_calendar), [Wikipedia Chinese](https://zh.wikipedia.org/zh-cn/%E6%B3%95%E5%9C%8B%E5%85%B1%E5%92%8C%E6%9B%86)

It uses the Romme method of calculating leap years, as in keeping the ones used by the French Republic and using the Gregorian rules for the years after the calendar was abolished.

In comparison with [dekadans/repcal](https://github.com/dekadans/repcal), this repo offers flag and APIs that supports Chinese.

### Installation

```
$ pip install repcalchn
```

### Usage

The current local time is used by default.

```
$ repcalchn
5:60:56, 法国共和历 231年 菓月 18 鼠李日 星期八
```

Or, for the full Republican experience, it can default to Paris Mean Time (6.49 decimal minutes ahead of GMT).

```
$ repcalchn --paris-mean
2:33:91, 法国共和历 231年 菓月 18 鼠李日 星期八
```

If you want see it in French, just add `--fr`

```
$ repcalchn --fr
5:62:1, octidi 18 fructidor an CCXXXI
```

It also accepts date, time and format as arguments.

```
$ repcalchn '1969-07-20 20:17:40'
8:45:60, 法国共和历 177年 牧月 1 紫花苜蓿日 星期一

$ repcalchn '1969-07-20'
法国共和历 177年 牧月 1 紫花苜蓿日 星期一

$ repcalchn '20:17:40'
8:45:60

$ repcalchn '1969-07-20' --format '{%d} {%B}'
1 thermidor

$ repcalchn '1969-07-20' --format '{%y}年 {%b} {%d}'
177年 牧月 1
```

### As a Python package

```python
from repcalchn import RepublicanDate, DecimalTime
from datetime import datetime

n = datetime.now()
rd = RepublicanDate.from_gregorian(n.date())
rd.set_chinese_formatting()
dt = DecimalTime.from_standard_time(n.time())

print(rd) # 法国共和历 231年 菓月 18 鼠李日 星期八
print(dt) # 5:66:4
```

### RepublicanDate API


| Value                          | Instance method       | Format placeholder | Example           | Note                                                                                       |
| :------------------------------- | ----------------------- | -------------------- | ------------------- | -------------------------------------------------------------------------------------------- |
| Year (arabic)                  | get_year_arabic()     | %y                 | _219_             |                                                                                            |
| Year (roman)                   | get_year_roman()      | %Y                 | _CCXXIX_          |                                                                                            |
| Month                          | get_month()           | %B                 | _vendémiaire_     | Method returns`None` and placeholder returns `''` if `is_sansculottides()` is `True`.      |
| Month (Chinese)                | get_month_chn()       | %b                 | _获月_            | Method returns`None` and placeholder returns `''` if `is_sansculottides()` is `True`.      |
| Week (décade)                  | get_week_number()     | %W                 | _3_               |                                                                                            |
| Day in month                   | get_day()             | %d                 | _28_              |                                                                                            |
| Day in week                    | get_weekday()         | %A                 | _octidi_          | Method and placeholder returns french sansculottides name if`is_sansculottides()`is`True`. |
| Day in week (Chinese)          | get_weekday_chn()     | %a                 | _星期八_          | Method and placeholder returns Unique Day name if`is_sansculottides()`is`True`.            |
| Unique Day name (Chinese)      | get_unique_chn()      | %x                 | _紫花苜蓿日_      | Every date in French Republican Calendar has an unique name.                               |
| Full Unique Day name (Chinese) | get_full_unique_chn() | %X                 | _牧月 紫花苜蓿日_ | Month and unique day name in chinese. No month if`is_sansculottides()` is `True`.          |
| Is complementary               | is_sansculottides()   | --                 | _false_           | Check if it is a sansculottides day, which is not included in any month.                   |

### DecimalTime API


| Value  | Property | Format placeholder | Example |
| -------- | ---------- | -------------------- | --------- |
| Hour   | hour     | %H                 | _8_     |
| Minute | minute   | %M                 | _1_     |
| Second | second   | %S                 | _65_    |
