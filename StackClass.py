
class ArrayStack:
  def __init__(self):
    self.__stack = []
    self.__size = 0
  def push(self, element):
    """adds a new element to the stack"""
    self.__stack.append(element)
    self.__size += 1
  def pop(self):
    """Removes the last item added from the stack"""
    if self.__is_empty():
      lastVar = self.__stack[-1]
      del self.__stack[-1]
      self.__size -= 1
      return lastVar
    else:
      raise IndexError("list index out of range")
  def top(self):
    """Returns the last item added to the stack"""
    if self.__is_empty():
      return self.__stack[-1]
    else:
      raise IndexError("list index out of range")
  def __is_empty(self):
    """Determines if the stack is empty"""
    return self.__size > 0
  def __len__(self):
    """Returns the length of the stack"""
    return self.__size
  def __str__(self):
    """Display contents of stack"""
    out = ""
    for ele in self.__stack:
        out += str(ele) + ' '

    out += "<TOP"
    return out