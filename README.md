```markdown
# 🤖 Telegram-бот для сборки компьютеров

## 📖 Описание
Telegram-бот, который помогает пользователям собирать компьютеры, предоставляя информацию о различных комплектующих и готовых сборках. Бот упрощает процесс выбора компонентов и предлагает актуальные цены, ссылки на покупку и характеристики.

## 🚀 Функциональность
- **Выбор комплектующих**: Возможность выбирать процессоры, видеокарты, оперативную память и другие компоненты.
- **Готовые сборки**: Предоставление готовых сборок для игр, офисной работы и рендеринга.
- **Информация о компонентах**: Актуальные ссылки на покупку, цены и описание характеристик.

## 🔧 Установка
1. **Клонируйте репозиторий:**
   ```bash
   git clone <URL вашего репозитория>
   cd <имя_папки_репозитория>
   ```
2. **Установите необходимые библиотеки:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Настройте токен API и другие параметры в файле `config.py`:**
   ```python
   API_TOKEN = 'ваш_токен_бота'
   ADMIN_ID = 'ваш_ID_администратора'
   ```

## 💻 Использование
- Запустите бота:
  ```bash
  python bot.py
  ```
- Откройте Telegram и найдите вашего бота по имени пользователя, указанному при его создании.
- Начните взаимодействие с ботом, используя команду `/start`.

## 📜 Команды
- `/start` - Приветствие и основные инструкции.
- `/choose_components` - Выбор комплектующих для сборки компьютера.
- `/select_ready_builds` - Просмотр готовых сборок по категориям (игры, офис, рендеринг и т. д.).

## 🗂 Структура проекта
- `bot.py` - Основной файл бота.
- `config.py` - Файл конфигурации (токены и ID).
- `handlers.py` - Обработчики команд и callback-запросов.
- `builds.py` - Данные о готовых сборках и комплектующих.
- `requirements.txt` - Список необходимых библиотек.

## 📄 Лицензия
Этот проект лицензирован под MIT License. Подробности можно найти в файле `LICENSE`.

## 📬 Контакты
Если у вас есть вопросы или предложения, вы можете связаться с разработчиком по адресу электронной почты: <ваш_email>.
```
