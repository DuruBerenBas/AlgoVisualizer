class Node:
    """Veri yapılarındaki her bir elemanı temsil eden düğüm sınıfı."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """LIFO (Last In, First Out) mantığıyla çalışan Yığın veri yapısı."""
    def __init__(self, limit=None):
        self.top = None
        self.size = 0
        self.limit = limit

    def is_empty(self):
        return self.top is None

    def push(self, data):
        if self.limit and self.size >= self.limit:
            raise OverflowError("Hata: Stack kapasitesi dolu (Stack Overflow)!")
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        return True

    def pop(self):
        if self.is_empty():
            raise IndexError("Hata: Boş yığından eleman çıkarılamaz (Stack Underflow)!")
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def get_all_elements(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        return elements

class Queue:
    """FIFO (First In, First Out) mantığıyla çalışan Kuyruk veri yapısı."""
    def __init__(self, limit=None):
        self.front = None
        self.rear = None
        self.size = 0
        self.limit = limit

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        if self.limit and self.size >= self.limit:
            raise OverflowError("Hata: Kuyruk kapasitesi dolu!")
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Hata: Boş kuyruktan eleman çıkarılamaz!")
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeued_node.data

    def get_all_elements(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        return elements

class LinkedList:
    """Elemanların birbirine referans (pointer) ile bağlandığı Tek Yönlü Bağlı Liste."""
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def get_all_elements(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# ==========================================
# --- TEST ALANI ---
# ==========================================
if __name__ == "__main__":
    print("--- Stack Testi ---")
    my_stack = Stack()
    my_stack.push("A")
    my_stack.push("B")
    print(f"Stack: {my_stack.get_all_elements()}")

    print("\n--- Queue Testi ---")
    my_queue = Queue()
    my_queue.enqueue("1")
    my_queue.enqueue("2")
    print(f"Queue: {my_queue.get_all_elements()}")

    print("\n--- Linked List Testi ---")
    my_list = LinkedList()
    my_list.insert_at_tail("Düğüm 1")
    my_list.insert_at_tail("Düğüm 2")
    my_list.insert_at_head("Yeni Baş")
    print(f"Linked List: {my_list.get_all_elements()}")