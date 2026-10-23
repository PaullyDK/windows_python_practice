import logging

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p'
)
logging.info("A New Request Came")
try:
    x = int(input("Enter First Number:"))
    y = int(input("Enter Second Number:"))
    print("The Result", x/y)

except ZeroDivisionError as msg:
    print("cannot divide with zero")
    logging.exception(msg)

except ValueError as msg:
    print("Please provide int values only")
    logging.exception(msg)

logging.info("Request Processing Completed")
