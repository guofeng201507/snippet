def remove_fc(state_dict):
    """ Remove the fc layer parameter from state_dict. """
  return {key: value for key, value in state_dict.items() if not key.startswith('fc.')}

#generate list of names
peta_dataset.image_name = [f'{100000 + i + 1:06}.png' for i in range(19000)]

#rename files

for count, filename in enumerate(os.listdir(peta_dataset.root)): 
    new_name = f'{100000 + i + 1:06}.png'

    src = os.path.join(peta_dataset.root, filename) 
    dst = os.path.join(peta_dataset.root, new_name) 

    os.rename(src, dst) 
    i = i + 1
   
#create dataframe from array
import pandas as pd
import numpy as np
    >>data.shape
    (480,193)
    >>type(data)
    numpy.ndarray
df=pd.DataFrame(data=data[0:,0:],
    ...        index=[i for i in range(data.shape[0])],
    ...        columns=['f'+str(i) for i in range(data.shape[1])])
    >>df.head()
