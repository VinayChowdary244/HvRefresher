product_1 = int(input('quantity of first product :'))
product_2 = int(input('quantity of second product :'))
product_3 = int(input('quantity of third product :'))

if((product_1<=0) or (product_2<=0) or (product_3<=0)):
    print('please enter a positive value')
else:
    print('product quantity with price')
    total = product_1*300 + product_2*400 + product_3*500
    entries = { product_1: 300,product_2 : 400 , product_3 : 500}
    for i,p in entries.items():
        print(i,p)
    print('the amount that you need to pay is :')
    print(total)