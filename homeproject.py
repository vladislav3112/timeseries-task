import click
import pandas as pd


@click.command()
@click.option("--filename", required=True, help='Путь к файлу')
@click.option("--year", default=2000, help='Год наблюдений')
@click.option("--count", default=5, help='Число самых жарких городов за год.')
def run(year: int, filename: str, count: int):
    """Выдает CONUT самых жарких городов по наблюдениям за YEAR год
        Данные о погоде перутся из FILENAME"""
    
    if (year > 2013 or year < 1900):
        print("Данные только в период с 1900 по 2013 год!")
        return
    
    if (count > 100):
        print("Всего 100 городов в данных!\n")
    
    if (count < 1):
        print("Некоректное значение count!\n")
        return
    
    try:
        data = pd.read_csv(filename, parse_dates=["dt"])
    except(FileNotFoundError):
        print("Неправильный путь к файлу!")
        return
    
    data.index = data['dt'].values
    data = data.drop('dt', axis=1)
    data = data[data.index.year == year]
    values = []
    
    res = pd.DataFrame()
    unique_cities = data.City.unique()
    res['City'] = unique_cities
    
    for city in unique_cities:
        data_city = data[data['City'] == city]['AverageTemperature']
        data_city = data_city.resample('Y').mean()
        data_city.index = data_city.index.year
        values.append(data_city.values.squeeze())
    res['avg_temp'] = values
    print(res.sort_values(ascending=False, by='avg_temp', ignore_index=True).head(count))

if __name__ == "__main__":
    run()