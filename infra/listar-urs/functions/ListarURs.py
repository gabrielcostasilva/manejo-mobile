import mysql.connector
import os

manejo_db_host = os.environ.get('MANEJO_DB_HOST')
manejo_db_user = os.environ.get('MANEJO_DB_USER')
manejo_db_pwd = os.environ.get('MANEJO_DB_PWD')

mydb = mysql.connector.connect(
  host=manejo_db_host,
  user=manejo_db_user,
  password=manejo_db_pwd
)

def select_database(db_cursor, user_email):

    db_cursor.execute(
        f"SELECT `idr`.`supervisor`.`email` "
        f"FROM `idr`.`supervisor` "
        f"WHERE `idr`.`supervisor`.`email` = '{user_email}'")   

    return 'idr' if db_cursor.rowcount > 0 else 'senar'

def lambda_handler(event, context):   
    mycursor = mydb.cursor(dictionary=True, buffered=True)

    database = select_database(mycursor, event['user_email'])

    harvest_id = 4 if database == 'idr' else 3

    statement = (
    f"SELECT {database}.survey.id, {database}.field.`name` "
    f"FROM {database}.supervisor "
        f"LEFT JOIN {database}.field_supervisors "
            f"ON {database}.supervisor.id = {database}.field_supervisors.supervisors_id "
        f"LEFT JOIN {database}.field "
            f"ON {database}.field.id = {database}.field_supervisors.field_id "
        f"LEFT JOIN {database}.survey "
            f"ON {database}.survey.field_id = {database}.field_supervisors.field_id " 
    f"WHERE {database}.supervisor.email = '{event['user_email']}' "
        f"AND {database}.survey.harvest_id = {harvest_id}")

    mycursor.execute(statement)

    return mycursor.fetchall()