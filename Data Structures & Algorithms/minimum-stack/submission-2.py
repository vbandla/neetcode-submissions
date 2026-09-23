class MinStack:

    def __init__(self):
        self.minstack = [];
        self.minval=math.inf;

    def push(self, val: int) -> None:
        if not self.minstack :
            self.minstack.append(0);
            self.minval = val;
        else :
            self.minstack.append(val-self.minval);
            if val < self.minval :
                self.minval = val;

    def pop(self) -> None:
        if self.minstack[-1] < 0 :
            self.minval = self.minval - self.minstack[-1];
        self.minstack.pop();

    def top(self) -> int:
        if self.minstack[-1] <= 0 :
            return self.minval;
        return self.minstack[-1] + self.minval

    def getMin(self) -> int:
        return self.minval;