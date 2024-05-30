''' Pair Plot Graph '''
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# df = pd.read_csv('tips.csv')
# sns.pairplot(df)
# plt.show()



''' hue=' parameter used '''
# import pandas as pd
# import matplotlib.pyplot as mlt
# import seaborn as sns
# import numpy as np
# df = pd.read_csv('tips.csv')
# sns.pairplot(df, hue='sex')
# mlt.show()



''' 'hue_order=' and y or x_vars=[___, ___] '''
# import matplotlib.pyplot as mlt
# import pandas as pd
# import seaborn as sns
# import numpy as np
# df = pd.read_csv('tips.csv')
# sns.pairplot(df, hue='sex', hue_order=['Female','Male'], y_vars=['total_bill','tip'], palette= 'twilight')
# mlt.show()



''' 'kind=' parameter '''
import matplotlib.pyplot as mlt
import pandas as pd
import seaborn as sns
import numpy as np
df = pd.read_csv('tips.csv')
sns.pairplot(df, hue='sex', hue_order=['Female','Male'], kind='hist', palette= 'twilight') ## kind= {'scatter', 'kde', 'hist', 'reg'}
mlt.show()