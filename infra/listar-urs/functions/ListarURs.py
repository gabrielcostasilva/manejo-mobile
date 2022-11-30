import mysql.connector
import os

manejo_db_host = os.environ.get('MANEJO_DB_HOST')
manejo_db_user = os.environ.get('MANEJO_DB_USER')
manejo_db_pwd = os.environ.get('MANEJO_DB_PWD')
manejo_db_database = os.environ.get('MANEJO_DB_DATABASE')
test_email = os.environ.get('TEST_EMAIL')
test_survey = os.environ.get('TEST_SURVEY')

mydb = mysql.connector.connect(
  host=manejo_db_host,
  user=manejo_db_user,
  password=manejo_db_pwd,
  database=manejo_db_database
)

def lambda_handler(event, context):   
    mycursor = mydb.cursor(dictionary=True)

    statement = (
    """SELECT survey.id, field.`name` FROM supervisor 
        LEFT JOIN field_supervisors
            ON supervisor.id = field_supervisors.supervisors_id
        LEFT JOIN field
            ON field.id = field_supervisors.field_id
        LEFT JOIN survey
            ON survey.field_id = field_supervisors.field_id """ 
    f"WHERE supervisor.email = '{test_email}' "
        f"AND survey.harvest_id = {test_survey}")

    mycursor.execute(statement)

    result = mycursor.fetchall()

    return result
