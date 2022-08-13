
#%%
from TS_DNB.data import May_model
from TS_DNB.data import saddle_node
import matplotlib.pyplot as plt
# %%

times,x,y =saddle_node.get_data()
plt.plot(times,x)
plt.plot(times,y)

# %%
times,x,y =May_model.get_data()
plt.plot(times,x)
plt.plot(times,y)

# %%
