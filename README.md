# Currency Tracker

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Мониторинг курсов валют с API ЦБ РФ и уведомлениями в консоль.**

Консольный инструмент для отслеживания курсов валют. Получает данные от официального API Центробанка РФ, анализирует изменения и сохраняет историю в CSV.

**📚 [Смотреть все проекты в портфолио](https://github.com/Alex-top/portfolio)**

---

## 📋 Возможности

| Функция | Описание |
|---------|----------|
| **Получение курсов** | Данные от API ЦБ РФ (актуальные на сегодня) |
| **Анализ изменений** | Сравнение с предыдущим значением, расчёт % |
| **Уведомления** | Цветной вывод в консоль (▲ рост, ▼ падение) |
| **Сохранение истории** | Запись всех данных в CSV-файл |
| **Выбор валют** | Отслеживание конкретных валют или всех сразу |

---

## 🧠 Архитектура проекта

---
## 🛠 Технологии
Python 3.10+

requests — HTTP-запросы к API

click — CLI-интерфейс

CSV — хранение данных
---

## 🚀 Установка и запуск:
1. Настройка виртуального окружения:
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate          # Windows

3. Установка зависимостей:
```bash
pip install -r requirements.txt

4. Запуск проекта:
```bash
python scripts/run.py
---

## Дополнительные команды:
# Все валюты из API
python scripts/run.py --all

# Конкретные валюты
python scripts/run.py --currencies USD,GBP,JPY

# Другой файл для сохранения
python scripts/run.py --file data/my_rates.csv
---

### 1. Клонирование

```bash
git clone https://github.com/Alex-top/currency-tracker.git
cd currency-tracker