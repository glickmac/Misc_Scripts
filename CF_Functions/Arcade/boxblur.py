def find_all_around(arr, row, col):
   top_left =  arr[row-1][col-1]
   top = arr[row-1][col]
   top_right = arr[row-1][col+1]
   right= arr[row][col+1]
   bot_right = arr[row+1][col+1]
   bot = arr[row+1][col]
   bot_left = arr[row+1][col-1]
   left = arr[row][col-1]
   res = [top_left, top, top_right, right, bot_right, bot, bot_left, left]
   return sum(res)


def boxBlur(arr):
   col = len(arr[0])
   row = len(arr)
   res = []
   for i in range(1,row-1):
      mew = []
      for j in range(1, col-1):
         mew.append((find_all_around(arr, i, j) + arr[i][j])//9)
      res.append(mew)
   return res
