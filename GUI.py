from tkinter import*
from PIL import Image, ImageTk
import speech_to_text
import action
root= Tk()
root.title("AI Asiistant")
root.geometry("850x700")
root.resizable(False, False)
root.config(bg="#78b2cc")


def ask():
    user_val= speech_to_text.speech_to_text()
    bot_val= action.action(user_val)
    text.insert(END, 'User-->'+user_val+"\n")
    if bot_val !=None:
        text.insert(END,'BOT-->'+str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()
        
        
def send():
    send = entry.get()
    bot_val = action.action(send)
    print(bot_val)
    text.insert(END, 'User-->'+send+"\n")
    if bot_val !=None:
        text.insert(END,'BOT-->'+str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()
    # print("send")

    
def delete():
    text.delete('1.0','end')
    # print('delete')

#frame
frame=LabelFrame(root, padx=20, pady=7,borderwidth=3,relief="raised")
frame.config(bg="#7db1c9")
frame.grid(row=0, column=1, padx=85, pady=10)

#text label
text_label= Label(frame, text="AI Assistant", font=("Times New Roman",14,"bold"), bg="#bad1db")
text_label.grid(row=0, column=0, padx=20, pady=10)

#image label
image=ImageTk.PhotoImage(Image.open("imge/image.png"))
image_label= Label(frame, image=image)
image_label.grid(row=1,column=0, pady=20)

#text widget
text=Text(root, font=("Times New Roman", 12, "bold"), bg="#7db1c9")
text.grid(row=2, column=0)
text.place(x=200,y=500,width=450, height=80)

#entry widget
entry= Entry(root, justify=CENTER)
entry.place(x=200,y=590, width=450, height=38)

#button1
button1= Button(root, text="Ask", padx=40, pady=6, borderwidth=1, relief=SOLID, command=ask)
button1.place(x=205,y=640)
#button2
button2= Button(root, text="Send", padx=40, pady=6, borderwidth=1, relief=SOLID, command=send)
button2.place(x=355,y=640)
#button2
button3= Button(root, text="Delete", padx=40, pady=6, borderwidth=1, relief=SOLID, command=delete)
button3.place(x=515,y=640)


root.mainloop()