


class Calculator:
    def __init__(self):
        self.operations= {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
        self.last_result= None
        self.result_chain= []



    def run(self):

        if self.last_result is None:
            a = float(input("Enter a: "))
        else:
            a= float(self.last_result)

        op = input("Choose operation: ")



        if op.lower()== "ce":
            self.last_result= None
            self.result_chain= []
            print("0")
            return True

        elif op.lower()=="exit":
            print("Goodbye!")
            print(self.last_result)
            return False

        if op not in self.operations:
            print("Invalid operation")
            return True

        else:
            b = float(input("Enter b: "))
            result = self.operations[op](a, b)
            if result is not None:
                self.result_chain.append(result)
                self.last_result = result
            print(result)
            return True


    def add(self,a,b):
        return (a+b)

    def subtract(self,a,b):
        return (a-b)

    def multiply(self,a,b):
        return (a*b)

    def divide(self,a,b):
        if b == 0:
            print("Cannot divide by 0")
            return None
        else:
            return (a/b)
