"""Модуль для анализа изменений курсов валют"""

from typing import Dict, Any, List


class RateAnalyzer:
    """Анализирует изменения курсов валют"""
    
    @staticmethod
    def analyze_rate(rate: Dict[str, Any]) -> Dict[str, Any]:
        """
        Анализирует один курс: вычисляет изменение и процент.
        
        Args:
            rate: словарь с полями code, name, value, previous
        
        Returns:
            словарь с добавленными полями change, change_percent, trend
        """
        value = rate.get('value', 0)
        previous = rate.get('previous', 0)
        
        if previous == 0:
            change = 0
            change_percent = 0
            trend = "→"
        else:
            change = value - previous
            change_percent = (change / previous) * 100
            
            if change > 0:
                trend = "▲"
            elif change < 0:
                trend = "▼"
            else:
                trend = "→"
        
        return {
            **rate,
            'change': round(change, 4),
            'change_percent': round(change_percent, 2),
            'trend': trend
        }
    
    @staticmethod
    def analyze_all(rates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Анализирует список курсов"""
        return [RateAnalyzer.analyze_rate(rate) for rate in rates]
    
    @staticmethod
    def get_changes_only(rates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Возвращает только те курсы, которые изменились"""
        analyzed = RateAnalyzer.analyze_all(rates)
        return [r for r in analyzed if r['change'] != 0]