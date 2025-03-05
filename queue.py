from os import system

class QueueError(Exception):
    def __init__(self, message="Empty list"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

class Queue():
    def __init__(self):
        self.queue_list = list()
    
    def put(self, element):
        self.queue_list.insert(0, element)
    
    def get(self):
        if len(self.queue_list) > 0:
            val = self.queue_list.pop(0)
            return val
        else:
            raise QueueError("Empty list error!")

if __name__ == "__main__":
    system("cls || clear")
    
    que = Queue()
    que.put(1)
    que.put("Perro")
    que.put(False)
    
    try:
        for i in range(4):
            print(que.get())
    except QueueError as e:
        print("Queue error!", str(e))
    except Exception:
        print("Warning: Non tracked error!")