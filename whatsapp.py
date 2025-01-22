import pywhatkit
import datetime

# Get the current time
now = datetime.datetime.now()
print(now)

# Add 1 minute to the current time
send_hour = now.hour
send_minute = now.minute + 1

# Adjust for overflow of minutes
if send_minute >= 60:
    send_hour += 1
    send_minute %= 60

try:
    # Schedule the message to send 1 minute from now
    pywhatkit.sendwhatmsg("+254797180740", "Yooh rada", send_hour, send_minute)
    print("Sent successfully!")
except Exception as e:
    print(f"Error: {e}")
