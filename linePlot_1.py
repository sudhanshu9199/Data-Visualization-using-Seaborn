''' Mathplotlib '''
# import seaborn as sns
# import matplotlib.pyplot as plt

# var = [1, 2, 3, 4, 5, 6, 7]
# var_1 = [2, 3, 4, 1, 5, 6, 7]

# plt.plot(var, var_1)
# plt.show()

''' Seaborn '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# var = [1, 2, 3, 4, 5, 6, 7]
# var_1 = [2, 3, 4, 1, 5, 6, 7]

# x_1 = pd.DataFrame({'var':var, 'var_1':var_1})
# sns.lineplot(x = 'var', y = 'var_1', data=x_1)
# plt.show()


''' Seaborn Graph work on Direct without 'DataFrame' '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# var = [1, 2, 3, 4, 5, 6, 7]
# var_1 = [2, 3, 4, 1, 5, 6, 7]
# sns.lineplot(x = var, y = var_1)
# plt.show()



'''import data from github of 'Car Accidient' '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('car_crashes.csv')
# print(df)
# sns.lineplot(x = 'speeding', y = 'alcohol', data = df)
# plt.show()



''' 'hue=' parameter encode a third variable for color in the plot.  '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('titanic.csv')
# # print(df)
# sns.lineplot(x = 'embark_town', y = 'age', hue = 'sex', data = df)
# plt.show()


''' 'size =' parameter allows you to control the size of plot elements (e.g., markers in scatter plots, lines in line plots) '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('titanic.csv')
# print(df)
# sns.lineplot(x = 'embark_town', y = 'age',  hue='sex',size= 50,data = df)
# plt.show()



''' 'style =' parameter allows you to control the visual style (e.g., marker shape, line style) of plot elements '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('titanic.csv')
# print(df)
# sns.lineplot(x = 'embark_town', y = 'age',  hue='sex',style='sex',data = df)
# plt.show()



''' 'palette =' parameter is a powerful tool in seaborn for customizing the color scheme used in your visualizations. '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('titanic.csv')
# print(df)
# sns.lineplot(x = 'embark_town', y = 'age',  hue='sex',style='sex', palette = 'Accent',data = df)
# plt.show()


''' 'markers=' parameter allows you to specify the marker symbol used to represent data points in the plot. '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('penguins.csv')
# print(df)
# sns.lineplot(x = 'bill_length_mm', y = 'bill_depth_mm', hue='sex', style='sex', palette = 'coolwarm', data = df,markers=["o",">"])
# plt.show()


''' head(__) '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('penguins.csv').head(20)
# print(df)
# sns.lineplot(x = 'bill_length_mm', y = 'bill_depth_mm', hue='sex', style = 'sex', palette = 'vlag', data = df,markers=['o','<'])
# plt.show()


''' 'Legend' parameter '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('penguins.csv').head(20)
# print(df)
# sns.lineplot(x = 'bill_length_mm', y = 'bill_depth_mm', hue='sex', style = 'sex', palette = 'vlag', data = df,markers=['o','<'], legend=False)
# plt.show()



