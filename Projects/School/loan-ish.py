print("For each question, answer with a 1-10 rating:")

loan_size = int(input("How large is the loan?\n"))
credit_score = int(input("How good is your credit history?\n"))
income = int(input("How high is your income?\n"))
down_payment = int(input("How large is your down payment?\n"))

loan_ish = False

if loan_size >= 5:
    if credit_score >= 7 and income >= 7:
        loan_ish = True
    elif credit_score >= 7 or income >= 7:
        if down_payment >= 5:
            loan_ish = True
        else:
            loan_ish = False
    else:
        loan_ish = False
else:
    if credit_score < 4:
        loan_ish = False
    else:
        if income >= 7 or down_payment >= 7:
            loan_ish = True
        elif income >= 4 and down_payment >= 4:
            loan_ish = True
        else:
            loan_ish = False

if loan_ish:
    print("The decision is yes. This is a good loan.")
else:
    print("The decision is no. You should not loan this money.")