amount = 1000
gst = ((1000*18)/100)
total = amount + gst 

if total > 1000:
    dis = total*0.10
    total -=dis
    print(total)
else:
    print("Final amount:",total )
