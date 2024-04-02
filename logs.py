import logging
import time

# Configure logging
logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_logs():
    print('Success Logs')
    logging.info("This is a log message.")

def main():
    while True:
        generate_logs()
        time.sleep(5)  # Sleep for 1 hour (3600 seconds)

if __name__ == "__main__":
    main()
