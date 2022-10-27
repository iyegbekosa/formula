import math
# wc = 'Waist circumfrence'
# x = 'PI'
# h = 'height'
# w = 'weight'
# bmi = 'bmi'
# hc = 'hip circumfrence'
# s = 'waist'
# l = 'hip'



class formula():
    def bri():
        """body roundness index"""
        wc = float(input("Waist circumfrence: "))
        h = float(input("Height: "))
        x = float(input("PI: "))
        q = "string"
        
        if type(wc) == type(x) == type(h) == type(1.0):
            body_ri = -1.3000000000000114 * math.sqrt(1-((wc/(2*x))**2)/((0.5*h)**2))
            print(body_ri)
        
        elif type(wc) == type(q) or type(x) == type(q) or type(h) == type(q):
            print("Value must not be string")
            
        else :
            ('invalid input')
        
    def ci():
        """conicity index"""
        wc = float(input("Waist circumfrence: "))
        h = float(input("Height: "))
        w = float(input("Weight: "))
        q = "string"
        
        
        if type(wc) == type(w) == type(h) == type(1.0):
            co_i = wc / ( 0.109 * math.sqrt( w / h ) )
            print(co_i)
        
        elif type(wc) == type(q) or type(w) == type(q) or type(h) == type(q):
            print("Value must not be string")
            
        else :
            ('invalid input')
            
    def absi():
        """A body shape index"""
        wc = float(input("Waist circumfrence: "))
        h = float(input("Height: "))
        bmi = float(input("Body mass index: "))
        q = "string"
        
        if type(wc) == type(bmi) == type(h) == type(1.0):
            a_bsi = wc / ((bmi**2/3) * (h**1/2) )
            print(a_bsi)
        
        elif type(wc) == type(q) or type(bmi) == type(q) or type(h) == type(q):
            print("Value must not be string")
            
        else :
            ('invalid input')
    
    def bai():
        """body adipocity index"""
        hc = float(input("Hip circumfrence: "))
        h = float(input("Height: "))
        q = "string"
        
        if type(hc) == type(h) == type(1.0):
            b_ai = (hc / h**1.5) -18 #body adipocity index
            print(b_ai)
        
        elif type(hc) == type(q) or type(h) == type(q):
            print("Value must not be string")
            
        else :
            ('invalid input')
        
        
        
    
    def avi():
        """abdominal volume index"""
    
    def bsi():
        """for adolescents adjusted body shape index"""
    
    def whpr():
        """waist hip ratio"""
    
    def whtr():
        """waist height ratio"""

formula.bri()
