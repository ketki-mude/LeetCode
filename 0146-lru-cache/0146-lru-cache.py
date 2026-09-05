class LRUCache:

    def __init__(self, capacity: int):
        self.lrucap=capacity
        self.lrudict={}

        
    def get(self, key: int) -> int:
        if key in self.lrudict:
            
            self.lrudict[key][1]=time.time()
            return self.lrudict[key][0]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        
        if key in self.lrudict:
            self.lrudict[key]=[value,time.time()]

        else:
            if len(self.lrudict)< self.lrucap:
                self.lrudict[key]=[value,time.time()]
            else:
                min_key=None
                min_timestamp=float(inf)
                for element in self.lrudict:
                    if self.lrudict[element][1]<min_timestamp:
                        min_timestamp=self.lrudict[element][1]
                        min_key=element
                
                del self.lrudict[min_key]

                self.lrudict[key]=[value,time.time()]

                    

        
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)