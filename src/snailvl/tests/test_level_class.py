from ..level import *
from pathlib import Path

class TestLevelClass:
    test_level = Level(str(Path(__file__).parent // "data\TestLevel1.lvl"))

    def test_raw_get_and_write(self):
        test_data_one = self.test_level.getRawLevel()
        self.test_level.writeRawLevel(test_data_one)
        test_data_two = self.test_level.getRawLevel()
        assert test_data_one == test_data_two

    def test_get_and_write(self):
        test_data_one = self.test_level.getLevel()
        self.test_level.writeLevel(test_data_one)
        test_data_two = self.test_level.getLevel()
        assert test_data_one == test_data_two