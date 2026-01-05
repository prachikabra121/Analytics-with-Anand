import logging

# Configure logging
logging.basicConfig(
    filename='operation.log',  # Added the missing comma here
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO
)

def add_numbers(a, b):
    logging.info("Starting the addition operation")
    try:
        result = a + b
        logging.info(f"Adding {a} and {b}")
        logging.info(f"Result of addition: {result}")
        return result
    except Exception as e:
        logging.error("An error occurred during addition: %s", e)
        return None

# Example usage
num1 = 5
num2 = 'a'  # This will raise an exception
logging.info(f"Numbers to be added: {num1} and {num2}")
sum_result = add_numbers(num1, num2)
logging.info(f"Final result: {sum_result}")
