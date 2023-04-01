import sqlite3
import Def
import random
import textwrap as tw

# ⏬ создание БД 

with sqlite3.connect('function.db') as db:
	cursor = db.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS function (
		type TEXT, 
		method TEXT,
		arguments TEXT,
		description TEXT)""")
	db.commit()

Def.info()
print('\v')

while True:
    
    # ⏬ Выбор действия
    
    Action_add_or_teach =input('\v\tДля добавления нового метода\n\tВведите:1\n\n\tДля тренировки\n\tВведите: 2\n\n\t')
    
    # ⏬ Добавление нового метода в БД 

    if Action_add_or_teach == '1':
        Def.Data_recording()
	
    # ⏬ Тренировка 

    if Action_add_or_teach == '2':
    	while True:
            Def.vizov() 
    			
					  	        			  	        	


    		
    		
    
 
    		
    				
	    
	    
	





		
		
				


		




