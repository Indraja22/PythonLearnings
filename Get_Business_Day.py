from datetime import datetime, timedelta
import random

class Get_Business_Day:

    def get_planned_start_and_end_dates(self):
        random_int = random.randint(1,4)
        start_date = datetime.now() + timedelta(days=random_int)
        strt_dt = start_date

        random_int_1 = random.randint(10, 20)
        end_date = strt_dt + timedelta(days=random_int_1)
        end_dt = end_date

        while strt_dt.weekday() > 5 or end_dt.weekday() > 5:
                strt_dt = strt_dt + timedelta(days=1)
                end_dt = end_dt + timedelta(days=1)
        return strt_dt.strftime('%m/%d/%Y'), end_dt.strftime('%m/%d/%Y')
        
    def get_actual_date(self,planned_start_date,planned_end_date):
        planned_start_date_obj = datetime.strptime(planned_start_date,'%m/%d/%Y')

        random_int_start_date = random.randint(1,4)
        random_int_end_date = random.randint(1,10)

        actual_start_date = planned_start_date_obj + timedelta(days=random_int_start_date)
        actual_end_date = actual_start_date + timedelta(days=random_int_end_date)

        while actual_start_date.weekday() > 5 or actual_end_date.weekday() > 5:
            actual_start_date = actual_start_date + timedelta(days=1)
            actual_end_date = actual_end_date + timedelta(days=1)
        return actual_start_date.strftime('%m/%d/%Y'), actual_end_date.strftime('%m/%d/%Y')
    
    def calculate_cycle_time_business_days(self,planned_start_date, planned_end_date):
        planned_start_date_obj = datetime.strptime(planned_start_date,'%m/%d/%Y')
        planned_end_date_obj = datetime.strptime(planned_end_date,'%m/%d/%Y')
        business_days = 0
        start_dt = planned_start_date_obj
        end_dt = planned_end_date_obj
        while start_dt <= end_dt:
            if start_dt.weekday() < 5:
                business_days = business_days + 1
            start_dt += timedelta(days=1) 
        return business_days
    
    def check_lag_time_of_precedent_task(self,lag_days,start_date):
        start_date_obj = datetime.strptime(start_date,'%m/%d/%Y')
        while lag_days > 0:
            start_date_obj = start_date_obj + timedelta(days=1)
            if start_date_obj.weekday() < 5:
                lag_days = lag_days - 1
        return start_date_obj.strftime('%m/%d/%Y')


bus_date = Get_Business_Day()
print(bus_date.get_planned_start_and_end_dates())
start_dt, end_dt = bus_date.get_planned_start_and_end_dates()
print(bus_date.get_actual_date(start_dt, end_dt))
cyc_time = bus_date.calculate_cycle_time_business_days(start_dt, end_dt)
print(cyc_time)
lag_start_date = bus_date.check_lag_time_of_precedent_task(5,"12/26/2023")
print(f"{lag_start_date} is the new date")