import pytest
from click.testing import CliRunner
from homeproject import *

FILENAME = "GlobalLandTemperaturesByMajorCity.csv"

def test_default():
    """Тест для праметров по умолчанию"""
    runner = CliRunner()

    result = runner.invoke(run, [f'{"--filename="}{FILENAME}'])
    #captured = capsys.readouterr()
    expected_out_start = "               City            avg_temp\n"
    "0        Umm Durman            29.62125"
    
    assert result.exit_code == 0
    assert result.output.startswith(expected_out_start), result.output
    
    
@pytest.mark.parametrize("count", [-5,-12,1,989, 132])    
def test_count(count):
    """Тест для проверки count"""
    runner = CliRunner()

    result = runner.invoke(run, [f'{"--filename="}{FILENAME}', f'{"--count="}{count}'])
    #captured = capsys.readouterr()
    if (count < 0):
        expected_out_start = "Некоректное значение count!"
    elif (count > 100):
        expected_out_start = "Всего 100 городов в данных!"
        expected_out_end = "[100 rows x 2 columns]\n"
        assert result.exit_code == 0
        assert result.output.endswith(expected_out_end), result.output[-8:]
    else:
        expected_out_start = "         City  avg_temp"
    assert result.exit_code == 0
    assert result.output.startswith(expected_out_start), "start"+result.output
    
    