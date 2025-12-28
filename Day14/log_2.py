import logging

logging.basicConfig(filename="log_02.log",
                    level=logging.DEBUG,
                    format="%(asctime)s-%(levelname)s -%(message)s")


try:
    num1 = int(input(" enter a number 1"))
    logging.info(f"user has enter number 1 {num1}")
    num2 = int(input(" enter a number 2"))
    logging.info(f"user has enter number 2 {num2}")
    result=num1/num2
    logging.info(f"result from num1 and num2 is {result}")

except ZeroDivisionError as e:
    logging.error("An error occureds : Division by zeror.", exc_info=True)