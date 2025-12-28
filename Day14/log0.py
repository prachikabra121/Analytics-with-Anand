import logging

logging.basicConfig(filename="app.log",
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level=logging.INFO)

logging.info("user logged in")
