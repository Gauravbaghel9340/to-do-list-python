import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"{self.title} - {self.description} [{status}]"

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        # Frame for title and description entry
        input_frame = tk.Frame(self.root, padx=10, pady=10)
        input_frame.pack(pady=10)

        # Title Entry
        tk.Label(input_frame, text="Task Title:").grid(row=0, column=0, pady=5)
        self.title_entry = tk.Entry(input_frame, width=50)
        self.title_entry.grid(row=0, column=1, pady=5)

        # Description Entry
        tk.Label(input_frame, text="Task Description:").grid(row=1, column=0, pady=5)
        self.description_entry = tk.Entry(input_frame, width=50)
        self.description_entry.grid(row=1, column=1, pady=5)

        # Buttons Frame
        buttons_frame = tk.Frame(self.root, padx=10, pady=10)
        buttons_frame.pack()

        self.add_button = tk.Button(buttons_frame, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white")
        self.add_button.grid(row=0, column=0, padx=5)

        self.update_button = tk.Button(buttons_frame, text="Update Task", command=self.update_task, bg="#2196F3", fg="white")
        self.update_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(buttons_frame, text="Delete Task", command=self.delete_task, bg="#F44336", fg="white")
        self.delete_button.grid(row=0, column=2, padx=5)

        # Tasks Listbox Frame
        listbox_frame = tk.Frame(self.root, padx=10, pady=10)
        listbox_frame.pack(pady=10)

        self.tasks_listbox = tk.Listbox(listbox_frame, width=70, height=15)
        self.tasks_listbox.pack(side=tk.LEFT)

        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tasks_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tasks_listbox.yview)

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        if title:
            task = Task(title, description)
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, str(task))
            self.title_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task title is required.")

    def update_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            title = self.title_entry.get()
            description = self.description_entry.get()
            completed = messagebox.askyesno("Mark Completed", "Is the task completed?")

            if title:
                self.tasks[index].title = title
            if description:
                self.tasks[index].description = description
            if completed:
                self.tasks[index].mark_complete()

            self.tasks_listbox.delete(index)
            self.tasks_listbox.insert(index, str(self.tasks[index]))
            self.title_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Selection Error", "Select a task to update.")

    def delete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.tasks_listbox.delete(index)
        else:
            messagebox.showwarning("Selection Error", "Select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
