def foo(req, *args, **kwargs):
    print(req)
    print(args)
    print(kwargs)

foo(1, 2, 3, 4, zi=1, di=2)

#*args - zmienna liczba argumentów funkcji, która jest zamieniana na tuple
#**kwargs - zmienna liczba słów kluczowych funkcji, która zamieniana jest na słownik