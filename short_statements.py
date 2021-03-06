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

    
#find the longest sentencce
prideSentenceLengths = [len(sent) for sent in prideSents]
[sent for sent in prideSents if len(sent) == max(prideSentenceLengths)]

#re-order the dataframe with expected list of columns
expected_columns = ["a", "b"]
df = df[expected_columns]

#giving file name as running number with fix length (6 digit)
[f'{100000 + i + 1:06}.png' for i in range(19000)]

#generate list
list_19000 = [x for x in range(19000)]

#pickle
    with open(peta_pkl_file, 'rb') as handle:
        peta_data_info = pickle.load(handle)


    with open(pa100k_peta_pkl_file, 'wb') as handle:
        pickle.dump(peta_data_info, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
 #shuffle list
import random
random.shuffle(list_100k)

#converting values to numeric classes start from 0
age_map = {val:ii for ii,val in enumerate(set(users['Age']))}
users['Age'] = users['Age'].map(age_map)

#select columns from DF based on title
users = users.filter(regex='UserID|Gender|Age|JobID')


