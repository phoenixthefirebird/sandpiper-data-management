from argparse import ArgumentParser
import sys
import os
from pathlib import Path
from dotenv import load_dotenv
from mysql.connector import connect, Error

def getDBConnection():
  """
  Returns a connection object to the local MySQL database.


  Return:
  A connection object to the local MySQL database or None if the connection failed.
  """
  env_file_path = Path("./.env")
  load_dotenv(env_file_path)
  try:
    connection = connect(
      host="localhost",
      user=os.getenv("MYSQL_USER"),
      password=os.getenv("MYSQL_PASSWORD"),
      database=os.getenv("DATABASE_NAME"),
    )
  except Error as e:
    print(e)
    return None
  return connection

if __name__ == '__main__':
  # read csv file containing basic profile information
  # command to run: python3 populateDB.py <csv_file>

  parser = ArgumentParser()
  # add optional argument for the csv filename
  parser.add_argument("-f", "--filename", dest="filename",
                      help="specifies the name of csv file containing the predictions", metavar="FILE")
  parser.add_argument("-c", "--clear", dest="clear",
                      help="clear the database before populating it", action="store_true")
                      
  args = parser.parse_args()

  if not args.filename and not args.clear:
    parser.print_help()
    sys.exit(1)

  if args.clear:
    connection = getDBConnection()
    if connection:
      clearDB(connection)
      print("Database cleared")
      connection.close()
    else:
      print("Error: could not connect to database")
      sys.exit(1)

  if args.filename:
    filename = args.filename
    pred_df = pd.read_csv(filename, index_col=0)
    start_time = time.time() # for timing the script
    for i in range(len(pred_df)):
      accession = pred_df.loc[i,"UniProt_ID"]
      gene_name = pred_df.loc[i,"Gene_name"]
      protein_sequence = pred_df.loc[i,"UniProt_sequence"]
      predictions = eval(pred_df.loc[i,"Prediction"])
      
      predictions = [float(x*100) for x in predictions] # convert to percentage
      populateDB(accession, gene_name, protein_sequence, predictions)
      print(f"Entry {i+1}/{len(pred_df)} ({accession}) successfully written to database!")

    print(f"Time elapsed: {time.time() - start_time} seconds")
  