from discussion.db_handler.mysql_dbconn import DbConnection
from discussion.db_handler.db_vars import (
    ENDPOINT_URL,
    USERNAME,
    PASSWORD,
    DB_NAME
)

def delete_db_info():
    my_db = DbConnection(host=ENDPOINT_URL, user=USERNAME, passwd=PASSWORD, db_name=DB_NAME)
    my_db.call_sp("sp_ERASE_ALL_DATA", "none", *[])


if __name__ == "__main__":
    delete_db_info()