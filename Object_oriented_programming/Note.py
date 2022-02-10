from Note_book import Note
from Note_book import NoteBook

my_notebook = NoteBook("python object oriented programming")
my_notebook
new_note = Note("python")
print(new_note)
new_note_2 = Note("python lecture")
print(new_note_2)
my_notebook.add_note(new_note_2, )
my_notebook.add_note(new_note_2, 100)
print(my_notebook.get_number_of_pages())
print(my_notebook.notes[100])

