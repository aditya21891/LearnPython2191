principal=500000.0
rate=0.05
payment=2684.11  
total_paid=0.0
while principal >0:
  principal=principal*(1+rate/12) - apay
  total_paid=total_paid + payment 
  
print ("Total Paid :",total_paid)
  
  
