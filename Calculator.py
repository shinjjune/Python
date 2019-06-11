from tkinter import*
window = Tk()

window.title("My_calculator")
disp=Entry(window, width=33, bg="gold")
disp.grid(row=0,column=0,columnspan=5)

button_list=["7","8","9","/","C",
            "4","5","6","*"," ",
            "1","2","3","-"," ",
            "0",".","=","+"," "]

def click(key):
    if key=="=":
        result=eval(disp.get())
        s=str(result)
        disp.insert(END,"="+s)
    elif key=="C":
        disp.delete(0,END)
    else: disp.insert(END)

row_index=1
col_index=0

for button_text in button_list:
    def process(t=button_text):
        click(t)
    Button(window, text=button_text, width=5, command=process).grid(row=row_index, column=col_index)
    col_index +=1
    if col_index>4:
        col_index=0
        row_index+=1
