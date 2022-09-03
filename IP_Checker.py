import subprocess
import os

while True:
    addre = input("write down the first 3 octet (Exemple : 192.168.1.) : \n")
    _from = int(input("from i.e. 192.168.1.1 :\n"))
    _to = int(input("to i.e. 192.168.1.200 :\n"))
    with open(os.devnull, "wb") as limbo:
        for n in range(_from, _to):
                ip=str(addre) +"{0}".format(n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print (ip, " inactive")
                else:
                        print (ip, " active")
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break

