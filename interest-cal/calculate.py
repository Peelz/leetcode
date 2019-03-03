def calculate (**kwarg):
    total_pay = kwarg['installment'] * kwarg['month']
    total_pay_with_down = total_pay + kwarg['down_cost']
    settlement = total_pay_with_down - kwarg['item_price']
    interest_per_month = float(settlement) / float(kwarg['month'])
    
    interest_per_month_percentage = 100 * interest_per_month/ total_pay_with_down

    print ("\n")

    for i in kwarg:
        print("%s--%s" % (i, kwarg[i]) )

    print ("\n")
    print ("#"*48)
    print ("\n")

    print ("Total Pay(exclude down): %s"% total_pay)
    print ("Total Pay(include down): %s"% total_pay_with_down)

    print ("\n")

    print ("Settlement: %s - %s = %s"% (total_pay_with_down, item_price,settlement))
    print ("\n")

    print ("real pay from %s is %s" % (installment, installment - interest_per_month))
    print ("\n")

    print ("Interest / month (number): %s"% interest_per_month)
    print ("Interest / month (percentag): %s"% interest_per_month_percentage)
    print ("Interest / year (percentag): %s"% (interest_per_month_percentage*12) )



if __name__ == "__main__":
    import Tkinter as tkinter

    top = tkinter.Tk()
    # Code to add widgets will go here...
    top.mainloop()
    # mode = input("(1) default (0) mannual: ")
    # if mode == 1:
    #     item_price = 188000
    #     down_cost = 18800
    #     installment = 5687
    #     month = 36
    #     # calculate(item_price=item_price, down_cost=down_cost, installment=installment, month=month)
    # else :
    #     print ("Item price: ")
    #     item_price = input()
    #     print ("Down: ")
    #     down_cost = input()
    #     print ("Installment: ")
    #     installment = input()
    #     print ("Month: ")
    #     month = input()

    # calculate(item_price=item_price, down_cost=down_cost, installment=installment, month=month)
