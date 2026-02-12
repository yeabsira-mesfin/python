print("Please Enter your three test scores: and I will tell you if you passed or failed.")

con = 'y'
while con == 'y':
    score1 = float(input("Enter your first test score:"))
    score2 = float(input("Enter your second test score:"))
    score3 = float(input("Enter your third test score:"))
    total = (score1 + score2 + score3)
    avg = total / 3

    if avg >= 70:
        print(f"Congraturlations you passed with a total score of {total} and an average score of {avg}")
    else:
        print(f"Sorry, you failed with a total score of {total} and an average score of {avg}")
        
    print("===============================================")
    con = input("Do you want to enter another set of scores? enter y to continue or enter anyother key to stop: ")
                     