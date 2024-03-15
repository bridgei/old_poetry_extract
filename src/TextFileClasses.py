from os import makedirs
from os import path as os_path
from pathlib import Path

class ArrayToFile:

  def __init__(self, list, name, path, create=True):
    # if list.count + len(name) > 0:
    if name:
      self.name = name
    else:
      print('No file name given')

    if path:
      if Path(path).exists():
        self.path = path
      else:
        if create:
          self.path = path
          makedirs(self.path)
    else:
      self.path = './'

    if list:
      self.list = []
      self.list = list
    else:
      print("empty list")
      return

    self.filepath = os_path.join(self.path, self.name)


    if(isinstance(list, dict)):
      self.__create_file_from_dict(self.filepath, self.list)
    else:
      self.__create_file_from_list(self.filepath, self.list)


  def __create_file_from_list(self, filepath, list):
    with open(filepath,'w') as of:
      for item in list:
        of.write(f'{item}\n')
        # print((f'{item}\n'))
      self.count = len(list)
      print(self.count)
      of.close()
      return self.count

  def __create_file_from_dict(self, filepath, list):
    with open(filepath,'w') as of:
      for key,value in list.items():
        for item in value:
          of.write(f'{item}\n')
          # print((f'{item}\n'))
        self.count = len(list)
        print(self.count)
      of.close()
      return self.count






# Test code
# list = [1,2,3,4]
# file = ArrayToFile(list,'file.txt', 'data')
# print(file.name)
