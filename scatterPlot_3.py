# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('penguins.csv')
# print(df)
# sns.scatterplot(x = 'bill_length_mm', y = 'bill_depth_mm', data = df)
# plt.show()


''' 'hue=' parameter '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('penguins.csv')
# print(df)
# sns.scatterplot(x = 'bill_length_mm', y = 'bill_depth_mm', hue='sex', data = df)
# plt.show()


''' 'style=' , 'size=' , 'sizes=(__, __)' '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('penguins.csv').head(30)
# sns.scatterplot(x = 'bill_length_mm', y = 'bill_depth_mm', hue='sex', data = df, style= 'sex', size = 'sex', sizes = (100, 40))
# plt.show()


''' 'markers=' parameter '''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('penguins.csv').head(30)
# mark = {'Male': '*', 'Female':'o'}
sns.scatterplot(x = 'bill_length_mm', y = 'bill_depth_mm', hue='sex', data = df, style= 'sex', size = 'sex', sizes = (100, 40), markers= ['o','*'])
plt.show()