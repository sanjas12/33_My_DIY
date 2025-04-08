## Prerequisites ()
>=Python 3.9
0. py --list                            -> какие установлены питоны
Если py -0 показывает, что у вас установлены Python 3.11 и 3.8, но при вводе python в CMD запускается 3.8, значит, в переменной окружения PATH путь к Python 3.8 стоит выше, чем к 3.11.
1. установка uv                         -> pip install uv 
2. Создание виртуального окружения      -> python -m venv venv 
3. Активация виртуального окружения     -> source venv/Scripts/activate
4. Установка зависимостей через uv      -> cd diy-app/backend/ && uv pip install -e .

### Usage

### help
python -m pip install -r requirements.txt --no-index --find-links=d:/temp/python_Library/

uv pip compile pyproject.toml -o requirements.txt   # Создайте requirements.txt с помощью uv

uv pip install -r requirements.txt   # Для установки зависимостей через uv:

TODO
Задача	            Модель/Инструмент	Сложность интеграции
Генерация текста	Bloom, GPT-J	        Высокая (требует GPU)
Анализ изображений	FoodAI, YOLOv8	        Средняя
Рекомендации	    LightFM, Sentence-BERT	Низкая
Голосовой интерфейс	Whisper + TTS	        Средняя

### Usage - Develeper (Windows)
cd diy-app/backend/ && uvicorn main:app --reload