class Node:
    """Yığın içindeki her bir elemanı temsil eden düğüm sınıfı."""

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """LIFO (Last In, First Out) mantığıyla çalışan Yığın veri yapısı."""

    def __init__(self, limit=None):
        self.top = None
        self.size = 0
        self.limit = limit  # İsteğe bağlı kapasite sınırı

    def is_empty(self):
        """Yığının boş olup olmadığını kontrol eder."""
        return self.top is None

    def push(self, data):
        """Yığının en üstüne yeni bir eleman ekler."""
        if self.limit and self.size >= self.limit:
            raise OverflowError("Hata: Stack kapasitesi dolu (Stack Overflow)!")

        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        return True

    def pop(self):
        """Yığının en üstündeki elemanı çıkarır ve döndürür."""
        if self.is_empty():
            raise IndexError("Hata: Boş yığından eleman çıkarılamaz (Stack Underflow)!")

        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data

    def peek(self):
        """Yığının en üstündeki elemanı çıkarmadan değerini döndürür."""
        if self.is_empty():
            return None
        return self.top.data

    def get_all_elements(self):
        """
        Görselleştirme aşamasında yığının güncel halini
        arayüze çizdirmek için kullanacağımız yardımcı metod.
        """
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        return elements


class Queue:
    """FIFO (First In, First Out) mantığıyla çalışan Kuyruk veri yapısı."""

    def __init__(self, limit=None):
        self.front = None  # Kuyruğun başı
        self.rear = None  # Kuyruğun sonu
        self.size = 0
        self.limit = limit

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        """Kuyruğun sonuna (rear) yeni bir eleman ekler."""
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
        """Kuyruğun başındaki (front) elemanı çıkarır ve döndürür."""
        if self.is_empty():
            raise IndexError("Hata: Boş kuyruktan eleman çıkarılamaz!")

        dequeued_node = self.front
        self.front = self.front.next

        # Eğer eleman çıkardıktan sonra kuyruk boş kaldıysa, rear'ı da None yapmalıyız
        if self.front is None:
            self.rear = None

        self.size -= 1
        return dequeued_node.data

    def get_all_elements(self):
        """Arayüzde çizdirmek için kuyruğun elemanlarını liste olarak döndürür."""
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# --- Test Alanı ---
if __name__ == "__main__":
    print("Stack Testi Başlıyor...\n")
    my_stack = Stack(limit=3)

    print("\n--- Queue Testi Başlıyor ---")
    my_queue = Queue(limit=3)
    my_queue.enqueue("Müşteri 1")
    my_queue.enqueue("Müşteri 2")
    my_queue.enqueue("Müşteri 3")
    print(f"Kuyruk (Baştan Sona): {my_queue.get_all_elements()}")

    islem_goren = my_queue.dequeue()
    print(f"İşlem gören (Sıradan çıkan): {islem_goren}")
    print(f"Güncel Kuyruk: {my_queue.get_all_elements()}")

    # Push işlemi
    my_stack.push("Python")
    my_stack.push("Java")
    my_stack.push("C++")
    print(f"Stack içeriği (Üstten alta): {my_stack.get_all_elements()}")

    # Peek işlemi
    print(f"En üstteki eleman (Peek): {my_stack.peek()}")

    # Pop işlemi
    cikarilan = my_stack.pop()
    print(f"Çıkarılan eleman: {cikarilan}")
    print(f"Güncel Stack içeriği: {my_stack.get_all_elements()}")
