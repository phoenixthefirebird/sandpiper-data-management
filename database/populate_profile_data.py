from argparse import ArgumentParser
import sys
import os
from pathlib import Path
from dotenv import load_dotenv
from mysql.connector import connect, Error
import pandas as pd
from datetime import timezone
import datetime

def getDBConnection():
  """
  Returns a connection object to the local MySQL database.


  Return:
  A connection object to the local MySQL database or None if the connection failed.
  TODO verifies it actually gets the connection and how to set the variables 
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

def addProfile(中文姓名, 英文姓名, 性别, 加拿大潮属社团总会职务, 加拿大潮属社团总会职务_英文, 社团职务,
                 社团职务_英文, 工作职务, 工作职务_英文, 联系电话, 联系邮箱, 地址, 政要, 地区, 关系人姓名, 关系, 更新时间):
  """
  Appends 1 profile record to profiles table in the local MySQL database. 

  Parameters are all strings

  Return:
  void
  """
  env_file_path = Path("./.env")
  load_dotenv(env_file_path)
  try:
    with connect(
      host="localhost",
      user=os.getenv("MYSQL_USER"),
      password=os.getenv("MYSQL_PASSWORD"),
      database=os.getenv("DATABASE_NAME"),
    ) as connection:
        insert_profile_query = """
          INSERT INTO profiles
          (中文姓名, 英文姓名, 性别, 加拿大潮属社团总会职务, 加拿大潮属社团总会职务_英文, 社团职务,
            社团职务_英文, 工作职务, 工作职务_英文, 联系电话, 联系邮箱, 地址, 政要, 地区, 关系人姓名, 关系,
            更新时间)
          VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
          """

        profile_record = [
          (中文姓名, 英文姓名, 性别, 加拿大潮属社团总会职务, 加拿大潮属社团总会职务_英文, 社团职务,
          社团职务_英文, 工作职务, 工作职务_英文, 联系电话, 联系邮箱, 地址, 政要, 地区, 关系人姓名, 关系, 更新时间)
        ]

        with connection.cursor() as cursor:
          cursor.executemany(insert_profile_query, profile_record)
          connection.commit()

  except Error as e:
    print(e)

if __name__ == '__main__':
  # read csv file containing basic profile information
  # command to run: python3 populateDB.py <csv_file>

  parser = ArgumentParser()
  # add optional argument for the csv filename
  parser.add_argument("-f", "--filename", dest="filename",
                      help="specifies the name of csv file containing the predictions", metavar="FILE")
  args = parser.parse_args()

  if not args.filename:
    parser.print_help()
    sys.exit(1)

  if args.filename:
    filename = args.filename
    profile_data_df = pd.read_csv(filename, index_col=0)
    for i in range(len(profile_data_df)):
      中文姓名 = profile_data_df.loc[i,"中文姓名"]
      英文姓名 = profile_data_df.loc[i,"英文姓名"]
      性别 = profile_data_df.loc[i,"性别"]
      加拿大潮属社团总会职务 = profile_data_df.loc[i,"加拿大潮属社团总会职务"]
      加拿大潮属社团总会职务_英文 = profile_data_df.loc[i,"加拿大潮属社团总会职务_英文"]
      社团职务 = profile_data_df.loc[i,"社团职务"]
      社团职务_英文 = profile_data_df.loc[i,"社团职务_英文"]
      工作职务 = profile_data_df.loc[i,"工作职务"]
      工作职务_英文 = profile_data_df.loc[i,"工作职务_英文"]
      联系电话 = profile_data_df.loc[i,"联系电话"]
      联系邮箱 = profile_data_df.loc[i,"联系邮箱"]
      地址 = profile_data_df.loc[i,"地址"]
      政要 = profile_data_df.loc[i,"政要"]
      地区 = profile_data_df.loc[i,"地区"]
      关系人姓名 = profile_data_df.loc[i,"关系人姓名"]
      关系 = profile_data_df.loc[i,"关系"]
      更新时间 = datetime.datetime.now(timezone.utc)
      # TODO remove this print after debug
      print(更新时间)
      
      addProfile(中文姓名, 英文姓名, 性别, 加拿大潮属社团总会职务, 加拿大潮属社团总会职务_英文, 社团职务,
                 社团职务_英文, 工作职务, 工作职务_英文, 联系电话, 联系邮箱, 地址, 政要, 地区, 关系人姓名, 关系, 更新时间)

      # TODO remove print after debug
      print(f"Entry {i+1}/{len(profile_data_df)} successfully written to database!")

  