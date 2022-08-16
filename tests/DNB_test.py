# 調整中
#%%
#%%
import numpy as np
import matplotlib.pyplot as plt
from src.dnb_ts.data import May_model
from src.dnb_ts.dnb_ts import time_DNB
#%%
times, x,y = May_model.get_data()
plt.plot(time_DNB(x,1000))

# %%
