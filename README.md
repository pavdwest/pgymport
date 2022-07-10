# Overview

A tiny utility to dump a csv as text into a Postgres database.

Creates the table for you automatically. columns are varchar, it just gets the data into the db so you can do ETL with SQL.

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

## Import example file "data/friends.csv"

### Minimal

`python3 src/cli.py --filepath="data/friends.csv"`

### All Params

`python3 src/cli.py --filepath="data/friends.csv" delimiter="," --server="localhost" database="pgymportdb" table="friendstable" --username "postgres" --password="supersecurepassword" --port=5432 --column-width=1024`
