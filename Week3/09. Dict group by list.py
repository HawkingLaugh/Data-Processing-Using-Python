def func(stu_list):
    d = {}
    for item in stu_list:
        r = item.split('_')
        a, b = r[0], r[1].strip()
        if a not in d:
            d[a] = [b]
        else:
            d[a] += [b]
    sorted(d.items(), key = lambda d: len(d[1]))
    return d

if __name__ == "__main__":
    try:
        with open('sports_day.txt', 'r+') as f:
            stu_list = f.readlines()
    except FileNotFoundError as err:
        print(err)
    else:
        print(func(stu_list))