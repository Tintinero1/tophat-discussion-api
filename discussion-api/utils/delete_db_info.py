from discussion.db_handler.mysql_dbconn import DbConnection
from discussion.db_handler.db_vars import (
    ENDPOINT_URL,
    USERNAME,
    PASSWORD,
    DB_NAME
)

def delete_db_info():
    my_db = DbConnection(host=ENDPOINT_URL, user=USERNAME, passwd=PASSWORD, db_name=DB_NAME)
    my_db.execute_and_fetch("""
        SET FOREIGN_KEY_CHECKS = 0;

        TRUNCATE table Comment;
        TRUNCATE table Discussion_Question;
        TRUNCATE table Rel_Comment_Response;
        TRUNCATE table Rel_Discussion_Question_Response;

        SET FOREIGN_KEY_CHECKS = 1;
    """, 'none')


if __name__ == "__main__":
    delete_db_info()