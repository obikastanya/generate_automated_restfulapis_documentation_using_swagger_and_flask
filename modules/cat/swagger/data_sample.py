from utils.swagger.data_sample_builder import DataSample


class Cat(DataSample):
    def __init__(self):
        data_sample = {
            "id": "1",
            "name": "Mario",
            "colors": [{"color": "Black"}, {"color": "Grey"}, {"color": "Orange"}],
        }
        super().__init__(data_sample)
