# Overview

A tiny utility to dump a csv file as text into a Postgres database.

Creates the table for you automatically. All columns are varchar, it just gets the data into the db so you can do ETL with SQL.

Should be very fast as it uses Postgres' COPY command. Python just orchestrates the process.

# Installation

Clone repo:
`git clone git@github.com:pavdwest/pgymport.git`

Create a new virtual environment & install dependencies:

`cd pgymport`

`python3 -m venv .venv`

`source .venv/bin/activate`

`pip3 install -r requirements.txt`

# Use

## Help

`python3 src/cli.py --help`

```
Usage: cli.py [OPTIONS]

Options:
  --filepath TEXT                 Relative/full filepath including extension.
                                  [required]
  --delimiter TEXT                Delimiter/Column Separator in file.
                                  [default: ,]
  --server TEXT                   Server/Host on which the database resides.
                                  [default: localhost]
  --database TEXT                 Database to load data into. Will be created
                                  if doesn't exist.  [default: pgymportdb]
  --table TEXT                    Create the data with a specific table name.
                                  Will drop and recreate this table if it
                                  exists so use carefully! Uses convention
                                  'tmp_[YYYYmmDD_HHMMSS_fff]' if not provided.
  --username TEXT                 Postgres username  [default: postgres]
  --password TEXT                 Postgres user password
  --port INTEGER                  Port  [default: 5432]
  --column-width INTEGER          Max characters per column.  [default: 256]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```

## Import example file "data/friends.csv"

### Minimal

`python3 src/cli.py --filepath="data/friends.csv"`

### All Params

`python3 src/cli.py --filepath="data/friends.csv" delimiter="," --server="localhost" database="pgymportdb" table="friendstable" --username "postgres" --password="supersecurepassword" --port=5432 --column-width=1024`
