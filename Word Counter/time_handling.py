#Time handling

#This is something that Python already knows and has saved
from datetime import datetime

#This is the function that is used to later write in the document for when it was last opened
def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")