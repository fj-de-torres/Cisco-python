class Queue():
    def __init__(self):
        queue_list = list()
    
    def put(self,element):
        self.queue_list.append(element)
    
    def get(self):
        if len(self.queue_list)>0:
            val = self.queue_list.pop(0)