import csv
with open('mydata.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(('one', 'two', 'three'))
    writer.writerow(('1', '2', '3'))
    writer.writerow(('4', '5', '6'))
    writer.writerow(('7', '8', '9'))
