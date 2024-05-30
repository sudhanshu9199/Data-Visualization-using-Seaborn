'''  heatMap method '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# # df = pd.read_csv('penguins.csv')
# ##   numpy.linespace(start, end, quantity)
# df = np.linspace(1, 10, 20).reshape(4, 5)
# print(df)
# sns.heatmap(df)
# plt.show()


''' Dataset from github 'seaborn dataseat' '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# df = pd.read_csv('anagrams.csv')
# print(df)



''' To delete the 'attnr' column from the data and graph the 'heatmap' '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# df = pd.read_csv('anagrams.csv')
# x = df.drop(columns=['attnr'], axis=1)
# print(x)
# sns.heatmap(x)
# plt.show()



''' now using 'head(__)' '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# df = pd.read_csv('anagrams.csv').head(10)
# x = df.drop(columns=['attnr'], axis=1)
# print(x)
# sns.heatmap(x)
# plt.show()



''' min value to max value '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# df = pd.read_csv('anagrams.csv').head(10)
# x = df.drop(columns=['attnr'], axis=1)
# sns.heatmap(x, vmin=0, vmax=12)
# plt.show()


''' 'cmap=' parameter : short for "colormap", is widely used in various Python libraries for data visualization,'''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# df = pd.read_csv('anagrams.csv').head(10)
# x = df.drop(columns=['attnr'], axis=1)
# sns.heatmap(x, vmin=0, vmax=12, cmap= 'pink_r')
# plt.show()



''' 'annot=' and  'fmt=' parameter '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# df = pd.read_csv('anagrams.csv')
# x = df.drop(columns=['attnr'], axis=1)
# sns.heatmap(x, vmin=0, vmax=14, cmap='icefire', annot=True) # 'fmt=.2f' for:- Display values with two decimal places
# plt.show()



''' using array for replacing the actual value to given value for showing on using 'annot=' parameter '''
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# df = np.linspace(1, 10, 10).reshape(2, 5)
# print(df)
# ar = np.array([['Text0', 'Text1', 'Text2', 'Text3', 'Text4'],
#                 ['dext5', 'dext6', 'dext7', 'dext8', 'dext9']])
# print(ar)
# sns.heatmap(df, vmin = 0, vmax=10, cmap='PuOr', annot=ar, fmt='s')
# plt.show()



''' Now changes font color and sizes which display '''
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# df = np.linspace(1, 10, 10).reshape(2, 5)
# print(df)
# y = {'fontsize':20, 'color':'red'}
# sns.heatmap(df, vmin = 0, vmax=10, cmap='PuOr', annot=True, annot_kws= y )
# plt.show()



''' 'linewidth=' parameter: used for gap between the boxes '''
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# df = np.linspace(1, 10, 10).reshape(2, 5)
# print(df)
# y = {'fontsize':20, 'color':'red'}
# sns.heatmap(df, vmin = 0, vmax=10, cmap='PuOr', annot=True, annot_kws= y, linewidths=10)
# plt.show()



''' 'linecolor=' parameter: give color in the gaps '''
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# df = np.linspace(1, 10, 10).reshape(2, 5)
# print(df)
# y = {'fontsize':20, 'color':'red'}
# sns.heatmap(df, vmin = 0, vmax=10, cmap='PuOr', annot=True, annot_kws= y, linewidths=10, linecolor='blue')
# plt.show()


''' 'cbar=' parameter: to control the display and customization of colorbars(True or False) in heatmaps and other visualizations that use colormaps  '''
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# df = np.linspace(1, 10, 10).reshape(2, 5)
# print(df)
# y = {'fontsize':20, 'color':'red'}
# sns.heatmap(df, vmin = 0, vmax=10, cmap='PuOr', annot=True, annot_kws= y, linewidths=10, linecolor='blue', cbar = False)
# plt.show()



''' 'xticklabels=' parameter '''
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# df = np.linspace(1, 10, 10).reshape(2, 5)
# print(df)
# y = {'fontsize':20, 'color':'red'}
# sns.heatmap(df, vmin = 0, vmax=10, cmap='PuOr', annot=True, annot_kws= y, linewidths=10, linecolor='blue', cbar = False, xticklabels=False)
# plt.show()


''' Set axis labels using the Axes object '''
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# df = np.linspace(1, 10, 10).reshape(2, 5)
# print(df)
# y = {'fontsize':20, 'color':'red'}
# sns.heatmap(df, vmin = 0, vmax=10, cmap='PuOr', annot=True, annot_kws= y, linewidths=10, linecolor='blue', cbar = False, xticklabels=True)
# v = sns.scatterplot(df)
# v.set(xlabel = 'Python', ylabel = 'Love')
# plt.show()



''' Now we customise the font size of x and y axis labels '''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = np.linspace(1, 10, 10).reshape(2, 5)
print(df)
y = {'fontsize':20, 'color':'red'}
sns.heatmap(df, vmin = 0, vmax=10, cmap='PuOr', annot=True, annot_kws= y, linewidths=10, linecolor='blue', cbar = False, xticklabels=True)
v = sns.scatterplot(df)
v.set(xlabel = 'Python', ylabel = 'Love')
# Increase font size for x and y-axis labels in the scatter plot
v = sns.scatterplot(df)
v.set_xlabel('Python', fontsize=18)  # Increased font size for x-axis label
v.set_ylabel('Love', fontsize=18)   # Increased font size for y-axis label
plt.show()