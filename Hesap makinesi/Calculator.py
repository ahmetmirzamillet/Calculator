import tkinter as x


def butona_tikla(buton_metni):
    entry1.insert(x.END, buton_metni)


def hesapla():
    try:
        ifade = entry1.get()
        sonuc = eval(ifade)
        entry1.delete(0, x.END)
        entry1.insert(x.END, str(sonuc))
    except:
        entry1.delete(0, x.END)
        entry1.insert(x.END, "Hata")
def temizlik():
    entry1.delete(0, x.END)


def bir_önceki():
    mevcut_metni = entry1.get()
    if mevcut_metni:
        entry1.delete(len(mevcut_metni)-1, x.END)


arayüz =x.Tk()
arayüz.geometry("250x280")
arayüz.title("Hesap Makinesi")


entry1 = x.Entry(arayüz,width=35, font=("Arial",24))
entry1.grid(row=0, column=0,columnspan=30,sticky="w")

buton_width=5
buton_height=2

button1 = x.Button(arayüz, text="1", command=lambda: butona_tikla("1"), width=buton_width, height=buton_height)
button1.grid(column=0,row=1)

button2 = x.Button(arayüz, text="2", command=lambda: butona_tikla("2"),width=buton_width, height=buton_height)
button2.grid(column=1,row=1)

button3 = x.Button(arayüz, text="3",command=lambda: butona_tikla("3"),width=buton_width, height=buton_height)
button3.grid(column=2,row=1)

button4 = x.Button(arayüz, text="4", command=lambda: butona_tikla("4"),width=buton_width, height=buton_height)
button4.grid(column=0,row=2)

button5 = x.Button(arayüz, text="5", command=lambda: butona_tikla("5"),width=buton_width, height=buton_height)
button5.grid(column=1,row=2)

button6 = x.Button(arayüz, text="6", command=lambda: butona_tikla("6"),width=buton_width, height=buton_height)
button6.grid(column=2,row=2)

button7 = x.Button(arayüz, text="7", command=lambda: butona_tikla("7"),width=buton_width, height=buton_height)
button7.grid(column=0,row=3)

button8 = x.Button(arayüz, text="8", command=lambda: butona_tikla("8"),width=buton_width, height=buton_height)
button8.grid(column=1,row=3)

button9 = x.Button(arayüz, text="9", command=lambda: butona_tikla("9"),width=buton_width, height=buton_height)
button9.grid(column=2,row=3)

button0 = x.Button(arayüz, text="0", command=lambda: butona_tikla("0"),width=buton_width, height=buton_height)
button0.grid(column=1,row=4)

button10 = x.Button(arayüz, text="+", command=lambda: butona_tikla("+"),width=buton_width, height=buton_height)
button10.grid(column=3,row=1)

button11 = x.Button(arayüz, text="-", command=lambda: butona_tikla("-"),width=buton_width, height=buton_height)
button11.grid(column=3,row=2)

button12 = x.Button(arayüz, text="x", command=lambda: butona_tikla("*"),width=buton_width, height=buton_height)
button12.grid(column=3,row=3)

button13 = x.Button(arayüz, text="/", command=lambda: butona_tikla("/"),width=buton_width, height=buton_height)
button13.grid(column=3,row=4)

button14 = x.Button(arayüz, text="C", command=temizlik,width=buton_width, height=buton_height)
button14.grid(column=1,row=5)

button15 = x.Button(arayüz, text="(", command=lambda: butona_tikla("("),width=buton_width, height=buton_height)
button15.grid(column=0,row=4)

button16 = x.Button(arayüz, text=")", command=lambda: butona_tikla(")"),width=buton_width, height=buton_height)
button16.grid(column=2,row=4)

button17 = x.Button(text=",", command=lambda: butona_tikla(","),width=buton_width, height=buton_height)
button17.grid(column=2,row=5)

button18 = x.Button(arayüz, text="<--" ,width=buton_width, height=buton_height,command=bir_önceki)
button18.grid(column=0,row=5)

button19 = x.Button(arayüz, text="=",width=buton_width, height=buton_height,command=hesapla)
button19.grid(column=3,row=5)

arayüz.mainloop()
