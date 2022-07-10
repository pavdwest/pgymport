from typing import Optional


import typer


from db_client import DbClient


app = typer.Typer()


@app.command(name="upload")
def upload(
    filepath: str = typer.Option(..., help="Relative/full filepath including extension."),
    delimiter: str = typer.Option(",", help="Delimiter/Column Separator in file."),
    server: str = typer.Option("localhost", help="Server/Host on which the database resides."),
    database: str = typer.Option("pgymportdb", help="Database to load data into. Will be created if doesn't exist."),
    table: str = typer.Option("", help="Create the data with a specific table name. Will drop and recreate this table if it exists so use carefully! Uses convention 'tmp_[YYYYmmDD_HHMMSS_fff]' if not provided."),
    username: str = typer.Option("postgres", help="Postgres username"),
    password: str = typer.Option("", help="Postgres user password"),
    port: int = typer.Option(5432, help="Port"),
    column_width: int = typer.Option(256, help="Max characters per column.")

):
    client = DbClient(
        database=database,
        server=server,
        username=username,
        password=password,
        port=port
    )

    if table == "tmp_[YYYYmmDD_HHMMSS_fff]":
        table = None

    client.load_file(
        filepath=filepath,
        table=table,
        delimiter=delimiter,
        column_width=column_width
    )


def main():
    app()


if __name__ == '__main__':
    main()
