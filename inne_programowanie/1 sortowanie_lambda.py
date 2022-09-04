
zbior = [
    "Adam",
    "Ewaryst",
    'Miłosz',
    'Samuel'
]
size = lambda z: z[2]
zbior.sort(key=size)

zibi = sorted(zbior, key=lambda z:z[2])

print(zbior)
print(zibi)