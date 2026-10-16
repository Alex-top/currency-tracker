"""Модуль для сохранения курсов валют в CSV"""

import csv
import os
from datetime import datetime
from typing import Dict, Any, List


class CSVStorage:
    """Хранилище курсов валют в CSV-файле"""
    
    def __init__(self, file_path: str = "data/rates.csv"):
        self.file_path = file_path
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Создаёт файл с заголовками, если его нет"""
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        
        need_create = False
        
        if not os.path.exists(self.file_path):
            need_create = True
        else:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()
                if not first_line or 'date' not in first_line:
                    need_create = True
        
        if need_create:
            with open(self.file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'date', 'currency_code', 'currency_name',
                    'rate', 'previous_rate', 'change', 'change_percent'
                ])
    
    def save_rates(self, rates: List[Dict[str, Any]], date_str: str = None):
        """Сохраняет курсы в CSV"""
        if not date_str:
            date_str = datetime.now().strftime('%Y-%m-%d')
        
        with open(self.file_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for rate in rates:
                writer.writerow([
                    date_str,
                    rate['code'],
                    rate['name'],
                    rate['value'],
                    rate['previous'],
                    rate['change'],
                    rate['change_percent']
                ])
    
    def get_previous_rates(self, code: str) -> Dict[str, Any]:
        """Получает последний сохранённый курс для валюты"""
        if not os.path.exists(self.file_path):
            return {}
        
        last_rate = None
        with open(self.file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['currency_code'] == code:
                    last_rate = row
        
        return last_rate or {}