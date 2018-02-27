x = input('name?')
user ={
    'son':{
        'tuoi': '26',
        'sex': 'nam',
        'so thich': 'da bong'
            },
    'yen':{
        'tuoi': '24',
        'sex': 'nu',
        'so_thich': 'hat'
            }
}
for v in user:
    if x == v:
        print(user[v])
        break
else:
    print('not')
