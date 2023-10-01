from typing import Union

class DataSample:
    def __init__(self, data:Union[list, dict]):
        
        self._collections = []
        self._generate_data_sample(data)
    

    def _generate_data_sample(self, data:Union[list, dict]):
        
        if isinstance(data, dict):
            for key, value in data.items():

                if isinstance(value, (dict, list)):
                    setattr(self, key, DataSample(value))
                else:
                    setattr(self, key, value)
        
        elif isinstance(data, list): 
            for item in data:
                if isinstance(item, (list, dict)):
                    collection = DataSample(item)
                    self._collections.append(collection)
                else:
                    self._collections.append(item)
        else:
            self._collections = data

    def __getitem__(self, index):
        if isinstance(self._collections, list):            
            return self._collections[index]
