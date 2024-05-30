''' Histogram Plot'''
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# df = pd.read_csv('penguins.csv')
# print(df)

# sns.displot(df['bill_length_mm'])
# plt.show()


''' 'bins=' Parameter '''
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# df = pd.read_csv('penguins.csv')
# # print(df)

# sns.displot(df['bill_length_mm'], bins = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
# plt.show()


''' ' Kde=' '''
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# df = pd.read_csv('penguins.csv')
# # print(df)

# sns.displot(df['bill_length_mm'], bins = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70], kde=True)
# plt.show()



''' 'rug=' These rug plots visually represent the individual data points underlying the distribution. '''

# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# df = pd.read_csv('penguins.csv')
# # print(df)

# sns.displot(df['bill_length_mm'], bins = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70], kde=True, rug= True)
# plt.show()


''' 'color=' parameter used across various seaborn plotting functions to control the color of visual elements in your plot. '''

# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# df = pd.read_csv('penguins.csv')
# # print(df)

# sns.displot(df['bill_length_mm'], bins = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70], kde=True, rug= True, color='blue')
# plt.show()



''' 'log=' parameter to control whether or not to use a logarithmic scale for one or both axes (x and y) in the plot.  '''
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# df = pd.read_csv('penguins.csv')
# # print(df)

# sns.displot(df['bill_length_mm'], kde=True, rug= True, color='blue', log_scale=True)
# plt.show()




''' BarPlot Method '''
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# df = pd.read_csv('penguins.csv')
# print(df)

# sns.barplot(x = df.island, y = df.bill_length_mm)
# plt.show()



''' barplot Graph using 'hue=' parameter '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('penguins.csv')
# sns.barplot(x = 'island', y = 'bill_length_mm',hue='sex', data = df)
# plt.show()



''' 'order=' parameter using in barplot '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('penguins.csv')
# order_1 = ['Dream', 'Torgersen', 'Biscoe']
# sns.barplot(x = 'island', y = 'bill_length_mm', hue = 'sex', data = df, order = order_1)

# plt.show()



''' 'order=' parameter using for 'hue=' parameter '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('penguins.csv')
# order_1 = ['Dream', 'Torgersen','Biscoe']
# sns.barplot(x = 'island', y = 'bill_length_mm', hue = 'sex', data = df, hue_order=["Female","Male"])
# plt.show()


''' 'ci=' parameter : percentiles must be in the range[0, 100] '''

# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv('penguins.csv')
# sns.barplot(x = 'island', y = 'bill_length_mm', hue = 'sex', data = df, ci=20)
# plt.show()


''' 'orient=' parameter  '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv('penguins.csv')
# sns.barplot(x = 'bill_length_mm', y = 'bill_depth_mm', hue = 'sex', data = df, orient='v')
# plt.show()


''' 'saturation=' parameter '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv('penguins.csv')
# sns.barplot(x = 'island', y = 'bill_length_mm', hue = 'sex', data = df, saturation=10)
# plt.show()


''' 'errcolor=' parameter to customize the color of error bars in bar charts.  '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv('penguins.csv')
# sns.barplot(x = 'island', y = 'bill_length_mm', hue = 'sex', data = df, saturation=10, errcolor='red')
# plt.show()


''' 'errwidth=' parameter to control the thickness of the error bars in bar charts. '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv('penguins.csv')
# sns.barplot(x = 'island', y = 'bill_length_mm', hue = 'sex', data = df, saturation=10, errcolor='red', errwidth=12)
# plt.show()



''' 'capsize=' parameter  to control the size of the caps on error bars in bar charts.  '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv('penguins.csv')
# sns.barplot(x = 'island', y = 'bill_length_mm', hue = 'sex', data = df, saturation=10, errcolor='red', capsize=0.5)
# plt.show()


''' 'alpha=' parameter typically controls the opacity or transparency of an element in a visualization or graphical representation. '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv('penguins.csv')
# sns.barplot(x = 'island', y = 'bill_length_mm', hue = 'sex', data = df, saturation=10, errcolor='red', capsize=0.5, alpha= 0.3)
# plt.show()



''' 'style='color'' :- like(darkgrid, whitegrid, dark, white, ticks, so on...) 'style=' parameter to control the overall visual style of your plots. '''

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('penguins.csv')
sns.set(style='ticks')
sns.barplot(x = 'island', y = 'bill_length_mm', hue = 'sex', data = df, saturation=10, errcolor='red')
plt.show()
