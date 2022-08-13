import numpy as np 
from  numpy.lib.stride_tricks import sliding_window_view as sliding_window

def time_std(x,window_size=10,padding = 'same'):
    xs = sliding_window(x,window_size)
    cov_time = np.zeros(x.shape)
    cov_time_tmp = xs.std(1)
    cov_time[window_size//2:-window_size//2+1] = cov_time_tmp
    cov_time[:window_size//2] = cov_time_tmp[0]
    cov_time[-window_size//2+1:] = cov_time_tmp[-1]
    return cov_time

def MAM(x,windo_size=10,padding = 'same'):
    # moving_average_method
    xs = sliding_window(x,windo_size)
    x_LP = np.zeros(x.shape[0])
    x_LP_tmp = xs.mean(1)
    x_LP[windo_size//2:-windo_size//2+1] = x_LP_tmp
    x_LP[:windo_size//2] = x_LP_tmp[0]
    x_LP[-windo_size//2:] = x_LP_tmp[-1]
    return  x_LP


if __name__ == "__main__":
    print("Hello DNB world")
