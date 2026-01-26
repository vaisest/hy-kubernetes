import uuid
from datetime import datetime
import time

string = str(uuid.uuid1())
while True:
    print(f"{datetime.now().isoformat()}: {string}")
    time.sleep(5)