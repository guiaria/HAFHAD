import sqlite3



def db_connect():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS user(cmd_id int PRIMARY KEY,time_execute datetime default current_timestamp,command_type char(16) NOT NULL, command_description char(16)  )''')
    print("Successful")

    return conn

def main():
    db_connect()

if __name__ == '__main__':
    main()
#conn.close()