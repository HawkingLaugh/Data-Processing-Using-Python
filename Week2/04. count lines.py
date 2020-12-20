countList = []
try:
    with open('Lorem.txt', 'r+') as f1:
        countList = f1.readlines()
except FileNotFoundError:
    print('file not found')
count = len(countList)
print("Lorem.txt has", str(count), "lines")

def countLines(fname):
    data = ''
    try:
        with open(fname) as f:
            data = f.readlines()
    except FileNotFoundError:
        print(fname, 'file not found')
    lens = len(data)
    print(fname, 'has', str(lens), 'lines')

files = ['1Lorem.txt', '2Lorem.txt', '3Lorem.txt', '4Lorem.txt', ]
for file in files:
    countLines(file)