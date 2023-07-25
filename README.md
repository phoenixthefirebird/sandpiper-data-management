# sandpiper-data-management

## Loading profile data into MySQL from csv
### Prerequisite
- Python 3
- MySQL

### Step 1: 
Create a new MySQL database
### Step 2:
Create a `.env` file in the `database directory` and add the following:

```
DATABASE_NAME=<DATABASE_NAME>

MYSQL_USER=<YOUR_MYSQL_USERNAME>

MYSQL_PASSWORD=<YOUR_MYSQL_PASSWORD>
```

replace variables in <> with actual names and passwords

### Step 3:
Set up Python virtual environment under the `database` directory and run

`pip install -r requirements.txt` 

to install required Python packages

### Step 4: 
While in `database` directory, run the following command to execute the loading script:

`python .\populate_profile_data.py  <relative file path to the csv file>`

or if you need to start loading at a certain index due to i.e. duplication or error: 

`python .\populate_profile_data.py  <relative file path to the csv file> --start-index <row index to start loading>`


## Requirements for running frontend app
1. node >= 16.8.0
