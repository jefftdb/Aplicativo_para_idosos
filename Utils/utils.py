from datetime import datetime

class Utils():
    def set_name(self):
        return datetime.now().strftime("APP_IDOSOS_%d_%m_%Y_%H_%M_%S_%mm") + ".mp4"