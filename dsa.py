import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For background image support

# Stack Implementation
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return "Stack is empty. Cannot pop."
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty. No top element."
        else:
            return self.stack[-1]

    def clear(self):
        self.stack.clear()

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack


# Queue Implementation
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty. Cannot dequeue."
        else:
            return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty. No front element."
        else:
            return self.queue[0]

    def clear(self):
        self.queue.clear()

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        return self.queue


# Singly Linked List Implementation
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = SLLNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, value):
        current = self.head
        previous = None
        while current and current.data != value:
            previous = current
            current = current.next

        if current is None:
            return f"Value {value} not found in the linked list."
        else:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next
            return f"Deleted {value} from the linked list."

    def display(self):
        if not self.head:
            return "Singly Linked List is empty."
        else:
            current = self.head
            values = []
            while current:
                values.append(current.data)
                current = current.next
            return values


# Doubly Linked List Implementation (DLL)
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = DLLNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, value):
        current = self.head
        while current and current.data != value:
            current = current.next

        if current is None:
            return f"Value {value} not found in the doubly linked list."
        else:
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
            if current == self.head:
                self.head = current.next
            return f"Deleted {value} from the doubly linked list."

    def display(self):
        if not self.head:
            return "Doubly Linked List is empty."
        else:
            current = self.head
            values = []
            while current:
                values.append(current.data)
                current = current.next
            return values


