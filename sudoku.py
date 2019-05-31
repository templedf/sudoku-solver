import sys

class Container:
  def __init__(self):
    self.opts = set(range(1, 10))

  def add(self, n):
    self.opts.remove(n)

  def remove(self, n):
    self.opts.add(n)

class Cell:
  def __init__(self, c, r, q):
    self.r = r
    self.c = c
    self.q = q
    self.val = None

  def set(self, n):
    if self.val != None:
      self.c.remove(self.val)
      self.r.remove(self.val)
      self.q.remove(self.val)

    self.val = n

    if n != None:
      self.c.add(n)
      self.r.add(n)
      self.q.add(n)

  def opts(self):
    return self.c.opts.intersection(self.r.opts).intersection(self.q.opts)

def pprint():
  for i in range(9):
    for j in range(9):
      if cells[j][i].val != None:
        sys.stdout.write("%d " % cells[j][i].val)
      else:
        sys.stdout.write("X ")

    print

def solve(i, j):
  global count

  while j < 9:
    cell = cells[i][j]

    if cell.val != None:
      i = (i + 1) % 9

      if i == 0:
        j += 1
    else:
      opts = cell.opts()

      if len(opts) > 0:
        for n in opts:
          cell.set(n)
          ret = solve((i + 1) % 9, j + ((i + 1) / 9))

          if ret == 0:
            return 0

        cell.set(None)
        return 1
      else:
        count += 1
        return 1

  count += 1
  return 0

def init():
  for i in range(9):
    rows.append(Container())
    cols.append(Container())
    quads.append(Container())

  # First index is the column (x), and second is the row (y)
  for i in range(9):
    cells.append([])

    for j in range(9):
      cells[i].append(Cell(cols[i], rows[j], quads[i / 3 + 3 * (j / 3)]))

def load(file):
  f = open(file, "r")
  j = 0

  for line in f.readlines():
    data = line.split(' ')

    if len(cells) != 9:
      print "Bad line: %s" % line
      sys.exit(1)

    for i in range(9):
      if data[i].strip() in set([str(x) for x in range(1, 10)]):
        cells[i][j].set(int(data[i]))

    j += 1

  f.close()

count = 0
rows = []
cols = []
quads = []
cells = []

init()
load(sys.argv[1])
pprint()
print

if solve(0, 0) == 0:
  pprint()
else:
  print "NO SOLUTION"

print
print "%d solutions tried" % count

