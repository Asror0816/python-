def hello_name(name):
  return "Hello " + name + "!"



def make_out_word(out, word):
  return out[:2] + word + out[2:]


def first_half(str):
  l = len(str) / 2
  return str[:l]

def non_start(a, b):
  return a[1:] + b[1:]