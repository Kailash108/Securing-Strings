print("Welcome to BasiEncrypt.")
import tkinter as tk
window = tk.Tk()
window.geometry('340x110')
window.config(bg='black')
window.title("BasiEncrypt")
def final():
    result = ''
    for i in field.get():
        if(i==' '):
            result = result + ' '
        elif(i >= 'A' and i <= 'Z'):
            result = result + chr(ord(i) - 7)
            answer = tk.Label(text=f"The Encrypted Key Is '{result}'", bg="black", fg="white")
            answer.place(y = 90)
        elif(i >= '0' and i <= '9'):
            result = result + chr(ord(i) - 7)
            answer = tk.Label(text=f"The Encrypted Key Is '{result}'", bg="black", fg="white")
            answer.place(y=90)
        elif(i >= 'a' and i <= 'z'):
            result = result + chr(ord(i) - 6)
            answer = tk.Label(text=f"The Encrypted Key Is '{result}'", bg="black", fg="white")
            answer.place(y=90)
        else:
            result = result + chr(ord(i))
            answer = tk.Label(text=f"The Encrypted Key Is '{result}'", bg="black", fg="white", cursor="target")
            answer.place(y=90)
    print(f"The Encrypted Key For Your Input({field.get()})\nIs\n{result}")


text = tk.Label(text="String Encrypt", font=(30), bg="black", fg="green")
text.place(x=100)

text2 = tk.Label(text="Enter The Word/Sentence: ", bg="gold")
field = tk.Entry(width='30', bg="grey", fg="white")
text2.place(x=0, y=30)
field.place(x=150,y=31)

but = tk.Button(command=final, text="Encrypt", bg="gold")
but.place(x=140, y=60)

window.mainloop()