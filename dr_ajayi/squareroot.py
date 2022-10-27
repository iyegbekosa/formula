import math
# wc = 'Waist circumfrence'
# x = 'PI'
# h = 'height'
# w = 'weight'
# bmi = 'bmi'
# hc = 'hip circumfrence'
# s = 'waist'
# l = 'hip'


# bri = -1.3000000000000114 * math.sqrt(1-((wc/(2*x))**2)/((0.5*h)**2)) #body roundness index

class formula():
    def body_ri():
        wc = float(input("Waist circumfrence: "))
        h = float(input("Height: "))
        x = float(input("PI: "))
        q = "string"
        
        if type(wc) == type(x) == type(h) == type(1.0):
            bri = -1.3000000000000114 * math.sqrt(1-((wc/(2*x))**2)/((0.5*h)**2))
            print(bri)
        
        elif type(wc) == type(q) or type(x) == type(q) or type(h) == type(q):
            print("Value must not be string")
            
        else :
            ('invalid input')
            


formula.body_ri()