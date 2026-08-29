class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache={}

    def get(self, key: int) -> int:
        if key not in self.cache:
            
            return -1

        else:
            self.cache[key][1]=time.time()
            
            return self.cache[key][0]
    
    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.cache[key]=[value,time.time()]
            return

        if len(self.cache) < self.capacity:
            self.cache[key]= [value,time.time()]
                  
        else:
            min_timestamp = float('inf')
            key_of_min_time= None

            for keys in self.cache:
                timestamp= self.cache[keys][1]
                
                if timestamp<min_timestamp:
                    min_timestamp=timestamp

                    key_of_min_time= keys
   
            del self.cache[key_of_min_time]
            
            self.cache[key]=[value,time.time()]

            




