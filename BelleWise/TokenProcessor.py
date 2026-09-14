from TypeManager import TypeManager as TM

class TokenProcessor:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_index = 0
    
    def __repr__(self):
        return f"<TokenProcessor obj with {len(self.tokens)} tokens and current index {self.current_index}>"
    
    def get_next_token(self):
        if self.current_index < len(self.tokens):
            token = self.tokens[self.current_index]
            self.current_index += 1
            return token
        else:
            return None
    
    def basic_func(self):
        token = self.get_next_token #! first one
        if token == "run":
            token = self.get_next_token 
            if token == "print":
                print(self.get_next_token)
            elif token == "sum":
                sum_arr = []
                while True:
                    t = self.get_next_token
                    if TM(t).find_type() in ('int',"real"):
                        sum_arr.append(t)
                    if t is None:
                        break
                print(sum(sum_arr))