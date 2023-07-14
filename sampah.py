trash_organic = ['leaf', 
                 'fruit skin', 
                 'food waste', 
                 'decomposed fruits & vegetables',] 

trash_inorganic = ['bottle waste', 
                   'glass', 
                   'book', 
                   'paper']

with open('organic.txt', 'w', encoding='UTF-8') as f:
    for i in trash_organic:
        f.write(i + '\n' )
    f.close()

with open('inorganic.txt', 'w', encoding='UTF-8') as f:
    for i in trash_inorganic:
        f.write(i + '\n')
    f.close()