import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a = pd.DataFrame(index = range(1), columns= range(4))
print(a)

a.loc[0,3] = 1
print(a)

b = pd.DataFrame(index=range(1), columns= range(4))
a = pd.concat([a,b] , ignore_index=True)

print(a)


b = np.array([0,1,2,3,4])
plt.plot(b)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Plotting a NumPy Array')
plt.show()

