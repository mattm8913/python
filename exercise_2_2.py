
def main():
    charge_per_hour=0.51
    per_day=charge_per_hour*24
    per_month=per_day*(365/12)
    print('One server per day = {0:.2f}'.format(per_day))
    print('One server per month = {0:.2f}'.format(per_month))
    saved=918
    one_server_time=saved/per_day
    print('Twenty servers per day cost = {0:.2f}'.format(per_day*20))
    print('Twenty servers per month cost = {0:.2f}'.format(per_month*20))
    print('Days at one server = {}'.format(one_server_time))
    print('Days at twenty servers = {0:.2f}'.format(one_server_time/20))
