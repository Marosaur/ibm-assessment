#IBM Assessment Q1

import numpy as np

total_t_shirts = input()
total_sizes_input = input()
request_t_shirts = input()
request_sizes_input = input()

available_sizes = total_sizes_input.split(' ')
request_sizes = request_sizes_input.split(' ')

array_size = len(request_sizes)
size_fits = np.empty(array_size, dtype = int)
size_fits.fill(0)

if (request_t_shirts <= total_t_shirts):
  for x in range(len(available_sizes)):
    for y in range(len(request_sizes)):
      no_x = available_sizes[x].count('X')
      last_char_x = available_sizes[x][-1]
      no_y = request_sizes[y].count('X')
      last_char_y = request_sizes[yX][-1]
      if (last_char_y == last_char_x and no_y < no_x):
        size_fits[y] = 1
      elif (last_char_y == 'S'):
        if (last_char_x == 'M' or last_char_x == 'L'):
          size_fits[y] = 1
      elif (last_char_y == 'M'):
        if (last_char_x == 'M' or last_char_x == 'L'):
          size_fits[y] = 1
      else:
        pass
  if 0 in size_fits:
    print("No, no size")
  else:
    print("Yes")  
else:
  print("No, not enough t-shirts")