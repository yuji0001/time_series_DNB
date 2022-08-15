import numpy as np 
import time
import tqdm
from  numpy.lib.stride_tricks import sliding_window_view as sliding_window


def timer(func):
    def wrapper(*args, **kwargs):
        time_s = time.time()
        func(*args, **kwargs)
        print(f'calculation time ={time.time() - time_s}sec')
    return wrapper

@timer
def time_DNB(x,window_size,padding = 'same'):
    print('caluculate time series DNB:') 
    if len(x.shape) ==1:
        xs = sliding_window(x,window_size)
        cov_time_tmp = xs.std(1)
    else:
        x = x.reshape(x.shape[0],-1)
        xs = sliding_window(x,(window_size,1)).reshape(-1,x.shape[1],window_size)
        cov_time_tmp = np.zeros(xs.shape[0])
        for i in tqdm.tqdm(range(0,cov_time_tmp.shape[0])):
            sigmas,_ =np.linalg.eig(np.cov(xs[i]))
            cov_time_tmp[i] =sigmas.max()

    if padding == 'same':
        cov_time = np.zeros(x.shape[0])
        cov_time[window_size//2:-window_size//2+1] = cov_time_tmp
        cov_time[:window_size//2] = cov_time_tmp[0]
        cov_time[-window_size//2+1:] = cov_time_tmp[-1]
        return cov_time
    elif padding =='online':
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

