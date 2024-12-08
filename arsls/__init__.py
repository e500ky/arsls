from customtkinter import *
from tkinter import messagebox
import pyshorteners
import pyperclip

# Link kısaltıcı fonksiyonu
class Shorter(pyshorteners.Shortener):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.shortedURL = self.tinyurl.short(self.url)

    def get(self): return self.shortedURL

class GUI(CTk):
    def __init__(self):
        super().__init__()
        self.title('ARSLS - Link Shorter - ArsTech')
        self.geometry('550x300')
        self.resizable(False, False)
        self.gui()
    
    def gui(self):
        self.label = CTkLabel(self, text='URL Shorter', font=('Arial', 45, "bold"))
        self.label.pack(pady=30)

        self.first_fr = CTkFrame(self, corner_radius=0, border_width=0, bg_color=self.label.cget("bg_color"), fg_color=self.label.cget("bg_color"))
        self.first_fr.pack(fill=X, pady=(0, 20))

        self.url_entry = CTkEntry(self.first_fr, font=('Consolas', 20), placeholder_text="Enter URL...", border_width=1, height=40, justify="center")
        self.url_entry.pack(pady=0, fill=X, side=LEFT, anchor="n", expand=True, padx=(25, 12.5))

        self.url_entry.bind("<Return>", lambda event: ((self.convert()) if self.url_entry.get() != "" else ...))

        self.convert_btn = CTkButton(self.first_fr, font=("Arial", 20), text="Convert", width=150, height=40, command=self.convert)
        self.convert_btn.pack(pady=0, side=RIGHT, anchor="n", expand=False, padx=(0, 25))

        self.second_fr = CTkFrame(self, corner_radius=0, border_width=0, bg_color=self.label.cget("bg_color"), fg_color=self.label.cget("bg_color"))
        self.second_fr.pack(fill=X, pady=(0, 12.5), padx=12.5)

        self.converted_label = CTkLabel(self.second_fr, text="Converted URL", font=("Arial", 25, "bold"))
        self.converted_label.pack(padx=12.5, side=TOP, anchor="w", pady=(12.5, 0))
        
        self.converted_entry = CTkEntry(self.second_fr, font=("Consolas", 20), placeholder_text=("Converted URL"), height=40, border_width=1 , state="disabled", justify="center")
        self.converted_entry.pack(pady=(12.5, 0), fill=X, side=BOTTOM, expand=True, padx=(12.5, 12.5))

        self.converted_entry.bind("<Button-1>", lambda event: ((pyperclip.copy(self.converted_entry.get()), messagebox.showinfo("Copied!", f"copied URL: {self.converted_entry.get()}")) if self.converted_entry.get() != "" else ...))

    def convert(self):
        url = self.url_entry.get()
        self.converted_entry.configure(state="normal")
        self.converted_entry.delete(0, END)
        try:
            shorter = Shorter(url)
            self.converted_entry.insert(0, shorter.get())
        except:
            self.converted_entry.insert(0, url)
        self.converted_entry.configure(state="disabled")

def main():
    app = GUI()
    app.mainloop()

if __name__ == '__main__':
    main()