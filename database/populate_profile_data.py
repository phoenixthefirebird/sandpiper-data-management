from argparse import ArgumentParser
import sys
import os
from pathlib import Path
from dotenv import load_dotenv
from mysql.connector import connect, Error
import pandas as pd
from datetime import timezone
import datetime

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
  print(f"adding {中文姓名}'s profile")
  try:
    with connect(
      host="localhost",
      # TODO Remove the hardcodihng
      # user=os.getenv("MYSQL_USER"),
      # password=os.getenv("MYSQL_PASSWORD"),
      # database=os.getenv("DATABASE_NAME"),
      user="root",
      password="u909faulr",
      database="sandpipers",
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
          print(f"Success adding {中文姓名}'s profile")
          cursor.close()
    connection.close()
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
      中文姓名 = profile_data_df.iloc[i]["英文姓名"] if pd.isna(profile_data_df.iloc[i]["中文姓名"]) else profile_data_df.iloc[i]["中文姓名"]
      英文姓名 = None if pd.isna(profile_data_df.iloc[i]["英文姓名"]) else profile_data_df.iloc[i]["英文姓名"]
      性别 = None if pd.isna(profile_data_df.iloc[i]["性别"]) else profile_data_df.iloc[i]["性别"]
      加拿大潮属社团总会职务 = None if pd.isna(profile_data_df.iloc[i]["加拿大潮属社团总会职务"]) else profile_data_df.iloc[i]["加拿大潮属社团总会职务"]
      加拿大潮属社团总会职务_英文 = None if pd.isna(profile_data_df.iloc[i]["加拿大潮属社团总会职务_英文"]) else profile_data_df.iloc[i]["加拿大潮属社团总会职务_英文"]
      社团职务 = None if pd.isna(profile_data_df.iloc[i]["社团职务"]) else profile_data_df.iloc[i]["社团职务"]
      社团职务_英文 = None if pd.isna(profile_data_df.iloc[i]["社团职务_英文"]) else profile_data_df.iloc[i]["社团职务_英文"]
      工作职务 = None if pd.isna(profile_data_df.iloc[i]["工作职务"]) else profile_data_df.iloc[i]["工作职务"]
      工作职务_英文 = None if pd.isna(profile_data_df.iloc[i]["工作职务_英文"]) else profile_data_df.iloc[i]["工作职务_英文"]
      联系电话 = None if pd.isna(profile_data_df.iloc[i]["联系电话"]) else profile_data_df.iloc[i]["联系电话"]
      联系邮箱 = None if pd.isna(profile_data_df.iloc[i]["联系邮箱"]) else profile_data_df.iloc[i]["联系邮箱"]
      地址 = None if pd.isna(profile_data_df.iloc[i]["地址"]) else profile_data_df.iloc[i]["地址"]
      政要 = None if pd.isna(profile_data_df.iloc[i]["政要"]) else profile_data_df.iloc[i]["政要"]
      地区 = None if pd.isna(profile_data_df.iloc[i]["地区"]) else profile_data_df.iloc[i]["地区"]
      关系人姓名 = None if pd.isna(profile_data_df.iloc[i]["关系人姓名"]) else profile_data_df.iloc[i]["关系人姓名"]
      关系 = None if pd.isna(profile_data_df.iloc[i]["关系"]) else profile_data_df.iloc[i]["关系"]
      更新时间 = datetime.datetime.now(timezone.utc)
      
      addProfile(中文姓名, 英文姓名, 性别, 加拿大潮属社团总会职务, 加拿大潮属社团总会职务_英文, 社团职务,
                 社团职务_英文, 工作职务, 工作职务_英文, 联系电话, 联系邮箱, 地址, 政要, 地区, 关系人姓名, 关系, 更新时间)


  