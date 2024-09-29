import tkinter as tk
from tkinter import messagebox


def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    message = entry_message.get("1.0", tk.END)

    if not name or not email or not message:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
    else:
        messagebox.showinfo("Успех", "Форма успешно отправлена!")
        # Здесь можно добавить код для обработки данных (например, отправка на сервер)


# Создание основного окна
root = tk.Tk()
root.title("Форма заявки")

# Создание меток и полей ввода
label_name = tk.Label(root, text="Имя:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()

entry_email = tk.Entry(root)
entry_email.pack()

label_message = tk.Label(root, text="Сообщение:")
label_message.pack()

entry_message = tk.Text(root, height=5, width=30)
entry_message.pack()

# Кнопка отправки
submit_button = tk.Button(root, text="Отправить", command=submit_form)
submit_button.pack()

# Запуск основного цикла
root.mainloop()
