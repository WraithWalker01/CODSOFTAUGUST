import tkinter as tk
from tkinter import ttk


class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.style = ttk.Style()
        self.style.configure("Treeview",
                             background="#E1E1E1",
                             fieldbackground="#E1E1E1",
                             foreground="#000000")
        self.style.map("Treeview", background=[("selected", "#007ACC")])

        self.task_label = tk.Label(root, text="Task:", font=("Helvetica", 12))
        self.task_label.pack()

        self.task_entry = tk.Entry(root, font=("Helvetica", 12))
        self.task_entry.pack(pady=5)

        self.due_label = tk.Label(root, text="Due Date (optional):", font=("Helvetica", 12))
        self.due_label.pack()

        self.due_entry = tk.Entry(root, font=("Helvetica", 12))
        self.due_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Helvetica", 12))
        self.add_button.pack()

        self.task_tree = ttk.Treeview(root, columns=("Description", "Due Date", "Status"), show="headings")
        self.task_tree.heading("Description", text="Description")
        self.task_tree.heading("Due Date", text="Due Date")
        self.task_tree.heading("Status", text="Status")
        self.task_tree.pack()

        self.complete_button = tk.Button(root, text="Mark Completed", command=self.mark_completed,
                                         font=("Helvetica", 12))
        self.complete_button.pack()

        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task, font=("Helvetica", 12))
        self.edit_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, font=("Helvetica", 12))
        self.delete_button.pack()

    def add_task(self):
        task_description = self.task_entry.get()
        due_date = self.due_entry.get()

        new_task = Task(task_description, due_date)
        self.tasks.append(new_task)
        self.task_tree.insert("", "end", values=(new_task.description, new_task.due_date, "Pending"))

        self.task_entry.delete(0, "end")
        self.due_entry.delete(0, "end")

    def mark_completed(self):
        selected_item = self.task_tree.selection()
        if selected_item:
            item_index = int(self.task_tree.index(selected_item))
            if not self.tasks[item_index].completed:
                self.tasks[item_index].completed = True
                self.task_tree.item(selected_item, values=(self.tasks[item_index].description,
                                                           self.tasks[item_index].due_date,
                                                           "Completed"))

    def edit_task(self):
        selected_item = self.task_tree.selection()
        if selected_item:
            item_index = int(self.task_tree.index(selected_item))
            new_description = self.task_entry.get()
            new_due_date = self.due_entry.get()
            self.tasks[item_index].description = new_description
            self.tasks[item_index].due_date = new_due_date
            self.task_tree.item(selected_item, values=(new_description, new_due_date, "Pending"))

    def delete_task(self):
        selected_item = self.task_tree.selection()
        if selected_item:
            item_index = int(self.task_tree.index(selected_item))
            del self.tasks[item_index]
            self.task_tree.delete(selected_item)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
