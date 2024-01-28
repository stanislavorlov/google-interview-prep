# Design a logger system that receives a stream of messages along with their timestamps. 
# Each unique message should only be printed at most every 10 seconds 
# (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

# Input
# ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
# [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
# Output
# [null, true, true, false, false, false, true]

# Explanation
#Logger logger = new Logger();
#logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
#logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
#logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
#logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
#logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
#logger.shouldPrintMessage(11, "foo"); // 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21

from collections import defaultdict

class Logger:
    def __init__(self):
        self.timeMap = {}
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        cur = self.timeMap.get(message)
        if cur is None or timestamp >= cur + 10:
            self.timeMap[message] = timestamp
            return True
        return False
    
class Logger2:
    def __init__(self) -> None:
        self.expiry = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.expiry[message] > timestamp:
            return False
        self.expiry[message] = timestamp + 10
        return True

logger = Logger2()
print(logger.shouldPrintMessage(1, "foo"))      #true
print(logger.shouldPrintMessage(2, "bar"))      #true
print(logger.shouldPrintMessage(3, "foo"))      #false
print(logger.shouldPrintMessage(8, "bar"))      #false
print(logger.shouldPrintMessage(10, "foo"))     #false
print(logger.shouldPrintMessage(11, "foo"))     #true