''' 'set_context', 'mlt.figure()' '''
# import matplotlib.pyplot as mlt
# import pandas as pd
# import seaborn as sns

# df = pd.read_csv('tips.csv')
# print(df)
# sns.set_style('darkgrid')
# mlt.figure(figsize=(12, 3)) # figsize = (width, height)
# sns.set_context('notebook', font_scale=5)
# sns.boxplot(y =df['total_bill'])
# sns.barplot(x = 'day', y = 'total_bill', data = df)
# sns.despine() # removeing axes spines
# # mlt.grid()
# mlt.show()




''' ########     Multiple Plots (Facet - Grid )       ########## '''

# import seaborn as sns
# import matplotlib.pyplot as mlt
# import pandas as pd

# df = pd.read_csv('tips.csv')
# fg = sns.FacetGrid(df, col='sex', hue = 'day')# double values 
# fg.map(mlt.scatter,'total_bill','tip').add_legend() 
# mlt.show()



''' Create Scatter graph as per Days '''
# import seaborn as sns
# import matplotlib.pyplot as mlt
# import pandas as pd

# df = pd.read_csv('tips.csv')
# fg = sns.FacetGrid(df, col='day', hue='sex')
# fg.map(mlt.scatter,'total_bill', 'tip').add_legend
# mlt.show()

''' Create Bar graph as per Days '''
import seaborn as sns
import matplotlib.pyplot as mlt
import pandas as pd

df = pd.read_csv('tips.csv')
fg = sns.FacetGrid(df, col='day', hue='sex')
fg.map(mlt.bar,'total_bill', 'tip').add_legend
mlt.show()