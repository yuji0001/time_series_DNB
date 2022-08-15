#%%
import numpy as np
import matplotlib.pyplot as plt
from TS_DNB.data import May_model
from TS_DNB.TS_DNB import time_DNB
#%%
times, x,y = May_model.get_data()
plt.plot(time_DNB(x,1000))
