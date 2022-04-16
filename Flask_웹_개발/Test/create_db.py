import sqlite3

conn = sqlite3.connect('over_speeding.db')
print('Database creation successful')

conn.execute(
        '''
        create table Testcases (
        case_ integer, 
        image_path text, 
        information text, 
        datetime text)
        '''
)
print('Table creation successful')
conn.close()
