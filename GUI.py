from tkinter import filedialog, messagebox, Tk, Label, Entry, Button
import subprocess

root = Tk()
root.geometry('340x230')
root.resizable(width=False, height=False)
root.title("GUI для генератора IPv6 от Vikulin")

already_running = False


def start():
    global already_running
    if not already_running:
        already_running = True
        ygg_nice_ipv6_exe_path = filedialog.askopenfilename(filetypes=(("Ygg_nice_ipv6.exe", "*.exe"),))
        subprocess.Popen(
            f"{ygg_nice_ipv6_exe_path} {matching_bytes_field.get()} {ipv6_limit_field.get()} {what_to_search_field.get()}",
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        # пока вывод в никуда, потом сделаем консоль
        messagebox.showinfo("Запущено", "Не закрывайте GUI, так как это остановит генератор. Как узнать ключи ("
                                        "результат работы "
                                        "программы), мы ещё не придумали.")
        # из-за root.destroy() гуи закрывается, и все субпроцессы тоже
    else:
        messagebox.showerror("Ошибка", "Генератор уже работает!")


repeated_bytes = Label(root, text="Число повторяющихся байтов")
matching_bytes_field = Entry(root, width=11, font='Arial 14')

gen = Label(root, text="Сколько ipv6 будет пройдено")
ipv6_limit_field = Entry(root, width=11, font='Arial 14')

key = Label(root, text="Совпадающие части")
what_to_search_field = Entry(root, width=11, font='Arial 14', )
text_pred = Label(root, text="(Можно оставить пустым)")

go = Button(text="Запуск программы", width=15, height=3, bg="#99746C", fg='#FFFFFF', font='arial 14', command=start)

matching_bytes_field.place(x=180, y=1)
repeated_bytes.place(x=0, y=1)

gen.place(x=0, y=26)
ipv6_limit_field.place(x=180, y=26)

key.place(x=0, y=52)
what_to_search_field.place(x=180, y=52)
text_pred.place(x=0, y=70)

go.place(x=80, y=120)

root.mainloop()
