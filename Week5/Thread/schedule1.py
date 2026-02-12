from schedule import*
import time
 
# Functions setup
def sudo_placement():
    print("Get ready for Sudo Placement")
 
def good_luck():
    print("Good Luck for Test")
 
def work():
    print("Study and work hard")
 
def bedtime():
    print("It is bed time go rest")
     
def test():
    print("Yeabsira says Good")
 
# Task scheduling
# After every 1mins test() is called.
every(1).minutes.do(test)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    run_pending()
    time.sleep(1)

 
# # After every hour test() is called.
# schedule.every().hour.do(test)
 
# # Every day at 12am or 00:00 time bedtime() is called.
# schedule.every().day.at("00:00").do(bedtime)
 
# # After every 5 to 10mins in between run work()
# schedule.every(5).to(10).minutes.do(work)
 
# # Every monday good_luck() is called
# schedule.every().monday.do(good_luck)
 
# # Every tuesday at 18:00 sudo_placement() is called
# schedule.every().tuesday.at("18:00").do(sudo_placement)
