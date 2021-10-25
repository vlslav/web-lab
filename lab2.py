class MyClass:
    d = {}
    
    def __init__(self, di):
        self.d = di
        
    def sum_odds(self, key):
        s = 0
        for v in self.d[key]:
            if v%2 > 0:
                s += v
        return s
            
    
o1 = MyClass({'d':[2],'c':[1,2,3,4],'a':[4,5,6,7,7]})
o2 = MyClass({'1':[1,6],'2':[1,9,3,4],'2':[4,6,7,7]})
o3 = MyClass({'12':[1,6,65,76],'14':[32452,9,3,4],'15':[443,6,7,7]})

print(o1.sum_odds('d'))
print(o2.sum_odds('2'))
print(o3.sum_odds('12'))
