# write a python program to find simple intrest
def simple_intrest(p,t,r):
    print(f"The principal is {p}")
    print(f"The interst of rate is {r}")
    print(f"The time period is {t}")
    si = (p * t * r)/100
    print(f"The simple intrest is {si}")
    return simple_intrest
simple_intrest(6,7,8)
