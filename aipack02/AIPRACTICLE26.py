#Practical-26 Part-1

d1 =  [   [1, 2 ],
          [3, 4 ],
          [5, 6 ],
          [7, 8 ],
          [9, 10],
          [11,12],
          [13,14]
       ]

print("d1 = "  )
print(d1)

#Practical-26 Part-2

import numpy as np
d2 = np.array( [ [1,2],
                 [3,4],
                 [5,6],
                 [7,8],
                 [9,10],
                 [11,12],
                 [13,14]  ]   )

print( "\nd2 ="  )
print(d2)

print( "\n d2.shape = ", d2.shape  )  #(7,2)
print( "\n d2.size  = ", d2.size  )   #14
print( "\n d2.ndim  = ", d2.ndim  )   #2
