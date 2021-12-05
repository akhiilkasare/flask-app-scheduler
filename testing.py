from flask import Flask
from flask_apscheduler import APScheduler
import logging 

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')



logger=logging.getLogger()
  
app = Flask(__name__)
scheduler = APScheduler()

@app.route("/")
def index():
    return "flask api started"

def scheduledTask():
    print("This task will run after 5 seconds")
    logger.warning("This task will run after 5 seconds")

if __name__ == "__main__":
    scheduler.add_job(id='Scheduled task', func=scheduledTask, trigger='interval', seconds=2)
    scheduler.start()
    app.run(host='127.0.0.1',port=8001)