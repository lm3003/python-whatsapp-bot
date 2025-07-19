import logging
import os

from app import create_app
from start.whatsapp_quickstart import send_message, get_text_message_input



app = create_app()

message = """
Hi, I'm your health buddy. 
\nAsk me anything about health, food or exercise, I'll guide you to the best of my ability (like a true buddy).
\nI can also generate calorie count for you, track your daily calorie intake, generate a tasty but healthy weekly meal plan and send you daily reminders regarding your calorie count update.
\nTry me
"""

RECIPIENT_WAID=os.getenv("RECIPIENT_WAID")
# logging.info(RECIPIENT_WAID)
response = send_message(get_text_message_input(
    recipient=RECIPIENT_WAID, text=message
))
logging.info(response)
if __name__ == "__main__":
    logging.info("Flask app started")
    app.run(host="0.0.0.0", port=8000)
