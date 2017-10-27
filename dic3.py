dic = {}
dic["a"] = "1"
dic["b"] = "2"
dic["c"] = "3"

check = raw_input("What to check?")

for key in dic.keys(): print "......."

if check in dic.keys(): print "Its in the dictionary!!!"
else: print "Sorry not in the dictionary :("
