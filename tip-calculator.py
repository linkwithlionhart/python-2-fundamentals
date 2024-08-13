# declare variables
meal = float(44.50)
tax = float(6.75/100)
tip = float(15/100)

# reassign
meal = meal + meal * tax
total = meal + meal * tip

# process
total = round(total, 2)
print 'Server: the total comes to $%s' % total