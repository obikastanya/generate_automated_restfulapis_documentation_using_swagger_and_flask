from utils.swagger.data_sample_builder import DataSample


class User(DataSample):
    def __init__(self):
        data_sample = {"username": "obi kastanya", "password": "123456"}
        super().__init__(data_sample)


class Token(DataSample):
    def __init__(self):
        data_sample = {
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
        }
        super().__init__(data_sample)
