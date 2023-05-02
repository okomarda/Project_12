from utils import main

file_json = 'C:\lessons\KursProject12\operations.json'

def test_load_data():
    assert len(main.load_data(file_json)) >= 0
    assert main.load_data(file_json).count("счет") >= 5
    assert main.load_data (file_json).count ("->") == 5
    assert len(main.load_data(file_json).split("\n\n")) == 6




