import tkinter as tk
from tkinter import messagebox

from typeBook import Book
from repositoryBook import BookRepository
from validator import Validator
from formatting import Formatter
from serviceBook import BookService


class BookApp:

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title('Bitácora de Lectura y Reseñas')

        repo = BookRepository()
        self.service = BookService(repo)

        self._validator_ref = Validator
        self._book_cls_ref = Book

        # Formulario de entrada
        tk.Label(root, text='Título:').grid(row=0, column=0, sticky='w')
        self.entry_title = tk.Entry(root, width=35)
        self.entry_title.grid(row=0, column=1, pady=2)

        tk.Label(root, text='Autor:').grid(row=1, column=0, sticky='w')
        self.entry_author = tk.Entry(root, width=35)
        self.entry_author.grid(row=1, column=1, pady=2)

        tk.Label(root, text='Calificación (1-5):').grid(
            row=2, column=0, sticky='w'
        )
        self.entry_rating = tk.Entry(root, width=35)
        self.entry_rating.grid(row=2, column=1, pady=2)

        tk.Label(root, text='Reseña:').grid(row=3, column=0, sticky='w')
        self.entry_review = tk.Entry(root, width=35)
        self.entry_review.grid(row=3, column=1, pady=2)

        self.btn_add = tk.Button(
            root, text='Registrar Libro', command=self.add_book
        )
        self.btn_add.grid(row=4, column=0, columnspan=2, pady=5)

        self.listbox = tk.Listbox(root, width=50, height=8)
        self.listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        self.listbox.bind('<<ListboxSelect>>', self.show_review)

    def add_book(self) -> None:
        #Agrega libro
        title = self.entry_title.get()
        author = self.entry_author.get()
        rating = self.entry_rating.get()
        review = self.entry_review.get()

        if self.service.register_book(title, author, rating, review):
            self.clear_entries()
            self.update_list()
            messagebox.showinfo('Éxito', '¡Libro registrado correctamente!')
        else:
            messagebox.showerror(
                'Error de Validación',
                'Asegúrate de llenar todos los campos y de ingresa '
                'una calificación válida entre 1 y 5.',
            )

    def clear_entries(self) -> None:
        #Limpiar datos
        self.entry_title.delete(0, tk.END)
        self.entry_author.delete(0, tk.END)
        self.entry_rating.delete(0, tk.END)
        self.entry_review.delete(0, tk.END)

    def update_list(self) -> None:
        #actualiza lista
        self.listbox.delete(0, tk.END)
        for book in self.service.repo.get_all_books():
            self.listbox.insert(tk.END, Formatter.format_book_summary(book))

    def show_review(self, event: object) -> None:
        #mostrar reseña
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            book = self.service.repo.get_all_books()[index]
            messagebox.showinfo(
                f'Reseña de {book.title}',
                f'Autor: {book.author}\n'
                f'Calificación: {book.rating}/5 estrellas\n\n'
                f'Reseña:\n"{book.review}"',
            )


if __name__ == '__main__':
    window = tk.Tk()
    app = BookApp(window)
    window.mainloop()