import random
import subprocess
from lists import a_list, b_list, c_list


def nick_gen():
    f1 = random.choice(a_list)
    f2 = random.choice(b_list)
    f3 = random.choice(c_list)
    f4 = random.choice(c_list)
    f5 = random.choice(c_list)
    f6 = random.choice(c_list)
    return f"{f1}-{f2}-{f3}{f4}{f5}{f6}"




def copiar(text):
    process= subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
    process.communicate(input=text.encode('utf-8'))
    print(f"'{text}' <- your cool ass nickname was copied! ")







resp = input("Do you want a fucking cool JIM nickname to match your friends social currency? (yes/no): ").strip().lower()

 
if resp == "yes":
    nick = nick_gen()
    print(f"Your nickname is: {nick}")
    copiar(nick)
elif resp == "no":
    print("Go home, coward")
else:
    print("answer it right, newbie")
    









