from functools import reduce

data = [2.18,5.7,4.6,1.2,3.5,2.111]

area = list(map(lambda x: x**2*3.14, data))
print(area)
#funkcja map wykonuje funkcję na każdym elemencie listy... i zwraca obiekt map(będący iteratorem)

fit = list(filter(lambda x: x > 3, data))
print(fit)
#funkcja filter sprawdza funkcją elementy naszej listy i zwraca obiekt filter, który posiada elementy, które spełniły warunek funkcji

red = reduce(lambda x,y: x*y, data)
print(red)
#funkcja reduce wykonuje funkcję na każdym elemencie listy z wynikiem z poprzednich iteracji, na dole identyczne działanie tylko z forem
tmp = 1
for i in data: tmp = tmp * i
print(tmp)