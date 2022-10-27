import math
# bri = 364.2 - 365.5
# print(bri)
wc = 'Waist circumfrence'
x = 'PI'
h = 'height'
w = 'weight'
bmi = 'bmi'
hc = 'hip circumfrence'
s = 'waist'
l = 'hip'


bri = -1.3000000000000114 * math.sqrt(1- ( (wc / (2 * x) ) **2) / ( (0.5*h) **2) ) #body roundness index

ci = wc / ( 0.109 * math.sqrt( w / h ) ) #conicity index

absi = wc / ((bmi**2/3) * (h**1/2) ) #A body shape index

bai = (hc / h**1.5) -18 #body adipocity index

avi = ( 2* (s**2) + 0.7 * (s - l)**2 ) / 1000 #abdominal volume index

bsi = wc / bmi**0.45 * h**0.55 #for adolescents adjusted body shape index

whpr = wc / hc #waist hip ratio

whtr = wc / h #waist height ratio

class FORMULA ():
    def bri():
        """body roundness index"""
        
        print("BRI")
        
    def cl():
        """conicity index"""
        print("CL")
    
    def absi():
        """A body shape index"""
        print("CL")
    
    def bai():
        """body adipocity index"""
        print("CL")
    
    def avi():
        """abdominal volume index"""
        print("CL")
    
    def bsi():
        """for adolescents adjusted body shape index"""
        print("CL")
    
    def whpr():
        """waist hip ratio"""
        print("CL")
    
    def whtr():
        """waist height ratio"""
        print("CL")
