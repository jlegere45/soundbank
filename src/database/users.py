"""user_table actions this is just a small collection of functions
   caller needs to handle errors"""
from src.database.db_connect import setup_connection

conn, curr = setup_connection()

def insert_user(username, email, password, content_name="", content_url="",
                content_about=""):
    """_summary_

    Args:
        username (string)
        email (string)
        password (string)
        content_name (string, optional). Defaults to empty string.
        content_url (string, optional). Defaults to empty string.
        content_about (string, optional). Defaults to empty string.

    Returns:
        tuple: (id, username, email)
    """
    curr.execute("INSERT INTO users_table (username, email, registered, password) \
                 VALUES (%s, %s, %s, %s) RETURNING id, username, email",
                (username, email, False, password))
    result = curr.fetchone()
    conn.commit()
    if len(content_name) > 1:
        curr.execute("UPDATE users_table SET content_name=%s, content_about=%s, content_url=%s \
                VALUES (%s, %s, %s) RETURNING id, username, email",
            (username, email, False, password))
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