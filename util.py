
class CustomException(Exception):
  pass


def blocksToStacks(blocks):
  stackNumber = blocks // 64
  remainder = blocks - (stackNumber * 64)
  
  obj = [stackNumber, remainder]
  return obj