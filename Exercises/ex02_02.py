'''
Think Python 2 - Exercise 2-2
'''

# Question 3
start_time = '6:52'
print('Start time:', start_time)
start = start_time.split(':')
start_hour = int(start[0])
start_minutes = int(start[1])
run_minutes = int(2*8.25 + 3*(7 + (12/60)))
if start_minutes + run_minutes > 60:
    end_hour = start_hour + int((start_minutes + run_minutes)//60)
    end_minutes = (start_minutes + run_minutes) - 60
else:
    end_hour = start_hour
    end_minutes = (start_minutes + run_minutes)
print('Finish time: {0}:{1}'.format(end_hour, end_minutes))
