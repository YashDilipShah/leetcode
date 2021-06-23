"""
981. Time Based Key-Value Store
Medium

Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

    Stores the key and value, along with the given timestamp.

2. get(string key, int timestamp)

    Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
    If there are multiple such values, it returns the one with the largest timestamp_prev.
    If there are no values, it returns the empty string ("").

 

Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1);  // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); //output "bar2"   

Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]

 

Note:

    All key/value strings are lowercase.
    All key/value strings have length in the range [1, 100]
    The timestamps for all TimeMap.set operations are strictly increasing.
    1 <= timestamp <= 10^7
    TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.

"""




import bisect
class TimeMap:

    def __init__(self):
        
        self.database = {}

    def set(self, key : str, value : str, timestamp: int) -> None:
        if key in self.database.keys():
            self.database[key][timestamp] = value
            #self.database[key] = sorted(self.database[key], key=self.database.keys())
        else:
            self.database[key] = {}
            self.database[key][timestamp] = value
            #self.database[key] = sorted(self.database[key], key=self.database.keys())
        return None
        
        
    def get(self, key: str, timestamp: int) -> str:

        if key not in self.database:
            return ""
        else:
            keys = list(self.database[key].keys())
            if timestamp < keys[0]:
                return ""
            req = keys[bisect.bisect_right(keys, timestamp) - 1]
            return self.database[key][req]


def driver(commands, inputs):
    outputs = []
    commands = commands[1:]
    inputs = inputs[1:]
    obj = TimeMap()
    for i, j in zip(commands, inputs):
        if i == "set":
            outputs.append(obj.set(j[0], j[1], j[2]))
        elif i == "get":
            outputs.append(obj.get(j[0], j[1]))
    return outputs


obj = TimeMap()
obj.set("foo", "bar", 1)
print(obj.get("foo", 1))
print(driver(["TimeMap","set","get","get","set","get","get"], 
            [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]))
