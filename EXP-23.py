def permute(list, s):
   if list == 1:
      return s
   else:
      return [ 
         y + x
         for y in permute(1, s)
         for x in permute(list - 1, s)
      ]
print(permute(1, ["R","G","B"]))
print(permute(2, ["R","G","B"]))
