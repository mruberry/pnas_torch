from PIL import Image
import os

# Converts all jpg and jpeg images under the given path into pngs
# WARNING: deletes the original images
def convert_to_png(path):
    tree = os.walk(path)
    for (dirpath, dirnames, filenames) in tree:
        for filename in filenames:
            if filename.endswith('.jpg') or filename.endswith('.jpeg'):
                file_path = dirpath + "/" + filename
                img = Image.open(file_path)
                new_path = file_path.split('.')
                new_path[-1] = '.png'
                new_path = ''.join(new_path)
                img.save(new_path)
                os.remove(file_path)
