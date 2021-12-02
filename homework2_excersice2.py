from datetime import date, datetime, timedelta
#dt_today = datetime.now()
#delta = timedelta(1)
#delta2 = timedelta(30)
#dt_yesterday = dt_today - delta
#dt_30_days_ago = dt_today - delta2
#print(dt_today, dt_yesterday, dt_30_days_ago)


date_string = input('Введите дату по формату "день/месяц/год часов:минут:секунд.милисекунд": ')

def datetimer(date_string):
    date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date_dt
activate = datetimer(date_string)
print(activate)