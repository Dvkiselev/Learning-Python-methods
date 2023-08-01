import os
import sqlite3

        
def creating_table():

    '''
    Создает базу данных
    '''
    
    name_db = input('Напишите название новой БД: ')
    name = input('напишите название полей через запятую:\n')
    # создание полей
    name = ','.join([i + ' TEXT' for i in name.split(',')])    
    # создание БД
    with sqlite3.connect(f'{name_db}.db') as db: 
             cursor = db.cursor() 
             cursor.execute(f"""CREATE TABLE IF NOT EXISTS function ({name}, status)""") 
             db.commit() 


def choosing_db ():
    
    '''
    вывод всех баз данных в директории и выбор одной из них
    '''
    
    name_file = [x for x in os.listdir() if x.startswith('.db', -3) == True]
    print('выберете базу данных')
    print(*enumerate(name_file), sep = '\n')
    nam_db = int(input('введите номер БД -> '))
    return name_file[nam_db]



def data_entry_in_db():
    
    '''
    Добавление данных
    '''
    
    name_db = choosing_db()
    with sqlite3.connect(f'{name_db}') as db: 
        cursor = db.cursor() 8
        # получение полей таблицы
        cursor.execute("""SELECT* FROM function""")
        colnames = cursor.description
        list_colnames = [i[0] for i in colnames]
        # ввод значений 
        val = tuple(input(f'введите значенте {i}: ') for i in list_colnames)
        #добавлнрие значений
        cursor.execute(f"""INSERT INTO function  VALUES {val}""")
    return 'Данные добавлены'
        
     
   