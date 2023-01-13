import os
import datetime as dt


# Set environment variables
# os.environ['API_USER'] = 'username'
# os.environ['API_PASSWORD'] = 'secret'

# Get environment variables
USER = os.getenv('S3_BUCKET_NAME')
PASSWORD = os.environ.get('API_PASSWORD')
t = dt.datetime.now()
iter = 1
while True:
    delta = dt.datetime.now()-t
    if delta.seconds >= 10:
        print(str(iter*10) + " sec ...")
        # Update 't' variable to new time
        t = dt.datetime.now()
        # Get environment variables
        BUCKET = os.getenv('S3_BUCKET_NAME')
        PASSWORD = os.environ.get('API_PASSWORD')
        PRODUCT_NAME = os.environ.get('PRODUCT_NAME')
        print("BUCKET = "+str(BUCKET))
        print("PASSWORD = "+str(PASSWORD))
        print("PRODUCT_NAME = " + str(PRODUCT_NAME))
        iter += 1
#    print("Log ...")