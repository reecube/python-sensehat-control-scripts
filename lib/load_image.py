# https://pythonhosted.org/sense-hat/api/#load_image

import argparse

from _str2bool import str2bool
from _return import finish

parser = argparse.ArgumentParser(description='Loads an image file, '
                                             'converts it to RGB format and displays it on the LED matrix. '
                                             'The image must be 8 x 8 pixels in size.')
parser.add_argument('file_path', type=str,
                    help='The file system path to the image file to load.')
parser.add_argument('redraw', type=str2bool, nargs='?', default=True,
                    help='Whether or not to redraw the loaded image file on the LED matrix. Defaults to True')

args = parser.parse_args()

try:
  from sense_hat import SenseHat

  sense = SenseHat()

  result = sense.load_image(args.file_path, args.redraw)

  # A list containing 64 smaller lists of [R, G, B] pixels (red, green, blue) representing the loaded image after RGB conversion.
  finish({"result": result})
except Exception, e:
  finish(e, 1)
