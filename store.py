# 2019.07.01
storage ={}
def init(data):  #初始化
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
init(storage)
print(storage)

def lookup(data, label, name): #获取人员姓名
    return data[label].get(name)

print(lookup(storage, 'middle','Lie'))

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

MyNames = {}
init(MyNames)
store(MyNames, 'Magnus Lie Hetland')
print(lookup(MyNames, 'middle', 'Lie'))
store(MyNames, 'Anne Lie Hetland')
print(lookup(MyNames, 'middle', 'Lie'))
store(MyNames, 'Robin hood')
print(lookup(MyNames, 'first', 'Robin'))