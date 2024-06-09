def sleep_in(weekday, vacation):
    if(weekday and not vacation):
        return False
    else:
        return True
    
print(sleep_in(True, False))
print(sleep_in(True, True))
