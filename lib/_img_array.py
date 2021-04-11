import argparse


def to_int_list(v):
  return list(map(int, v.split(',')))


def img_array(v):
  if not isinstance(v, basestring):
    raise argparse.ArgumentTypeError('String value expected.')

  output = list(map(to_int_list, v.split(';')))

  if not (isinstance(output, list) and (len(output) == 8 * 8)):
    raise argparse.ArgumentTypeError('Expected list with 8 * 8 entries.')

  validStructure = all((isinstance(i, list) and (len(i) == 3) and all(isinstance(j, int) for j in i)) for i in output)

  if not validStructure:
    raise argparse.ArgumentTypeError('Expected 2d list with 3 colors of type int for each entry.')

  return output
