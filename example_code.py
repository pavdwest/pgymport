from src.db_client import DbClient


c = DbClient(
    server="localhost",
    database="testdb2",
    username="postgres",
    password="pwn123#"
)

c.load_file(
    filepath="data/friends.csv"
)
