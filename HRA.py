def HRA(month_basic, monthly_HRA,monthly_DA,monthly_rent,commission):
    Annual_amount= ((month_basic *12) + (monthly_DA *12) + commission)
    Annual_HRA = (monthly_HRA*12)
    Annual_rent = (monthly_rent*12)
    salary = (Annual_rent - (Annual_amount/100*10))
    return salary
x= HRA(10000,5000,4000,6000,0)
print('xxxxxx',x) 
    
