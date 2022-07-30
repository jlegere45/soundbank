"""user_table actions this is just a small collection of functions
   caller needs to handle errors"""
from src.database.db_connect import setup_connection

conn, curr = setup_connection()

def insert_user(username, email, content_name=None, content_url=None,
                content_about=None):
    curr.execute("INSERT INTO users_table (username, email, registered) \
                 VALUES (%s, %s, %s) RETURNING id, username, email",
                (username, email, False))
    result = curr.fetchone()
    conn.commit()
    return result


def set_content_creator():
    curr.close()
    conn.close()

def search_for_user():
    curr.close()
    conn.close()

def get_user(id=None, username=None, email=None):
    if id != None:
        curr.execute("SELECT * FROM users_table WHERE id = %s", (id,))
    elif username != None:
        curr.execute("SELECT * FROM users_table WHERE username = %s", (username,))
    elif email != None:
        curr.execute("SELECT * FROM users_table WHERE email = %s", (email,))
    else:
        return None
    return curr.fetchone()


def set_session_token():
    curr.close()
    conn.close()
    
    
def register_email():
    curr.close()
    conn.close()
    
    
def delete_user(username=None, email=None, id=None):
    if id == None:
        curr.execute("DELETE FROM users_table WHERE username = %s and email = %s", (username, email))
    else:
        curr.execute("DELETE FROM users_table WHERE id = %s", (id,))
    result = conn.commit()
    return result