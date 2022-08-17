import numpy as np 
import time
import tqdm
import dnb_tools
from  numpy.lib.stride_tricks import sliding_window_view as sliding_window


def timer(func):
    def wrapper(*args, **kwargs):
        time_s = time.time()
        res = func(*args, **kwargs)
        print(f'calculation time ={time.time() - time_s}sec')
        return res
    return wrapper

@timer
def EWS_DNB(x,window_size,padding = 'online',normalization = 'straight'):
    print('caluculating time series DNB:')     
    # normalization
    if normalization == 'std':
        x = x /x.std(0)
    elif normalization == 'minmax':
        x = x /(x.max(0) - x.min(0))
    elif normalization != 'straight':
        raise NameError('select \'straight\', \'minmax\', or \'std\' ')
        return -1
    # 1 dim or n dim
    if len(x.shape) ==1:
        xs = sliding_window(x,window_size)
        cov_time_tmp = xs.std(1)
    else:
        x = x.reshape(x.shape[0],-1)
        xs = sliding_window(x,(window_size,1)).reshape(-1,x.shape[1],window_size)
        cov_time_tmp = np.zeros(xs.shape[0])
        for i in tqdm.tqdm(range(0,cov_time_tmp.shape[0])):
            sigmas,_ =np.linalg.eigh(np.cov(xs[i]))
            cov_time_tmp[i] =sigmas.max()

    if padding == 'same':
        # padding marage data using the edge 
        cov_time = np.zeros(x.shape[0])
        cov_time[window_size//2:-window_size//2+1] = cov_time_tmp
        cov_time[:window_size//2] = cov_time_tmp[0]
        cov_time[-window_size//2+1:] = cov_time_tmp[-1]
        return cov_time
    elif padding =='online':
        # cov_time[t] is calculated as time-sereis data t - window_size : t
        cov_time = np.zeros(x.shape[0])
        cov_time[:window_size-1] = cov_time_tmp[0]
        cov_time[window_size-1:] = cov_time_tmp
        return cov_time
    elif padding == 'valid':
        return cov_time_tmp
    else:
        raise NameError('select \'same\', \'online\', or \'valid\' ')
        return -1


def main():
    print("Hello DNB world")

if __name__ == "__main__":
    main()

