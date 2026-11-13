class MyException(Exception):
    def __init__(self, err, *args):
        #super().__init__(*args)
        print(f"Te lanzaste un error {err}")

try:
    raise MyException("Llevatelo")
except:
    print("Piazo e loco")