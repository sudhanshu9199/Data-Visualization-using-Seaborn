''' Box Plot Method '''
# import matplotlib.pyplot as mlt
# import seaborn as sns
# import pandas as pd

# df = pd.read_csv('tips.csv')
# sns.set(style='whitegrid')
# sns.boxplot(x = 'day', y = 'total_bill', data = df)
# mlt.show()



''' 'order=', 'sowmeans=', 'meanprops=' parameter '''
import matplotlib.pyplot as mlt
import seaborn as sns
import pandas as pd

df = pd.read_csv('tips.csv')
sns.set(style='whitegrid')
sns.boxplot(x = 'day', y = 'total_bill', data = df, hue= 'sex', color= 'green', order=['Fri', 'Thur', 'Sun'], showmeans = True, meanprops ={'marker':'+', 'markeredgecolor': 'blue'})
mlt.show()