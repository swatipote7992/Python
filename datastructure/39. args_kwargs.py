def sum_args(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_args(1,2,3,4))

def sum_kwargs(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum += v
    print(f"{sum:.2f}")
    return round(sum,2)

print(sum_kwargs(coffee=2.99, cake=4.55, juice=2.99))
