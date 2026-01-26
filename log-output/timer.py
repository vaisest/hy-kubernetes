import uuid
from datetime import datetime
import pathlib
import time

unique = str(uuid.uuid1())
dest_file = pathlib.Path("./files/data.txt")

while True:
    dest_file.write_text(f"{datetime.now().isoformat()}: {unique}")
    time.sleep(5)
