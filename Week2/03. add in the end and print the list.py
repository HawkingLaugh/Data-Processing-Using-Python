s = 'Orcale'
with open('companies.txt', mode='a+') as f1:
    f1.writelines('\n')
    f1.writelines(s)
    # after writelines, the file pointer will go to tail of the file, therefore the next line will read nothing. use seek() method
    f1.seek(0)
    cNames = f1.readlines()
print(cNames)