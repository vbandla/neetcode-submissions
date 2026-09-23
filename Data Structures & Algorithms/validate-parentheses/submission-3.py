class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 :
            return False;
        arr=[];
        
        for i in range(len(s)) :
            if s[i] == '{' :
                arr.append('{');
            elif s[i] == '(' :
                arr.append('(');
            elif s[i] == '[' :
                arr.append('[');
            elif s[i] == '}' :
                if len(arr) == 0 or (len(arr) != 0 and arr.pop() != '{') :
                    return False;
            elif s[i] == ')' :
                if len(arr) == 0 or (len(arr) != 0 and arr.pop() != '(') :
                    return False;
            elif s[i] == ']' :
                if len(arr) == 0 or (len(arr) != 0 and arr.pop() != '[') :
                    return False;
        if len(arr) != 0 :
            return False;
        return True;