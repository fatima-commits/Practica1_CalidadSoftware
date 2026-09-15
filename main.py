"""Módulo principal que ejecuta la aplicación de Bitácora de Libros GUI."""

import tkinter as tk
from tkinter import messagebox

from formatting import Formatter
from repositoryBook import BookRepository
from serviceBook import BookService
from typeBook import Book
from validator import Validator


class BookApp:
    """Es la interfaz gráfica principal de la aplicación."""

    def __init__(self, root: tk.Tk) -> None:
        """Inicializa los componentes de la ventana principal."""
        self.root = root
        self.root.title('Bitácora de Lectura y Reseñas')

        repo = BookRepository()
        self.service = BookService(repo)

        self._validator_ref = Validator
        self._book_cls_ref = Book

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
        """Agrega un libro nuevo capturado desde los campos de texto."""
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
                'Asegúrate de llenar todos los campos y de ingresar '
                'una calificación válida entre 1 y 5.',
            )

    def clear_entries(self) -> None:
        """Limpia las entradas de texto del formulario."""
        self.entry_title.delete(0, tk.END)
        self.entry_author.delete(0, tk.END)
        self.entry_rating.delete(0, tk.END)
        self.entry_review.delete(0, tk.END)

    def update_list(self) -> None:
        """Actualiza la lista visual con todos los libros guardados."""
        self.listbox.delete(0, tk.END)
        for book in self.service.repo.get_all_books():
            self.listbox.insert(tk.END, Formatter.format_book_summary(book))

    def show_review(self, event: object) -> None:
        """Muestra una ventana modal con la reseña del libro seleccionado."""
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
