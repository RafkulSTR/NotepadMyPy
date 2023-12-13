import os
import json



# Путь к файлу с заметками
NOTES_FILE = 'notes.json'

# Функция для загрузки заметок из файла
def load_notes():
    if not os.path.exists(NOTES_FILE):
        return {}
    with open(NOTES_FILE, 'r') as file:
        return json.load(file)

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file, indent=4)

# Функция для создания новой заметки
def create_note():
    notes = load_notes()
    title = input("Введите название заметки: ").strip()
    if title in notes:
        print("Заметка с таким названием уже существует.")
        return
    content = input("Введите текст заметки: ").strip()
    notes[title] = content
    save_notes(notes)
    print("Заметка создана.")

# Функция для чтения списка заметок
def list_notes():
    notes = load_notes()
    if not notes:
        print("Список заметок пуст.")
    else:
        for title in notes:
            print(title)

# Функция для редактирования заметки
def edit_note():
    notes = load_notes()
    title = input("Введите название заметки для редактирования: ").strip()
    if title not in notes:
        print("Заметка не найдена.")
        return
    print("Текущий текст заметки:")
    print(notes[title])
    new_content = input("Введите новый текст заметки: ").strip()
    notes[title] = new_content
    save_notes(notes)
    print("Заметка обновлена.")

# Функция для удаления заметки
def delete_note():
    notes = load_notes()
    title = input("Введите название заметки для удаления: ").strip()
    if title in notes:
        del notes[title]
        save_notes(notes)
        print("Заметка удалена.")
    else:
        print("Заметка не найдена.")

# Главная функция с меню
def main():
    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        choice = input("Выберите пункт меню: ").strip()

        if choice == '1':
            create_note()
        elif choice == '2':
            list_notes()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Неправильный выбор. Пожалуйста, попробуйте снова.")


# Запуск программы
if __name__ == '__main__':
    main()