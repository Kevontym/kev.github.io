# debug~when your testing playing around trouble shooting, when know certain place in code
# info ~informational methods, email notifications, 17 users online 
# Warning ~ nothing bad happens yet but something might happen if you dont do nothing, Maybe storage is running low
# Error ~ couldnt do calculation or an exception was picked up 
# critical ~crucial component breaks down, system is dead, server downs,
import logging

logging.basicConfig(level=logging.DEBUG)

# logging.info("You have got 20 mails in your inbox")
# logging.critical("All components failed!")

logger = logging.getLogger("NeuralNine Logger")
# logger.info("The best logger was just created")
# logger.critical("Your youtube channel was deleted")
# logger.log(logging.ERROR, "An error occured")

logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("mylog.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("This is a debug messsage!")
logger.info("This is important information!")

