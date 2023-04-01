import sqlite3
import random
import textwrap as tw
	
			
def info():
	'''
	Метод открывает файл Readme.txt
	для ознакомления с работой программы
	'''
	    
	with open('Readme.txt', 'r') as f:
		for line in f:
			print(f'\t{line}')

#----------------------------------------------				
def Data_recording ():	
	
	'''
	Функция дает пользователю ввести 
	данные для записи в БД function.db
	'''
	
	Type = input('Введите тип данных: ')
	Function = input('Введите метод: ')
	Arguments = input('Введите аргументы функции: ')
	Description = input('Введите описание функции: ')
		
	# список введенных данных
				
	values = [type, method ,Arguments, description]
	    
	# запись данных в таблицу function.db
	    
	with sqlite3.connect('function.db') as db:
		cursor = db.cursor()
		cursor.execute("""INSERT INTO function 
		(type, 
		 method, 
		 arguments, 
		 description) VALUES(?, ?, ?, ?)""",values)
		
		db.commit()
			
	print('\v\tФункция добавленна')
	
#----------------------------------------------		
def vizov ():	 
    	
	Type_vizov = input('\v\tВведите тип метода:\n\t_list_\t_str_\t_dict_\t_set_\t_tuple_\n\t_sql_')
	
	'''
	Функция выводит из базы данных 
	кортеж  выбранных элементов 
	'''			
						
	with sqlite3.connect('function.db') as db:
			cursor = db.cursor()
			rows = cursor.execute(
			f"SELECT * FROM function WHERE type LIKE '{Type_vizov}'"). fetchall() 
	stroka = random.choice(rows)
	#взять один элемент из кортежа
		
	print(f'\t\v{stroka[:2]}')
	input()
	print(f'\t\v{stroka[2]}') 
	input()
	print(f'\v{tw.fill(stroka[3], 30,)}')
	input()
	

					
		
		
	
		
	
		
		