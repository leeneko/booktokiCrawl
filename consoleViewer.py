import os

def view(num):
  wantViewNo = num
  text = str(wantViewNo)

  folder_name = 'output'
  if not os.path.exists(folder_name):
    os.makedirs(folder_name)

  folder_name = 'output'
  file_name = f'화산귀환-{text}화.txt'
  file_path = os.path.join(folder_name, file_name)

  print(file_path)

  with open(file_path, mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
      print(line)

    f.close()