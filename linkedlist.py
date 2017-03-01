class Link:
  def __init__(self, value = None):
    self.value = value
    self._next = None

  def __str__(self):
    return 'Link ['+str(self.value)+']'

class LinkedListIterator:
  def __init__(self, head):
    self._ptr = head

  def next(self):
    if self._ptr is None:
      raise StopIteration
    else:
      n = self._ptr
      self._ptr = self._ptr._next
      return n

class LinkedList:
  def __init__(self):
    self._head = None
    self._last = None
    self._length = 0

  def __iter__(self):
    return LinkedListIterator(self._head)

  def append(self, x):
    if self._head == None:
      self._head = Link(x)
      self._last = self._head
    elif self._last == self._head:
      self._last = Link(x)
      self._head._next = self._last
    else:
      current = Link(x)
      self._last._next = current
      self._last = current
    self._length += 1

  def insert_after(self, x, link):
    nnext = link._next
    link._next = Link(x)
    link._next._next = nnext
    self._length += 1

  def remove_after(self, link):
    if link is None:
      if self._head is None:
        raise IndexError
      self._head = self._head._next
    else:
      if link._next is None:
        raise IndexError
      link._next = link._next._next
    self._length -= 1

  def __len__(self):
    return self._length

  def __str__(self):
    return 'LinkedList [ ' + ' '.join(str(node.value) for node in self) + ' ]'
