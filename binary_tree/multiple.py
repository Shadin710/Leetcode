def fun(num):
    if num==4:
        return 2
    else:
        return 2*fun(num+1)

if __name__ == '__main__':
    num=2
    print(fun(num))