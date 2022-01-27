birthday=input('Please insert your birthday dd/mm/yyyy  ')
date_target=input('Please insert target date of Biorhythim dd/mm/yyyy  ')

#birthday='15/04/2016'
#date_target='26/09/2019'

def get_month_code(mm):
  if mm=='01':
    return 0
  if mm=='02':
    return 3
  if mm=='03':
    return 3
  if mm=='04':
    return 6
  if mm=='05':
    return 1
  if mm=='06':
    return 4
  if mm=='07':
    return 6
  if mm=='08':
    return 2
  if mm=='09':
    return 5
  if mm=='10':
    return 0
  if mm=='11':
    return 3
  if mm=='12':
    return 5

def get_century_code(bcentruy):
  if bcentury=='s1700':
    return 4
  if bcentury=='s1800':
    return 2
  if bcentury=='s1900':
    return 0
  if bcentury=='s2000':
    return 6
  if bcentury=='s2100':
    return 4
  if bcentury=='s2200':
    return 2
  if bcentury=='s2300':
    return 0

def check_leap(byear):
  if int(byear)%100==0:
    return 1
  if int(byear)%400==0:
    return 1
  if int(byear)%4==0:
    return 1
  else:
    return 0

## TASK 1 to demonstrate day of date
    
day_code=birthday[:2]
bmonth=birthday[3:-5]
month_code=get_month_code(bmonth)
bcentury='s'+birthday[-4:-2]+'00'
byear=birthday[-4:]
leap_year=check_leap(byear)
century_code=get_century_code(bcentury)
year_code=(int(birthday[-2:])//4 + int(birthday[-2:]))%7
target_day=int(date_target[:2])
target_month=int(date_target[3:-5])
target_year=int(date_target[-4:])


def get_day_of_year(day_code,month_code,century_code,leap_year,year_code):
  mod=(int(year_code) + int(month_code) + int(century_code) + int(day_code) -leap_year)%7
  if (mod==0):
    print('You are born on Sunday \n')
  if (mod==1):
    print('You are born on Monday \n')
  if (mod==2):
    print('You are born on Tuesday \n')
  if (mod==3):
    print('You are born on Wednesday \n')
  if (mod==4):
    print('You are born on Thursday \n')
  if (mod==5):
    print('You are born on Friday \n')
  if (mod==6):
    print('You are born on Saturday \n')
    
    
print('\n'*2)    
get_day_of_year(day_code,month_code,century_code,leap_year,year_code)
    
daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def Count_Days(year1, month1, day1):
    if month1 ==2:
        if isLeapYear(year1):
            if day1 < daysOfMonths[month1-1]+1:
                return year1, month1, day1+1
            else:
                if month1 ==12:
                    return year1+1,1,1
                else:
                    return year1, month1 +1 , 1
        else: 
            if day1 < daysOfMonths[month1-1]:
                return year1, month1, day1+1
            else:
                if month1 ==12:
                    return year1+1,1,1
                else:
                    return year1, month1 +1 , 1
    else:
        if day1 < daysOfMonths[month1-1]:
             return year1, month1, day1+1
        else:
            if month1 ==12:
                return year1+1,1,1
            else:
                    return year1, month1 +1 , 1
                
def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    if y1 > y2:
        m1,m2 = m2,m1
        y1,y2 = y2,y1
        d1,d2 = d2,d1
    days=0
    while(not(m1==m2 and y1==y2 and d1==d2)):
        y1,m1,d1 = Count_Days(y1,m1,d1)
        days+=1
    return days


from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi
from matplotlib.dates import DateFormatter
from datetime import date

x = daysBetweenDates(int(byear), int(bmonth), int(day_code), target_year, target_month, target_day) 


# add ordinal date value 
ordinal_date_value=date(int(byear), int(bmonth), int(day_code)).toordinal() - date(1, 1, 1).toordinal()

t1 = arange(x-15, x+15, 1)
t = arange(ordinal_date_value+x-15, ordinal_date_value+x+15, 1)
y = [0,-1, 1]
x1 = [x+ordinal_date_value,x+ordinal_date_value,x+ordinal_date_value]
fig = figure(1)
ax1 = fig.add_subplot(111)
ax1.grid(True)
ax2=ax1.twinx()
ax2.plot(t, sin((2*pi*t1)/23),label='Physical')
ax2.plot(t, sin((2*pi*t1)/28),label='Intelectual')
ax2.plot(t, sin((2*pi*t1)/33),label='Emotional')
ax1.set_xlabel('DATES')
ax2.set_title('Biorhythim')
ax2.set_ylim((-1, 1))
ax1.set_ylim((-100, 100))
ax1.set_ylabel('PERCENTAGE %')
ax2.plot(x1, y , color='black',label='Target date')
ax2.plot(x+ordinal_date_value,sin((2*pi*(x))/23), marker='o', color='navy')
ax2.plot(x+ordinal_date_value,sin((2*pi*(x))/28), marker='o', color='orange')
ax2.plot(x+ordinal_date_value,sin((2*pi*(x))/33), marker='o', color='green')
ax2.legend(bbox_to_anchor=(1.20,1), loc="upper left")
date_form = DateFormatter("%d/%m/%Y")
ax2.xaxis.set_major_formatter(date_form)
ax1.xaxis.set_tick_params(rotation=30, labelsize=10)

for label in ax1.get_xticklabels():
    label.set_color('r')

show()

print('Target day on '+date_target+' your physical biorhytim is at '+str(round(sin((2*pi*x)/23)*100)) +'%')
print('Target day on '+date_target+' your intelectual biorhytim is at '+str(round(sin((2*pi*x)/28)*100)) +'%')
print('Target day on '+date_target+' your emotional biorhytim is at '+str(round(sin((2*pi*x)/33)*100)) +'%')
