# https://pythonhosted.org/sense-hat/api/#low_light

import argparse

from _str2bool import str2bool
from _return import finish

parser = argparse.ArgumentParser(
  description='Toggles the LED matrix low light mode, useful if the Sense HAT is being used in a dark environment.'
)
parser.add_argument(
  'low_light',
  type=str2bool,
  nargs='?',
  default=True,
  help='"low_light" state'
)

args = parser.parse_args()

try:
  from sense_hat import SenseHat

  sense = SenseHat()

  sense.low_light = args.low_light

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
