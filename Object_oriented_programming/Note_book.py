class Note(object) :
    def __init__(self, content = None) :
        self.content = content
    
    def write_content(self, new_content) :
        self.content = new_content 
    
    def remove_all(self) :
        self.content = ""
    
    def __add__(self, other) :
        return self.content + other.content
    
    def __str__(self) :
        return self.content
class NoteBook(object) :
    def __init__(self, title) :
        self.title = title
        self.page_num = 1
        self.notes = {}
    
    def add_note(self, note, page = 0) :
        if self.page_num < 300 :
            if page == 0 :
                self.notes[self.page_num] = note
                self.page_num += 1
            else :
                self.notes = {page : note}
                self.page_num += 1
        else :
            print("페이지가 모두 채워졌습니다.")
    
    def remove_note(self, page_num) :
        if page_num in self.notes.keys() :
            return self.notes.pop(page_num)
        else :
            print("해당 페이지는 존재하지 않습니다.")
            
    def get_number_of_pages(self) :
        return len(self.notes.keys())