"""Клиент для работы с API ЦБ РФ"""

import requests
from datetime import datetime
from typing import Dict, Any, Optional


class CBRClient:
    """Клиент для получения курсов валют с API ЦБ РФ"""
    
    BASE_URL = "https://www.cbr-xml-daily.ru/daily_json.js"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "CurrencyTracker/1.0"
        })
    
    def get_all_rates(self) -> Optional[Dict[str, Any]]:
        """
        Получает все курсы валют.
        Возвращает словарь с датой и курсами или None при ошибке.
        """
        try:
            response = self.session.get(self.BASE_URL, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            return {
                "date": data.get("Date", ""),
                "timestamp": data.get("Timestamp", ""),
                "valutes": data.get("Valute", {})
            }
        except requests.exceptions.RequestException as e:
            print(f"❌ Ошибка запроса к API: {e}")
            return None
        except ValueError as e:
            print(f"❌ Ошибка парсинга JSON: {e}")
            return None
    
    def get_rate(self, code: str) -> Optional[Dict[str, Any]]:
        """
        Получает курс конкретной валюты по коду (USD, EUR, CNY).
        """
        all_rates = self.get_all_rates()
        if not all_rates:
            return None
        
        valutes = all_rates.get("valutes", {})
        if code.upper() not in valutes:
            print(f"⚠️ Валюта {code} не найдена")
            return None
        
        valute = valutes[code.upper()]
        return {
            "code": code.upper(),
            "name": valute.get("Name", ""),
            "value": valute.get("Value", 0),
            "previous": valute.get("Previous", 0),
            "nominal": valute.get("Nominal", 1)
        }