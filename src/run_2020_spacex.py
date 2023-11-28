import numpy as np
import get_telemetry_spacex
import sys

data = np.loadtxt("spacex_urls_2020.csv",delimiter=",",skiprows=1,dtype='str')
for i in range(9,10): #np.shape(data)[0]):
    custom_args = ["-c", data[i,1], "-d", "SpaceX_" + data[i,0].replace("/","_"), "-T", str(data[i,2]),"-s"]
    print(custom_args)
    sys.argv = [get_telemetry_spacex.__file__] + custom_args
    get_telemetry_spacex.main()
