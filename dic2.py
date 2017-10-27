dic1 = {}
dic2 = {}
dic3 = {}

dic1["1"] = "10"
dic1["2"] = "20"
dic2["3"] = "30"
dic2["4"] = "40"
dic3["5"] = "50"
dic3["6"] = "60"
dictotal = dict(dic1.items() + dic2.items() + dic3.items())
print dictotal
