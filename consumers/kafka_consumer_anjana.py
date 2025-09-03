"""
kafka_consumer_anjana.py

Consume JSON messages from a Kafka topic.
"""

#####################################
# Import Modules
#####################################

import os
import json
from dotenv import load_dotenv
from kafka import KafkaConsumer
from utils.utils_logger import logger
from utils.utils_consumer import get_kafka_broker_address

#####################################
# Load Environment Variables
#####################################

load_dotenv()

#####################################
# Getter Functions for .env Variables
#####################################

def get_kafka_topic() -> str:
    topic = os.getenv("KAFKA_TOPIC", "boys_questions")
    logger.info(f"Kafka topic: {topic}")
    return topic

#####################################
# Process message function
#####################################

def process_message(message: dict) -> None:
    question = message.get("question", "")
    logger.info(f"Received question: {question}")

    # Simple highlight rules
    if "dinosaur" in question.lower():
        logger.info("🦕 This is a dinosaur question!")
    elif "superhero" in question.lower():
        logger.info("🦸 This is a superhero question!")
    elif "food" in question.lower() or "snack" in question.lower():
        logger.info("🍕 This is a food/snack question!")
    elif "game" in question.lower():
        logger.info("⚽ This is a game question!")

#####################################
# Main function
#####################################

def main() -> None:
    logger.info("START boys questions consumer.")

    topic = get_kafka_topic()
    broker = get_kafka_broker_address()

    logger.info(f"Connecting to Kafka broker at {broker}...")
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=[broker],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="boys-questions-group"
    )
    logger.info("Kafka consumer successfully created.")

    try:
        for msg in consumer:
            try:
                message = json.loads(msg.value.decode("utf-8"))
                process_message(message)
            except json.JSONDecodeError as e:
                logger.error(f"Failed to decode message: {e}")
    except KeyboardInterrupt:
        logger.warning("Consumer interrupted by user.")
    finally:
        consumer.close()
        logger.info("END boys questions consumer.")

#####################################
# Conditional execution
#####################################

if __name__ == "__main__":
    main()
