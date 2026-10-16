#!/usr/bin/env python
"""
Currency Tracker — мониторинг курсов валют с уведомлениями.

Использование:
    python scripts/run.py
    python scripts/run.py --currencies USD,EUR,CNY
    python scripts/run.py --all
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import click
from typing import List

from core.api_client import CBRClient
from core.storage import CSVStorage
from core.analyzer import RateAnalyzer
from core.notifier import ConsoleNotifier


# Валюты по умолчанию
DEFAULT_CURRENCIES = ['USD', 'EUR', 'CNY']


@click.command()
@click.option(
    '--currencies', '-c',
    default=','.join(DEFAULT_CURRENCIES),
    help='Список валют через запятую (например: USD,EUR,CNY)'
)
@click.option(
    '--all', 'all_currencies',
    is_flag=True,
    help='Показать все валюты из API'
)
@click.option(
    '--file', '-f',
    default='data/rates.csv',
    help='Путь к CSV-файлу для сохранения'
)
def main(currencies: str, all_currencies: bool, file: str):
    """Мониторинг курсов валют с API ЦБ РФ"""
    
    # 1. Получаем данные
    client = CBRClient()
    data = client.get_all_rates()
    
    if not data:
        ConsoleNotifier.print_error("Не удалось получить данные от API ЦБ РФ")
        return
    
    # 2. Определяем список валют
    valutes = data.get('valutes', {})
    
    if all_currencies:
        currency_list = list(valutes.keys())
    else:
        currency_list = [c.strip().upper() for c in currencies.split(',')]
    
    # 3. Собираем курсы
    rates = []
    for code in currency_list:
        if code in valutes:
            valute = valutes[code]
            rates.append({
                'code': code,
                'name': valute.get('Name', ''),
                'value': valute.get('Value', 0),
                'previous': valute.get('Previous', 0),
                'nominal': valute.get('Nominal', 1)
            })
    
    if not rates:
        ConsoleNotifier.print_error("Не найдено ни одной валюты")
        return
    
    # 4. Анализируем
    analyzed = RateAnalyzer.analyze_all(rates)
    
    # 5. Выводим
    date_str = data.get('date', '')[:10]
    if date_str:
        from datetime import datetime
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            date_str = date_obj.strftime('%d.%m.%Y')
        except:
            pass
    
    ConsoleNotifier.print_header(date_str)
    ConsoleNotifier.print_rates(analyzed)
    
    # 6. Итоги
    changed = len([r for r in analyzed if r['change'] != 0])
    ConsoleNotifier.print_summary(len(analyzed), changed)
    
    # 7. Сохраняем
    storage = CSVStorage(file)
    storage.save_rates(analyzed, date_str)
    ConsoleNotifier.print_saved(file)


if __name__ == '__main__':
    main()