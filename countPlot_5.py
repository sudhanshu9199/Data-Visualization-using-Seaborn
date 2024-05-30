''' Count Plot Graph '''
# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# df = pd.read_csv('tips.csv')
# print(df)
# sns.countplot(x = 'sex', data = df)
# plt.show()



''' 'hue=' parameter used 'vertical graph' '''
# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# df = pd.read_csv('tips.csv')
# print(df)
# sns.countplot(x = 'sex', data = df, hue='smoker')
# plt.show()



''' horizontal graph '''
# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# df = pd.read_csv('tips.csv')
# print(df)
# sns.countplot(y = 'sex', data = df, hue='smoker')
# plt.show()



''' Violin plot in Seaborn '''
# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# df = pd.read_csv('tips.csv')
# print(df)
# sns.violinplot(x = 'day', y = 'total_bill', data = df, hue='time')
# plt.show()



''' 'linewidth=5'''
# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# df = pd.read_csv('tips.csv')
# print(df)
# sns.violinplot(x = 'day', y = 'total_bill', data = df, linewidth=5)
# plt.show()



''' 'palette=' parameter '''
# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# df = pd.read_csv('tips.csv')
# sns.violinplot(x = 'day', y = 'total_bill', data = df, linewidth=5, palette='gnuplot2')
# plt.show()



''' 'order=' parameter '''
# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# df = pd.read_csv('tips.csv')
# sns.violinplot(x= 'time', y = 'total_bill', data = df, order=['Dinner','Lunch'])
# plt.show()



''' 'split=' parameter '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

# df = pd.read_csv('tips.csv')
# sns.violinplot(x = 'day', y = 'total_bill', data = df, hue='sex',split=True)
# plt.show()



''' 'scale=' parameter '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('tips.csv')
# sns.violinplot(x = 'day', y = 'total_bill', data = df, hue = 'sex', split= True, scale='width')
# plt.show()



''' 'inner=' parameter '''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('tips.csv')
sns.violinplot(x = 'day', y = 'total_bill', data = df, hue='sex', inner='stick') ## {'box', 'quartile', 'point', 'stick', none}
plt.show()