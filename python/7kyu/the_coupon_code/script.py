from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code != correct_code:
        return False
    elif type(entered_code) != type(correct_code):
        return False
    else: 
        if datetime.strptime(current_date, "%B %d, %Y") <= datetime.strptime(expiration_date, "%B %d, %Y"): return True
        else: return False
