import os
import time
from datetime import datetime
import shutil

def image_sorting(folder_with_photos):
    images = os.listdir(folder_with_photos)
    for image in images:
        time_of_creation = os.path.getmtime(f'{folder_with_photos}\\{image}')
        seconds_to_date = time.ctime(time_of_creation)
        date_time = datetime.strptime(seconds_to_date, "%a %b %d %H:%M:%S %Y")
        name_folder_from_date = f'{date_time.month}-{date_time.day}-{date_time.year}'
        if os.path.isdir(f'D:\\фото Iphone\\фото\\{name_folder_from_date}'):
            new_location = shutil.move(f'{folder_with_photos}\\{image}', f'{folder_with_photos}\\{name_folder_from_date}')

        else:
            os.mkdir(f'{folder_with_photos}\\{name_folder_from_date}')
            new_location = shutil.move(f'{folder_with_photos}\\{image}', f'{folder_with_photos}\\{name_folder_from_date}')

image_sorting('D:\\фото Iphone\\фото') # path to photo folder