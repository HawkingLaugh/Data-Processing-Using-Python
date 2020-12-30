import random

def func(data):
    cls_no = random.choice(list(data.keys()))
    stu_no = random.randint(1, data[cls_no])
    return '{}{:02}'.format(cls_no, stu_no)

if __name__ == "__main__":
    data = {"A001":304, "A002":200, "B001":320, "B002":130}
    # create a empty set to place result and avoid duplicate
    result = set()
    while len(result) < 10:
        result.add(func(data))
    for i in result:
        print(i)
    
