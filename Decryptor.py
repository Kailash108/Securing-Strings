print("Welcome to BasiDecrypt.")
import tkinter as tk
window = tk.Tk()
window.geometry('400x160')
window.config(bg='black')
window.title("BasiDecrypt")
def final():
    result = ''
    for i in field.get():
        if(i == ' '):
            result = result + ' '
            answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
            answer.place(y=115, x=160)
        elif(ord(i)>=33 and ord(i)<=47):
            win = tk.Label(text='Need Special Chars\nYes Or No')
            win.place(y=110)

            def yes():
                result = ''
                for i in field.get():
                    if(ord(i) >= 33 and ord(i) <= 57):
                        result = result + chr(ord(i))
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif(ord(i)>=48 and ord(i)<=57):
                        result = result + chr(ord(i)+7)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 91 and ord(i) <= 96):
                        result = result + chr(ord(i))
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 97 and ord(i) <= 122):
                        result = result + chr(ord(i))
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 58 and ord(i) <= 64):
                        result = result + chr(ord(i))
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 65 and ord(i) <= 90):
                        result = result + chr(ord(i)+7)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)

                print(f"The Decrypted Key For Your Input({field.get()})\nIs\n{result}")

            def no():
                result = ''
                for i in field.get():
                    if (ord(i) >= 41 and ord(i) <= 47):
                        result = result + chr(ord(i)+7)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif(ord(i)>=33 and ord(i)<=40):
                        result = result + chr(ord(i))
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 48 and ord(i) <= 57):
                        result = result + chr(ord(i) + 7)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 91 and ord(i) <= 122):
                        result = result + chr(ord(i)+6)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 58 and ord(i) <= 90):
                        result = result + chr(ord(i)+7)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)

                print(f"The Decrypted Key For Your Input({field.get()})\nIs\n{result}")


            que = tk.Button(text='Yes', command=yes)
            que.place(y=100, x=110)

            que1 = tk.Button(text='No', command=no)
            que1.place(y=130, x=110)

        elif (ord(i) >= 97 and ord(i) <= 122):
            win = tk.Label(text='Need Special Chars\nYes Or No')
            win.place(y=110)

            def yes():
                result = ''
                for i in field.get():
                    if (ord(i) >= 33 and ord(i) <= 47):
                        result = result + chr(ord(i))
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 48 and ord(i) <= 57):
                        result = result + chr(ord(i) + 7)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 91 and ord(i) <= 96):
                        result = result + chr(ord(i))
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 97 and ord(i) <= 122):
                        result = result + chr(ord(i)+6)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 58 and ord(i) <= 64):
                        result = result + chr(ord(i))
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 65 and ord(i) <= 90):
                        result = result + chr(ord(i) + 7)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)

                print(f"The Decrypted Key For Your Input({field.get()})\nIs\n{result}")

            def no():
                result = ''
                for i in field.get():
                    if (ord(i) >= 41 and ord(i) <= 47):
                        result = result + chr(ord(i)+7)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 33 and ord(i) <= 40):
                        result = result + chr(ord(i))
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 48 and ord(i) <= 57):
                        result = result + chr(ord(i) + 7)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 91 and ord(i) <= 122):
                        result = result + chr(ord(i)+6)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 58 and ord(i) <= 90):
                        result = result + chr(ord(i)+7)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)

                print(f"The Decrypted Key For Your Input({field.get()})\nIs\n{result}")

            que = tk.Button(text='Yes', command=yes)
            que.place(y=100, x=110)

            que1 = tk.Button(text='No', command=no)
            que1.place(y=130, x=110)

        elif(ord(i)>=58 and ord(i)<=96):

            win = tk.Label(text='Need Special Chars\nYes Or No')
            win.place(y=110)

            def yes():
                result = ''
                for i in field.get():
                    if (ord(i) >= 33 and ord(i) <= 47):
                        result = result + chr(ord(i))
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 48 and ord(i) <= 57):
                        result = result + chr(ord(i) + 7)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 91 and ord(i) <= 96):
                        result = result + chr(ord(i))
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif(ord(i)>=97 and ord(i)<=122):
                        result = result + chr(ord(i)+6)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 58 and ord(i) <= 64):
                        result = result + chr(ord(i))
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 65 and ord(i) <= 90):
                        result = result + chr(ord(i) + 7)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)

                print(f"The Decrypted Key For Your Input({field.get()})\nIs\n{result}")

            def no():
                result = ''
                for i in field.get():
                    if (ord(i) >= 41 and ord(i) <= 47):
                        result = result + chr(ord(i)+7)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 33 and ord(i) <= 40):
                        result = result + chr(ord(i))
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 48 and ord(i) <= 57):
                        result = result + chr(ord(i)+7)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 91 and ord(i) <= 122):
                        result = result + chr(ord(i) + 6)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)
                    elif (ord(i) >= 58 and ord(i) <= 90):
                        result = result + chr(ord(i)+7)
                        answer = tk.Label(text=f"The Decrypted Key Is '{result}'", bg="black", fg="white")
                        answer.place(y=115, x=160)

                print(f"The Decrypted Key For Your Input({field.get()})\nIs\n{result}")

            que = tk.Button(text='Yes', command=yes)
            que.place(y=100, x=110)

            que1 = tk.Button(text='No', command=no)
            que1.place(y=130, x=110)

    print(f"The Decrypted Key For Your Input({field.get()})\nIs\n{result}")


text = tk.Label(text="String Decrypt", font=(30), bg="black", fg="green")
text.place(x=135)

text2 = tk.Label(text="Enter The Word/Sentence: ", bg="gold")
field = tk.Entry(width='30', bg="grey", fg="white")
text2.place(x=0, y=30)
field.place(x=150,y=31)

but = tk.Button(command=final, text="Decrypt", bg="gold")
but.place(x=140, y=60)

window.mainloop()