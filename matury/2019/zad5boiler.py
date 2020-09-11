import csv

__all__ = ["data"]

class excel:
            delimiter = ';'
            quotechar = '"'
            escapechar = None
            doublequote = True
            skipinitialspace = False
            lineterminator = '\r\n'
            quoting = csv.QUOTE_MINIMAL


class Data:
  def __init__(self, row):
    self.day = int(row[0])
    self.temp = float(row[1].replace(",", "."))
    self.rain = int(row[2])
    self.cat = row[3]
    self.size = int(row[4])

data = []

with open("dane/pogoda.txt") as f:
  reader = csv.reader(f, dialect=excel)
  skip_first = False
  for row in reader:
    if skip_first is False:
      skip_first = True
      continue
    data.append(Data(row))