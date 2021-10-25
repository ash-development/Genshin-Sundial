# ./Utils/Function.py
# @author : Chtholly2000
# @created : 2021-AUG-02 18:53
# @last updated : 2021-OCT-06 19:39

#Adds a comma to every 3rd digit
def comma(num):
  if type(num) == int:
    return '{:,}'.format(num)
  elif type(num) == float:
    return '{:,.2f}'.format(num)
  else:
    print("Need int or float as input to function comma()!")
    
#Week function
def week(day):
  if day == 7 : return 0#SUN
  elif day == 6 : return 6#MON
  elif day == 5 : return 5#TUE
  elif day == 4 : return 4#WED
  elif day == 3 : return 3#THU
  elif day == 2 : return 2#FRI
  else : return 1#SAT   

#Hour function
def hour(h):
  if h >= 0 and h < 4 : return 3 - h
  else : return 23 - abs(4-h)
    
#Minute function
def minute(m):
  if m == 0 : return 0
  else: return 60 - m

#Singular Day Function 
def sing_day(D):
  if D == 1 : return 'day'
  else : return 'days'

#Singular Hour Function
def sing_hour(hour):
  if hour == 1 : return 'hour'
  else : return 'hours'

#Singular Minute Function
def sing_minute(Min):
  if Min == 1 : return 'minute'
  else : return 'minutes' 