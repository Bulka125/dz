import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as file:
            notes = json.load(file)
        return notes
    else:
        return []

def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file, indent=2)

def add_note(title, message):
    notes = load_notes()
    note_id = len(notes) + 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = {
        "id": note_id,
        "title": title,
        "message": message,
        "timestamp": timestamp
    }
    notes.append(new_note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def list_notes(filter_date=None):
    notes = load_notes()
    if filter_date:
        filtered_notes = [note for note in notes if note['timestamp'].startswith(filter_date)]
        notes = filtered_notes
    if not notes:
        print("Список заметок пуст.")
    else:
        for note in notes:
            print(f"ID: {note['id']}\nЗаголовок: {note['title']}\nДата/время: {note['timestamp']}\nТело: {note['message']}\n")

def edit_note(note_id, new_title, new_message):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            note['title'] = new_title
            note['message'] = new_message
            note['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным ID не найдена")

def delete_note(note_id):
    notes = load_notes()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    print("Заметка успешно удалена")

if __name__ == "__main__":
    while True:
        command = input("Введите команду (add/list/edit/delete/exit): ").lower()

        if command == "add":
            title = input("Введите заголовок заметки: ")
            message = input("Введите тело заметки: ")
            add_note(title, message)

        elif command == "list":
            filter_date = input("Введите дату для фильтрации (yyyy-mm-dd): ")
            list_notes(filter_date)

        elif command == "edit":
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_message = input("Введите новое тело заметки: ")
            edit_note(note_id, new_title, new_message)

        elif command == "delete":
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)

        elif command == "exit":
            break

        else:
            print("Неверная команда. Попробуйте снова.")