# GUI Implementation using Tkinter
class DataStructureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Structure Visualizer")

        # Set the window size to full screen
        self.root.geometry("1200x800")
        self.root.config(bg="lightblue")

        # Load background image (make sure to place an image file in the project directory)
        self.bg_image = Image.open("C:\\Users\\ADMIN\\Desktop\\DSA.jpg")
        self.bg_image = self.bg_image.resize((1200, 800), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a label for the background image
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create instances of data structures
        self.stack = Stack()
        self.queue = Queue()
        self.sll = SinglyLinkedList()
        self.dll = DoublyLinkedList()

        # Add a big title with a prominent font style
        self.title_label = tk.Label(self.root, text="Data Structure Visualizer", font=("Helvetica", 36, "bold"), bg="lightblue", fg="black")
        self.title_label.pack(pady=20)

        # Create a frame to hold all data structure sections horizontally
        self.main_frame = tk.Frame(self.root, bg="lightblue")
        self.main_frame.pack(pady=10, fill="both", expand=True)

        # Create frames for each data structure section
        self.stack_frame = self.create_section_frame("Stack", self.main_frame)
        self.queue_frame = self.create_section_frame("Queue", self.main_frame)
        self.sll_frame = self.create_section_frame("Singly Linked List", self.main_frame)
        self.dll_frame = self.create_section_frame("DLL", self.main_frame)

        # Call functions to create widgets for each data structure
        self.create_stack_widgets()
        self.create_queue_widgets()
        self.create_sll_widgets()
        self.create_dll_widgets()

    def create_section_frame(self, title, parent_frame):
        frame = tk.Frame(parent_frame, bg="lightblue", width=280)
        frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)

        section_label = tk.Label(frame, text=title, font=("Helvetica", 18, "bold"), bg="lightblue")
        section_label.pack(pady=10)

        return frame

    def create_input_with_clear(self, parent_frame):
        entry_frame = tk.Frame(parent_frame, bg="lightblue")
        entry_frame.pack(pady=5, fill="x")

        entry = tk.Entry(entry_frame, font=("Helvetica", 14))
        entry.pack(side="left", fill="x", expand=True)

        clear_button = tk.Button(entry_frame, text="X", command=lambda: entry.delete(0, tk.END), font=("Helvetica", 14))
        clear_button.pack(side="right")

        return entry

    def create_stack_widgets(self):
        # Stack UI
        self.stack_input = self.create_input_with_clear(self.stack_frame)

        self.stack_push_button = tk.Button(self.stack_frame, text="Push", command=self.stack_push, font=("Helvetica", 14))
        self.stack_push_button.pack(pady=5, fill="x")

        self.stack_pop_button = tk.Button(self.stack_frame, text="Pop", command=self.stack_pop, font=("Helvetica", 14))
        self.stack_pop_button.pack(pady=5, fill="x")

        self.stack_peek_button = tk.Button(self.stack_frame, text="Peek", command=self.stack_peek, font=("Helvetica", 14))
        self.stack_peek_button.pack(pady=5, fill="x")

        self.stack_clear_button = tk.Button(self.stack_frame, text="Clear", command=self.stack_clear, font=("Helvetica", 14))
        self.stack_clear_button.pack(pady=5, fill="x")

        self.stack_display_button = tk.Button(self.stack_frame, text="Display", command=self.stack_display, font=("Helvetica", 14))
        self.stack_display_button.pack(pady=5, fill="x")

        # Display result for Stack operations
        self.stack_result = tk.Label(self.stack_frame, text="", font=("Helvetica", 14), bg="lightblue")
        self.stack_result.pack(pady=5, fill="x")

    def stack_push(self):
        value = self.stack_input.get()
        if value:
            self.stack.push(value)
            self.stack_result.config(text=f"Pushed {value} to stack")
        else:
            self.stack_result.config(text="Please enter a value to push.")

    def stack_pop(self):
        result = self.stack.pop()
        self.stack_result.config(text=f"Pop result: {result}")

    def stack_peek(self):
        result = self.stack.peek()
        self.stack_result.config(text=f"Top element: {result}")

    def stack_clear(self):
        self.stack.clear()
        self.stack_result.config(text="Stack cleared.")

    def stack_display(self):
        result = self.stack.display()
        self.stack_result.config(text=f"Stack: {result}")

    def create_queue_widgets(self):
        # Queue UI
        self.queue_input = self.create_input_with_clear(self.queue_frame)

        self.queue_enqueue_button = tk.Button(self.queue_frame, text="Enqueue", command=self.queue_enqueue, font=("Helvetica", 14))
        self.queue_enqueue_button.pack(pady=5, fill="x")

        self.queue_dequeue_button = tk.Button(self.queue_frame, text="Dequeue", command=self.queue_dequeue, font=("Helvetica", 14))
        self.queue_dequeue_button.pack(pady=5, fill="x")

        self.queue_peek_button = tk.Button(self.queue_frame, text="Peek", command=self.queue_peek, font=("Helvetica", 14))
        self.queue_peek_button.pack(pady=5, fill="x")

        self.queue_clear_button = tk.Button(self.queue_frame, text="Clear", command=self.queue_clear, font=("Helvetica", 14))
        self.queue_clear_button.pack(pady=5, fill="x")

        self.queue_display_button = tk.Button(self.queue_frame, text="Display", command=self.queue_display, font=("Helvetica", 14))
        self.queue_display_button.pack(pady=5, fill="x")

        # Display result for Queue operations
        self.queue_result = tk.Label(self.queue_frame, text="", font=("Helvetica", 14), bg="lightblue")
        self.queue_result.pack(pady=5, fill="x")

    def queue_enqueue(self):
        value = self.queue_input.get()
        if value:
            self.queue.enqueue(value)
            self.queue_result.config(text=f"Enqueued {value} to queue")
        else:
            self.queue_result.config(text="Please enter a value to enqueue.")

    def queue_dequeue(self):
        result = self.queue.dequeue()
        self.queue_result.config(text=f"Dequeue result: {result}")

    def queue_peek(self):
        result = self.queue.peek()
        self.queue_result.config(text=f"Front element: {result}")

    def queue_clear(self):
        self.queue.clear()
        self.queue_result.config(text="Queue cleared.")

    def queue_display(self):
        result = self.queue.display()
        self.queue_result.config(text=f"Queue: {result}")

    # Singly Linked List Widgets
    def create_sll_widgets(self):
        self.sll_input = self.create_input_with_clear(self.sll_frame)

        self.sll_insert_button = tk.Button(self.sll_frame, text="Insert", command=self.sll_insert,
                                           font=("Helvetica", 14))
        self.sll_insert_button.pack(pady=5, fill="x")

        self.sll_delete_button = tk.Button(self.sll_frame, text="Delete", command=self.sll_delete,
                                           font=("Helvetica", 14))
        self.sll_delete_button.pack(pady=5, fill="x")

        self.sll_display_button = tk.Button(self.sll_frame, text="Display", command=self.sll_display,
                                            font=("Helvetica", 14))
        self.sll_display_button.pack(pady=5, fill="x")

        # Create a scrollable text area for the result
        self.sll_result = tk.Text(self.sll_frame, height=5, width=50, wrap=tk.WORD, font=("Helvetica", 14))
        self.sll_result.pack(pady=5, fill="x")

        # Add scrollbar
        self.sll_scrollbar = tk.Scrollbar(self.sll_result)
        self.sll_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.sll_result.config(yscrollcommand=self.sll_scrollbar.set)
        self.sll_scrollbar.config(command=self.sll_result.yview)

    def sll_insert(self):
        value = self.sll_input.get()
        if value:
            self.sll.insert(value)
            self.sll_result.delete(1.0, tk.END)  # Clear any existing text
            self.sll_result.insert(tk.END, f"Inserted {value} into SLL")
        else:
            self.sll_result.delete(1.0, tk.END)  # Clear any existing text
            self.sll_result.insert(tk.END, "Please enter a value to insert.")

    def sll_delete(self):
        value = self.sll_input.get()
        if value:
            result = self.sll.delete(value)
            self.sll_result.delete(1.0, tk.END)  # Clear any existing text
            self.sll_result.insert(tk.END, result)
        else:
            self.sll_result.delete(1.0, tk.END)  # Clear any existing text
            self.sll_result.insert(tk.END, "Please enter a value to delete.")

    def sll_display(self):
        result = self.sll.display()
        self.sll_result.delete(1.0, tk.END)  # Clear any existing text
        if result == "Singly Linked List is empty.":
            self.sll_result.insert(tk.END, result)
        else:
            # Limit the number of elements to display (e.g., 10)
            max_display = 10
            display_result = result[:max_display]  # Display only the first 10 elements
            formatted_result = " -> ".join(str(x) for x in display_result)

            # Check if there are more elements
            if len(result) > max_display:
                formatted_result += " -> ... (more elements)"

            self.sll_result.insert(tk.END, f"Singly Linked List: {formatted_result}")

    # Doubly Linked List Widgets
    def create_dll_widgets(self):
        self.dll_input = self.create_input_with_clear(self.dll_frame)

        self.dll_insert_button = tk.Button(self.dll_frame, text="Insert", command=self.dll_insert,
                                           font=("Helvetica", 14))
        self.dll_insert_button.pack(pady=5, fill="x")

        self.dll_delete_button = tk.Button(self.dll_frame, text="Delete", command=self.dll_delete,
                                           font=("Helvetica", 14))
        self.dll_delete_button.pack(pady=5, fill="x")

        self.dll_display_button = tk.Button(self.dll_frame, text="Display", command=self.dll_display,
                                            font=("Helvetica", 14))
        self.dll_display_button.pack(pady=5, fill="x")

        # Create a scrollable text area for the result
        self.dll_result = tk.Text(self.dll_frame, height=5, width=50, wrap=tk.WORD, font=("Helvetica", 14))
        self.dll_result.pack(pady=5, fill="x")

        # Add scrollbar for the Text widget
        self.dll_scrollbar = tk.Scrollbar(self.dll_result)
        self.dll_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.dll_result.config(yscrollcommand=self.dll_scrollbar.set)
        self.dll_scrollbar.config(command=self.dll_result.yview)

    def dll_insert(self):
        value = self.dll_input.get()
        if value:
            self.dll.insert(value)
            self.dll_result.config(text=f"Inserted {value} into DLL")
        else:
            self.dll_result.config(text="Please enter a value to insert.")

    def dll_delete(self):
        value = self.dll_input.get()
        if value:
            result = self.dll.delete(value)
            self.dll_result.config(text=result)
        else:
            self.dll_result.config(text="Please enter a value to delete.")

    def dll_display(self):
        result = self.dll.display()
        self.dll_result.delete(1.0, tk.END)  # Clear any existing text
        if result == "Doubly Linked List is empty.":
            self.dll_result.insert(tk.END, result)
        else:
            # Limit the number of elements to display (e.g., 10)
            max_display = 10
            display_result = result[:max_display]  # Display only the first 10 elements
            formatted_result = " <-> ".join(str(x) for x in display_result)

            # Check if there are more elements
            if len(result) > max_display:
                formatted_result += " <-> ... (more elements)"

            self.dll_result.insert(tk.END, f"Doubly Linked List: {formatted_result}")


# Start the app
root = tk.Tk()
app = DataStructureApp(root)
root.mainloop()
