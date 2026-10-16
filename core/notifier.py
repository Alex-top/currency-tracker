"""Модуль для вывода уведомлений о курсах валют"""

from datetime import datetime
from typing import Dict, Any, List


class ConsoleNotifier:
    """Выводит уведомления о курсах валют в консоль"""
    
    # Эмодзи для популярных валют
    CURRENCY_FLAGS = {
        'USD': '🇺🇸',
        'EUR': '🇪🇺',
        'CNY': '🇨🇳',
        'GBP': '🇬🇧',
        'JPY': '🇯🇵',
        'CHF': '🇨🇭',
        'TRY': '🇹🇷',
        'KZT': '🇰🇿',
        'BYN': '🇧🇾',
        'UAH': '🇺🇦',
    }
    
    @staticmethod
    def print_header(date_str: str = None):
        """Печатает заголовок"""
        if not date_str:
            date_str = datetime.now().strftime('%d.%m.%Y')
        
        print()
        print("=" * 50)
        print(f"📊 Мониторинг курсов валют — {date_str}")
        print("=" * 50)
        print()
    
    @staticmethod
    def print_rate(rate: Dict[str, Any]):
        """Печатает один курс"""
        code = rate.get('code', '?')
        name = rate.get('name', '?')
        value = rate.get('value', 0)
        change = rate.get('change', 0)
        change_percent = rate.get('change_percent', 0)
        trend = rate.get('trend', '→')
        
        flag = ConsoleNotifier.CURRENCY_FLAGS.get(code, '🏳️')
        
        # Форматируем изменение
        if change > 0:
            change_str = f"▲ +{change:.2f} (+{change_percent:.2f}%)"
            color = "\033[92m"  # зелёный
        elif change < 0:
            change_str = f"▼ {change:.2f} ({change_percent:.2f}%)"
            color = "\033[91m"  # красный
        else:
            change_str = "→ без изменений"
            color = "\033[93m"  # жёлтый
        
        reset = "\033[0m"
        
        print(f"{flag} {code}: {value:.2f} ₽  {color}{change_str}{reset}")
    
    @staticmethod
    def print_rates(rates: List[Dict[str, Any]]):
        """Печатает список курсов"""
        for rate in rates:
            ConsoleNotifier.print_rate(rate)
    
    @staticmethod
    def print_summary(total: int, changed: int):
        """Печатает итоговую информацию"""
        print()
        print("-" * 50)
        print(f"📈 Всего валют: {total}")
        print(f"🔄 Изменилось: {changed}")
        print("-" * 50)
    
    @staticmethod
    def print_saved(file_path: str):
        """Сообщает о сохранении данных"""
        print(f"\n✅ Данные сохранены в {file_path}")
    
    @staticmethod
    def print_error(message: str):
        """Печатает ошибку"""
        print(f"\n❌ Ошибка: {message}")