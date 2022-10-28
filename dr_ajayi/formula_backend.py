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
        s = float(input("waist: "))
        l = float(input("hip: "))
        q = "string"
        
        if type(s) == type(l) == type(1.0):
            a_vi = ( 2* (s**2) + 0.7 * (s - l)**2 ) / 1000
            print(a_vi)
        
        elif type(s) == type(q) or type(l) == type(q):
            print("Value must not be string")
            
        else :
            ('invalid input')

    
    def bsi():
        """for adolescents adjusted body shape index"""
        wc = float(input("Waist circumfrence: "))
        h = float(input("Height: "))
        bmi = float(input("Body mass index: "))
        q = "string"
        
        if type(wc) == type(h) == type(bmi) == type(1.0):
            b_si = wc / bmi**0.45 * h**0.55
            print(b_si)
        
        elif type(wc) == type(q) or type(h) == type(q):
            print("Value must not be string")
            
        else :
            ('invalid input')

    
    def whpr():
        """waist hip ratio"""
        hc = float(input("Hip circumfrence: "))
        wc = float(input("Waist circumfrence: "))
        q = "string"
        
        if type(wc) == type(hc) == type(1.0):
            w_hpr = wc / hc
            print(w_hpr)
        
        elif type(hc) == type(q) or type(wc) == type(q):
            print("Value must not be string")
            
        else :
            ('invalid input')

    
    def whtr():
        """waist height ratio"""
        wc = float(input("Waist circumfrence: "))
        h = float(input("Height: "))
        q = "string"
        
        if type(wc) == type(h) == type(1.0):
            w_htr = wc / h
            print(w_htr)
        
        elif type(wc) == type(q) or type(h) == type(q):
            print("Value must not be string")
            
        else :
            ('invalid input')