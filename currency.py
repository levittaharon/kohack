import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4

currency=float(input("Please select one: 1.USD 2.CAD 3.GBP "))
convert_dir=float(input("Select original currency: 1.SHKL 2.Other"))
my_value=float(input("Value:"))

#The function needs 3 parameters, all for integer values. 
#First value: 1 for USD, 2 for CAD, 3 for GBP, and 4 for EUR.
#Second parameter is a 1 or 2-- A 1 lets us know that the final output should be in the foreign currency, a 2 for shekels
#Last parameter specifies the actual value you wish to convert. If a 1 is specified in the second parameter, this parameter 
#will be in shekels. If the second parameter is a 2, this will be in the specified foreign currency."""
def convert(orig, to_or_from, value_orig):
    cur=["EMPTY", 4500]
    my_url='https://google.com'
    spec_class='hello'
    match orig:
        case 1:
            cur[0]="USD"
            my_url='https://www.google.com/finance/quote/USD-ILS?sa=X&ved=2ahUKEwiDjLiU--b9AhXkmokEHdNqCEgQmY0JegQIBhAd'
            spec_class="YMlKec fxKbKc"
        case 2:
            cur[0]="CAD"
            my_url='https://www.google.com/finance/quote/CAD-ILS?sa=X&ved=2ahUKEwjq3cGLq-j9AhXGFFkFHbg7CDwQmY0JegQIBhAd'
            spec_class="YMlKec fxKbKc"
        #case 4:
        #    cur[0]="EUR"
        #    url='https://www.google.com/finance/quote/EUR-ILS?sa=X&ved=2ahUKEwjuyvisq-j9AhVBFFkFHfO2D68QmY0JegQIBhAd'
        #    spec_class="YMlKec fxKbKc"
        case 3:
            cur[0]="GBP"
            my_url='https://www.google.com/finance/quote/GBP-ILS?sa=X&ved=2ahUKEwjBiaHNq-j9AhUzVTUKHYb6Cj8QmY0JegQIBhAd'
            spec_class="YMlKec fxKbKc"
        case _:
            print("ERROR: Please try again")
    res= requests.get(my_url)
    soup = BeautifulSoup(res.content, 'html.parser')
    get_value = soup.find_all(class_=spec_class)[0].text
    conversion_factor=float(get_value)
    match to_or_from:
        case 2:
            cur[0]="SHKL"
            cur[1]=(conversion_factor*value_orig)
        case 1:
            cur[1]=(value_orig/conversion_factor)
        case _:
            print("ERROR")
    return(cur)

print(str(round(convert(currency, convert_dir, my_value)[1],2)))
print(convert(currency, convert_dir, my_value)[0])
