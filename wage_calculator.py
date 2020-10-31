year = 365
work_days = float (input('how many days do you work: '))
work_days_fraction = work_days/7
hours = float (input ('how many hours do you work a day: '))
wage = float (input('what is your wage: '))
tax_b = float (input('what is the tax rate: '))
tax_e = tax_b/100
tax = 1 - tax_e
print (year*work_days_fraction*hours*wage*tax)