
import socket
import re
from functools import reduce

def main():
    HOST = "2048.challs.olicyber.it"
    PORT = 10007

def calcola(line):
    try:
        parts = line.strip().split()
        op = parts[0]
        nums = list(map(float, parts[1:]))

        if op == "SOMMA":
            res = nums[0] + nums[1]
        elif op == "DIFFERENZA":
            res = nums[0] - nums[1]
        elif op == "PRODOTTO":
            res = reduce(lambda x, y: x * y, nums)
        elif op == "DIVISIONE_INTERA":
            res = nums[0] // nums[1]
        elif op == "POTENZA":
            base = int(nums[0])
            exp = int(nums[1])
            res = pow(base, exp)
        else:
            return "operazione sconosciuta"

        if res == int(res):
            res_str = str(int(res))
        else:
            res_str = str(res)
        res_filtrato = ''.join(c for c in res_str if c.isdigit() or c == '-')

        return res_filtrato 

    except Exception as e:
        return f"errore: {str(e)}"

    with socket.create_connection((HOST, PORT)) as sock:
        buffer = ""
        while True:
            data = sock.recv(1024).decode()
            buffer += data
            print(data, end='')

            lines = buffer.strip().split("\n")
            for line in lines:
                if re.match(r"^(SOMMA|DIFFERENZA|PRODOTTO|DIVISIONE_INTERA|POTENZA)", line):
                    risposta = calcola(line)
                    print(f"risposta: {risposta}")
                    sock.sendall((risposta + "\n").encode())
                    buffer = ""
                    break

if __name__ == "__main__":
    main()