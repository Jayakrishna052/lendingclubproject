from lib import configreader

#Defining customers Schema
def get_customers_schema():
    Schema = "customer_id int, customer_fname string, customer_lname string, customer_email string, customer_password string," \
    "customer_street_address string, customer_city string, customers_state string, customer_zip_code string"
    return Schema

# Creating customers dataframe

def read_customers(spark,env):
    conf = configreader.get_app_config(env)
    customers_file_path = conf["customers.file.path"]
    return spark.read.format("csv").option("header","true").schema(get_customers_schema()).load(customers_file_path)

# Defining Orders Schema

def get_orders_schema():
    schema = "order_id int, order_date string, customer_id int, order_status string"
    return schema

#Creating orders dataframe
def read_orders(spark,env):
    conf = configreader.get_app_config(env)
    orders_file_path = conf["orders.file.path"]
    return spark.read.format("csv").option("header","true").schema(get_orders_schema()).load(orders_file_path)
