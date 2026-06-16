years = [2026, 2027]
Months = ['jan','feb']
days = range(1,29)

for y in years:
    for m in Months:
        for d in days:
            print(f'report_{y}_{m}_{d}')




tables = ['customers','orders','products','price']
coloumn = ['id','create_id']

for t in tables:
    for c in coloumn:
        print(f'SELECT count(*) from {t}WHERE C IS Null')


colors = ['red','green','blue']
sizes = ['L','M','S']

for color in colors:
    for size in sizes:
        print(f'{color} - size(size)')