''' Strip Plot Method '''
# import seaborn as sns
# import matplotlib.pyplot as mlt
# import pandas as pd
# import numpy as np

# df = pd.read_csv('tips.csv')
# sns.stripplot(x='day', y = 'total_bill', data = df)
# mlt.show()


''' 'hue-' and 'palette=' parameter '''
# import seaborn as sns
# import matplotlib.pyplot as mlt
# import pandas as pd
# import numpy as np

# df = pd.read_csv('tips.csv')
# sns.stripplot(x='day', y = 'total_bill', data = df, hue='sex', palette='YlGn')
# mlt.show()



''' 'linewidth=' Parameter :- to controls the thickness of lines in your plots, allowing you to visually emphasize or de-emphasize certain elements. '''
# import seaborn as sns
# import matplotlib.pyplot as mlt
# import pandas as pd
# import numpy as np

# df = pd.read_csv('tips.csv')
# sns.stripplot(x='day', y = 'total_bill', data = df, hue='sex', palette='YlGn', linewidth=1.2)
# mlt.show()



''' 'edgecolor=' parameter: to controls the color of the edges (borders or outlines) of various graphical elements in your plots. '''
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# df = pd.read_csv('tips.csv')
# sns.stripplot(x='day', y = 'total_bill', hue='sex', palette= 'YlGn', linewidth= 1.2,edgecolor='red', data = df, size = 10)
# plt.show()



''' 'jitter=' parameter: used to parameter controls the amount of random vertical jittering applied to the data points.'''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('tips.csv')
sns.stripplot(x='day', y = 'total_bill', hue='sex', palette= 'YlGn', linewidth= 1.2,edgecolor='red', data = df, size = 10, jitter=5)
plt.show()