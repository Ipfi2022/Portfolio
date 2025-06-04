import traceback
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def division1(m,n):
    if (n == 0):
        raise ValueError("There is something wrong with your data")
    else:
        logging.info("Operation performed successfully.")
        return(m/n)

def division2(m,n):
    try:
        return(m/n)
    except Exception as e:
        with open('error.log', 'a') as f:
            f.write(traceback.format_exc())

def division3(m,n):
    try:
        return(m/n)
    except ValueError as ve:
        logging.exception("Exception occurred: %s", str(ve))


def division4(m,n):
    assert (n!=0), "There is something wrong with your data"
    return(m/n)

def division5(m,n):
    try:
        return(m/n)
    except Exception:
        print("There is something wrong with your data")

print(division5(5,0))
