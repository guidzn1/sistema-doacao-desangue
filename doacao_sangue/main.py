import tkinter as tk
from sistema import SistemaDoacaoSangue
from tela_login import TelaLogin  

def main():
    root = tk.Tk()
    sistema = SistemaDoacaoSangue()
    tela_login = TelaLogin(root, sistema)
    root.mainloop()

if __name__ == '__main__':
    main()