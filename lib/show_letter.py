# https://pythonhosted.org/sense-hat/api/#show_letter

import argparse

from _return import finish
from _img_array import to_int_list

parser = argparse.ArgumentParser(
  description='Displays a single text character on the LED matrix.'
)
parser.add_argument(
  's',
  type=str,
  help='The letter to show.'
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

  sense.show_letter(
    args.s,
    args.text_colour,
    args.back_colour
  )

  finish(
    {
      "result": True
    }
  )
except Exception, e:
  finish(
    e,
    1
  )
