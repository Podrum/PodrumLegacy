"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

import decimal

class BCMath:
    @staticmethod
    def bcmul(num1, num2, scale=None):
        if scale != None:
            decimal.getcontext().prec = scale
        result = decimal.Decimal(num1) * decimal.Decimal(num2)
        return int(result)
      
    @staticmethod
    def bcdiv(num1, num2, scale=None):
        if scale != None:
            decimal.getcontext().prec = scale
        result = decimal.Decimal(num1) / decimal.Decimal(num2)
        return int(result)
       
    @staticmethod
    def bcadd(num1, num2, scale=None):
        if scale != None:
            decimal.getcontext().prec = scale
        result = decimal.Decimal(num1) + decimal.Decimal(num2)
        return int(result)
    
    @staticmethod
    def bcsub(num1, num2, scale=None):
        if scale != None:
            decimal.getcontext().prec = scale
        result = decimal.Decimal(num1) - decimal.Decimal(num2)
        return int(result)
    
    @staticmethod
    def bccomp(num1, num2):
        result = (int(num1) > int(num2)) - (int(num1) < int(num2))
        return int(result)
    
    @staticmethod
    def bcmod(num1, num2):
        result = int(num1) % int(num2)
        return int(result)
    
    @staticmethod
    def bcpow(num1, num2):
        result = int(num1) ** int(num2)
        return int(result)
    
    @staticmethod
    def bcpowmod(num1, num2, mod):
        result = pow(num1, num2, mod)
        return int(result)
    
    @staticmethod
    def bcscale(scale):
        result = decimal.getcontext().prec = scale
        return int(result)
    
    @staticmethod
    def bcsqrt(num):
        result = math.sqrt(num)
        return int(result)

