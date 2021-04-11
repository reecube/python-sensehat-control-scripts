# https://pythonhosted.org/sense-hat/api/#show_message

import argparse

from _return import finish
from _img_array import to_int_list

parser = argparse.ArgumentParser(
  description='Scrolls a text message from right to left across the LED matrix and at the specified speed, in the specified colour and background colour.'
)
parser.add_argument(
  'text_string',
  type=str,
  help='The message to scroll.'
)
parser.add_argument(
  '--scroll_speed',
  type=float,
  nargs='?',
  default=0.1,
  help='The speed at which the text should scroll. This value represents the time paused for between shifting the text to the left by one column of pixels. Defaults to 0.1'
)
parser.add_argument(
  '--text_colour',
  type=to_int_list,
  nargs='?',
  default=[255, 255, 255],
  help='A list containing the R-G-B (red, green, blue) colour of the text. Each R-G-B element must be an integer between 0 and 255. Defaults to [255, 255, 255] white.'
)
parser.add_argument(
  '--back_colour',
  type=to_int_list,
  nargs='?',
  default=[0, 0, 0],
  help='A list containing the R-G-B (red, green, blue) colour of the background. Each R-G-B element must be an integer between 0 and 255. Defaults to [0, 0, 0] black / off.'
)

args = parser.parse_args()

try:
  from sense_hat import SenseHat

  sense = SenseHat()

  result = sense.show_message(args.r, args.redraw)

  finish({"result": True})
except Exception, e:
  finish(e, 1)
