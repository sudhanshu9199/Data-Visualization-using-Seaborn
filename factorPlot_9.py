# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt

# # Sample data (replace with your actual data)
# tips = pd.read_csv("tips.csv")

# # Create a catplot (using kind='bar' for consistency)
# sns.factorplot(x="day", y="total_bill", hue="sex", data=tips, kind="bar")
# plt.show()

''' 'factor plot method is replcaed by 'cat plot Method' '''
# import seaborn as sns
# import matplotlib.pyplot as mlt
# import pandas as pd

# df = pd.read_csv('tips.csv').head(25)
# sns.catplot(x = 'tip', y = 'size', data = df, palette= 'PuBuGn_r')
# mlt.show()



''' 'height=' parameter '''
# import seaborn as sns
# import matplotlib.pyplot as mlt
# import pandas as pd

# df = pd.read_csv('tips.csv').head(25)
# sns.catplot(x = 'tip', y = 'size', data = df, palette= 'PuBuGn_r', hue='sex', height=2)
# mlt.show()



''' 'kind=' parameter: used in Cat plot for using structure the data into different graphs '''
import seaborn as sns
import matplotlib.pyplot as mlt
import pandas as pd

df = pd.read_csv('tips.csv').head(25)
sns.catplot(x = 'tip', y = 'size', data = df, palette= 'PuBuGn_r', hue='sex', kind='point')
mlt.show()