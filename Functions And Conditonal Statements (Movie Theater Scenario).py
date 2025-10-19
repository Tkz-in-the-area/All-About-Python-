FUNCTIONS AND CONDITIONAL STATEMENTS
(Movie Theater Scenario)

-- Looking At Total Sales --
# Define a function named `total_sales`
def total_sales():

    # Return a value
    return
    
   # Add a parameter to the function
def total_sales(n):

    # Multiply the parameter by the ticket price to get total sales(ticket price = $7.99)
    return n * 7.99 

# Call the function / Test the function
total_sales(59)

# Refine the `total_sales` function / Instance where ticket price changes e.g Opening Night / Movie premier / V.I.P tickets
def total_sales(price, num_tickets):
    return round(price * num_tickets, 2)
    
 # Call the function with two values / Returned with Two Decimal places (USD)
total_sales(15.99, 1001)

--------------------------------------------------------------------------------------------------------------------------------------
# Define function / Marketing Wants to Reward Regular Customers with [Discount/Voucher/Promo-Code=coupon]
def send_email(num_visits, visits_email):
    if num_visits >= visits_email:
        print('Send email.')
    else:
        print('Not enough visits.')
        
send_email(num_visits=3, visits_email=5)    # Should print 'Not enough visits.'
send_email(num_visits=5, visits_email=5)    # Should print 'Send email.'
send_email(num_visits=15, visits_email=10)  # Should print 'Send email.'

# Adding Logical Branching to Filter Those Appplicable for Reward(coupon)
def send_email(num_visits, visits_email, visits_coupon):
    if num_visits >= visits_coupon:
        print('Send email with coupon.')
    elif num_visits >= visits_email:
        print('Send email only.')
    else:
        print('Not enough visits.')
        
send_email(num_visits=3, visits_email=5, visits_coupon=8)   # Should print 'Not enough visits.'
send_email(num_visits=5, visits_email=5, visits_coupon=8)   # Should print 'Send email only.'
send_email(num_visits=6, visits_email=5, visits_coupon=8)   # Should print 'Send email only.'
send_email(num_visits=8, visits_email=5, visits_coupon=8)   # Should print 'Send email with coupon.'
send_email(num_visits=10, visits_email=5, visits_coupon=8)  # Should print 'Send email with coupon.'


