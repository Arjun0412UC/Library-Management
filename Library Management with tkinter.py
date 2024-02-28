class Table:
    def __init__(self,root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, font=('Times New Roman',16))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

def remove(widgets):
    for i in range(len(widgets)):
        widgets[i].destroy()

def _filter():
    global filter_choice_label, filter_novel_button, filter_reference_button, detail_entry, filter_button, v, filter_widgets, detail_choice_menu, o, filter_detail_choice_label
    
    v = IntVar()
    o = StringVar()
    o.set("Detail to Filter by")
        
    filter_choice_label = Label(root, text = "Do you wish to search for : ", font = ("Times New Roman", 17))
    filter_choice_label.place(x = 500, y = 150, anchor = CENTER)
    
    filter_novel_button = Radiobutton(root, text = "Novel", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 1)
    filter_novel_button.place(x = 250, y = 225, anchor = CENTER)
    
    filter_reference_button = Radiobutton(root, text = "Reference Book", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 2)
    filter_reference_button.place(x = 750, y = 225, anchor = CENTER)

    filter_detail_choice_label = Label(root, text = "Do you wish to Filter by : ", font = ("Times New Roman", 14))
    filter_detail_choice_label.place(x = 500, y = 275, anchor = CENTER)

    detail_choice_menu = OptionMenu(root, o, "Display All", "Book Name", "Publication", "Author Name", "Genre/Subject")
    detail_choice_menu.place(x = 475, y = 325, anchor = E)
    detail_choice_menu.config(width =25)

    detail_entry = Entry(root, width = 40)
    detail_entry.place(x = 500, y = 325, anchor = W)

    filter_button = Button(root, text = "Filter", height = 2, width = 10, font = ("Times New Roman", 12), command = lambda:[check_filter()])
    filter_button.place(x = 500, y = 425, anchor = CENTER)

    filter_widgets = [filter_choice_label, filter_novel_button, filter_reference_button, detail_entry, filter_button, detail_choice_menu, filter_detail_choice_label]
    if a == 1:
        back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(filter_widgets), student(), back_button.destroy()])
        back_button.place(x = 50, y = 50, anchor = CENTER)
    elif a == 2:
        back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(filter_widgets), teacher(), back_button.destroy()])
        back_button.place(x = 50, y = 50, anchor = CENTER)

def check_filter():
    global total_rows, total_columns, lst, l
    r = v.get()
    s = o.get()
    if r == 0 or o == "Detail to Filter by":
        window = Toplevel(root)
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Please Select an option", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(filter_widgets), _filter()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        if r == 1:
            l = [("Novel Number", "Novel Name", "Publication", "Author Name", "Genre")]
            cursor.execute('select novel_no from novels')
            data=cursor.fetchall()
            novels=[]
            for i in data:
                novels.append(i[0])
            if novels == []:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "No Novels in the library", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(filter_widgets), _filter()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                if s == "Display All":
                    a="select Novel_No,Novel_name,Publication,Author_Name,Genre from novels where availability=1"
                    cursor.execute(a)
                    data=cursor.fetchall()
                    if data == []:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Error!")
                        error_label = Label(window, text = "No Novels available", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(filter_widgets), _filter()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                    else:
                        window = Tk()
                        window.title("All Novels")
                        lst = l + data
                        total_rows = len(lst)
                        total_columns = len(lst[0])
                        t = Table(window)
                elif s == "Book Name":
                    detail = detail_entry.get()
                    a="select Novel_no, Novel_Name, Publication, Author_Name, Genre from novels where Novel_Name='{}' and Availability=1".format(detail)
                    cursor.execute(a)
                    data=cursor.fetchall()
                    if data == []:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Error!")
                        error_label = Label(window, text = "No Novel available in this name", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(filter_widgets), _filter()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                    else:
                        window = Tk()
                        window.title("Novel Name")
                        lst = l + data
                        total_rows = len(lst)
                        total_columns = len(lst[0])
                        t = Table(window)
                elif s == "Publication":
                    detail = detail_entry.get()
                    a="select Novel_no, Novel_Name, Publication, Author_Name, Genre from novels where Publication='{}' and Availability=1".format(detail)
                    cursor.execute(a)
                    data=cursor.fetchall()
                    if data == []:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Error!")
                        error_label = Label(window, text = "No Novel available with this Publication", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(filter_widgets), _filter()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                    else:
                        window = Tk()
                        window.title("Publication")
                        lst = l + data
                        total_rows = len(lst)
                        total_columns = len(lst[0])
                        t = Table(window)
                elif s == "Author Name":
                    detail = detail_entry.get()
                    a="select Novel_no, Novel_Name, Publication, Author_Name, Genre from novels where Author_Name='{}' and Availability=1".format(detail)
                    cursor.execute(a)
                    data=cursor.fetchall()
                    if data == []:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Error!")
                        error_label = Label(window, text = "No Novel available with this Author", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(filter_widgets), _filter()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                    else:
                        window = Tk()
                        window.title("Author")
                        lst = l + data
                        total_rows = len(lst)
                        total_columns = len(lst[0])
                        t = Table(window)
                elif s == "Genre/Subject":
                    detail = detail_entry.get()
                    a="select Novel_no, Novel_Name, Publication, Author_Name, Genre from novels where Genre='{}' and Availability=1".format(detail)
                    cursor.execute(a)
                    data=cursor.fetchall()
                    if data == []:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Error!")
                        error_label = Label(window, text = "No Novel available with this Genre", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(filter_widgets), _filter()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                    else:
                        window = Tk()
                        window.title("Genre")
                        lst = l + data
                        total_rows = len(lst)
                        total_columns = len(lst[0])
                        t = Table(window)
        elif r == 2:
            l = [("Reference Book Number", "Reference Book Name", "Publication", "Author Name", "Subject")]
            cursor.execute('select Reference_Book_No from reference where availability=1')
            data=cursor.fetchall()
            reference=[]
            for i in data:
                reference.append(i[0])
            if reference == []:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "No Reference Books in the library", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(filter_widgets), _filter()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                if s == "Display All":
                    a="select Reference_Book_No, Reference_Book_Name, Publication, Author_Name, Subject from reference where Availability=1"
                    cursor.execute(a)
                    data=cursor.fetchall()
                    if data == []:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Error!")
                        error_label = Label(window, text = "No Reference Book available", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(filter_widgets), _filter()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                    else:
                        window = Tk()
                        window.title("All Novels")
                        lst = l + data
                        total_rows = len(lst)
                        total_columns = len(lst[0])
                        t = Table(window)
                elif s == "Book Name":
                    detail = detail_entry.get()
                    a="select Reference_Book_No, Reference_Book_Name, Publication, Author_Name, Subject from reference where Reference_Book_Name='{}' and Availability=1".format(detail)
                    cursor.execute(a)
                    data=cursor.fetchall()
                    if data == []:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Error!")
                        error_label = Label(window, text = "No Reference Book available in this name", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(filter_widgets), _filter()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                    else:
                        window = Tk()
                        window.title("Novel Name")
                        lst = l + data
                        total_rows = len(lst)
                        total_columns = len(lst[0])
                        t = Table(window)
                elif s == "Publication":
                    detail = detail_entry.get()
                    a="select Reference_Book_No, Reference_Book_Name, Publication, Author_Name, Subject from reference where Publication='{}' and Availability=1".format(detail)
                    cursor.execute(a)
                    data=cursor.fetchall()
                    if data == []:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Error!")
                        error_label = Label(window, text = "No Reference Book available with this Publication", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(filter_widgets), _filter()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                    else:
                        window = Tk()
                        window.title("Publication")
                        lst = l + data
                        total_rows = len(lst)
                        total_columns = len(lst[0])
                        t = Table(window)
                elif s == "Author Name":
                    detail = detail_entry.get()
                    a="select Reference_Book_No, Reference_Book_Name, Publication, Author_Name, Subject from reference where Author_Name='{}' and Availability=1".format(detail)
                    cursor.execute(a)
                    data=cursor.fetchall()
                    if data == []:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Error!")
                        error_label = Label(window, text = "No Reference Book available with this Author", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(filter_widgets), _filter()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                    else:
                        window = Tk()
                        window.title("Author")
                        lst = l + data
                        total_rows = len(lst)
                        total_columns = len(lst[0])
                        t = Table(window)
                elif s == "Genre/Subject":
                    detail = detail_entry.get()
                    a="select Reference_Book_No, Reference_Book_Name, Publication, Author_Name, Subject from reference where Subject='{}' and Availability=1".format(Genre)
                    cursor.execute(a)
                    data=cursor.fetchall()
                    if data == []:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Error!")
                        error_label = Label(window, text = "No Reference Book available with this Genre", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(filter_widgets), _filter()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                    else:
                        window = Tk()
                        window.title("Genre")
                        lst = l + data
                        total_rows = len(lst)
                        total_columns = len(lst[0])
                        t = Table(window)

def get_date():
    global date
    date = date_entry.get()

def home():
    global choice_label, teacher_button, student_button, admin_button, home_widgets
    
    remove(date_widgets)

    lib_label = Label(root, text = "WELCOME TO THE LIBRARY", font = ("Times New Roman", 17))
    lib_label.place(x = 500, y = 75, anchor = CENTER)
    
    choice_label = Label(root, text = "Are you a/the : ", font = ("Times New Roman", 14))
    choice_label.place(x = 500, y = 200, anchor = CENTER)

    teacher_button = Button(root, text = "Teacher", height = 2, width = 10, font = ("Times New Roman", 12), command = teacher_login)
    teacher_button.place(x = 333, y = 275, anchor = CENTER)

    student_button = Button(root, text = "Student", height = 2, width = 10, font = ("Times New Roman", 12), command = student_login)
    student_button.place(x = 500, y = 275, anchor = CENTER)

    admin_button = Button(root, text = "Admin", height = 2, width = 10, font = ("Times New Roman", 12), command = admin)
    admin_button.place(x = 666, y = 275, anchor = CENTER)

    home_widgets = [choice_label, teacher_button, student_button, admin_button, lib_label]
    
def admin():
    global back_button, admin_label, admin_choice_label, add_book_button, remove_book_button, edit_book_button, list_book_button, delete_user_button, admin_widgets
    remove(home_widgets)
    
    admin_label = Label(root, text = "ADMIN", font = ("Times New Roman", 20))
    admin_label.place(x = 500, y = 75, anchor = CENTER)
    
    admin_choice_label = Label(root, text = "Do you wish to : ", font = ("Times New Roman", 17))
    admin_choice_label.place(x = 500, y = 150, anchor = CENTER)
    
    add_book_button = Button(root, text = "Add Books", height = 2, width = 17, font = ("Times New Roman", 12), command = lambda:[admin_add(), back_button.destroy()])
    add_book_button.place(x = 100, y = 275, anchor = CENTER)
    
    remove_book_button = Button(root, text = "Remove Books", height = 2, width = 17, font = ("Times New Roman", 12), command = lambda:[admin_remove(), back_button.destroy()])
    remove_book_button.place(x = 300, y = 275, anchor = CENTER)
    
    edit_book_button = Button(root, text = "Edit Books", height = 2, width = 17, font = ("Times New Roman", 12), command = lambda:[admin_edit(), back_button.destroy()])
    edit_book_button.place(x = 500, y = 275, anchor = CENTER)
    
    list_book_button = Button(root, text = "List all Borrowed Books", height = 2, width = 17, font = ("Times New Roman", 12), command = lambda:[admin_list(), back_button.destroy()])
    list_book_button.place(x = 700, y = 275, anchor = CENTER)
    
    delete_user_button = Button(root, text = "Delete Users", height = 2, width = 17, font = ("Times New Roman", 12), command = lambda:[admin_delete_user(), back_button.destroy()])
    delete_user_button.place(x = 900, y = 275, anchor = CENTER)

    admin_widgets = [add_book_button, remove_book_button, edit_book_button, list_book_button, delete_user_button, lib_label, admin_choice_label]

    back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(admin_widgets), home(), back_button.destroy(), admin_label.destroy()])
    back_button.place(x = 50, y = 50, anchor = CENTER) 

def admin_add():
    global add_book_choice_label, novel_button, reference_book_button, admin_add_widgets, add_book_details_label, book_number_label, book_number_entry, book_name_label, book_name_entry, book_publication_label, book_publication_entry, book_author_label, book_author_entry, book_genre_label, book_genre_entry, book_price_label, book_price_entry, book_add_button, v
    remove(admin_widgets)

    v = IntVar()
        
    add_book_choice_label = Label(root, text = "Do you wish to add : ", font = ("Times New Roman", 17))
    add_book_choice_label.place(x = 250, y = 150, anchor = CENTER)
    
    novel_button = Radiobutton(root, text = "Novel", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 1)
    novel_button.place(x = 250, y = 225, anchor = CENTER)
    
    reference_book_button = Radiobutton(root, text = "Reference Book", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 2)
    reference_book_button.place(x = 250, y = 275, anchor = CENTER)

    add_book_details_label = Label(root, text = "Enter the details of the book : ", font = ("Times New Roman", 17))
    add_book_details_label.place(x = 675, y = 150, anchor = CENTER)
    
    book_number_label = Label(root, text = "Book Number : ", font = ("Times New Roman", 14))
    book_number_label.place(x = 675, y = 200, anchor = E)
    
    book_number_entry = Entry(root, width = 40)
    book_number_entry.place(x = 675, y=200, anchor = W)
    
    book_name_label = Label(root, text = "Book Name : ", font = ("Times New Roman", 14))
    book_name_label.place(x = 675, y = 225, anchor = E)
    
    book_name_entry = Entry(root, width = 40)
    book_name_entry.place(x = 675, y=225, anchor = W)
    
    book_publication_label = Label(root, text = "Name of the Publication : ", font = ("Times New Roman", 14))
    book_publication_label.place(x = 675, y = 250, anchor = E)
    
    book_publication_entry = Entry(root, width = 40)
    book_publication_entry.place(x = 675, y=250, anchor = W)
    
    book_author_label = Label(root, text = "Name of the Author : ", font = ("Times New Roman", 14))
    book_author_label.place(x = 675, y = 275, anchor = E)
    
    book_author_entry = Entry(root, width = 40)
    book_author_entry.place(x = 675, y=275, anchor = W)
    
    book_genre_label = Label(root, text = "Genre/Subject of the Book : ", font = ("Times New Roman", 14))
    book_genre_label.place(x = 675, y = 300, anchor = E)
    
    book_genre_entry = Entry(root, width = 40)
    book_genre_entry.place(x = 675, y=300, anchor = W)
    
    book_price_label = Label(root, text = "Price of the Book : ", font = ("Times New Roman", 14))
    book_price_label.place(x = 675, y = 325, anchor = E)
    
    book_price_entry = Entry(root, width = 40)
    book_price_entry.place(x = 675, y=325, anchor = W)
    
    book_add_button = Button(root, text = "Confirm Book Details", height = 1, width = 20, font = ("Times New Roman", 12), command = lambda:[confirm_book(), back_button.destroy()])
    book_add_button.place(x = 500, y = 425, anchor = CENTER)

    admin_add_widgets = [add_book_choice_label, novel_button, reference_book_button, add_book_details_label, book_number_label, book_number_entry, book_name_label, book_name_entry, book_publication_label, book_publication_entry, book_author_label, book_author_entry, book_genre_label, book_genre_entry, book_price_label, book_price_entry, book_add_button]

    back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(admin_add_widgets), admin(), back_button.destroy()])
    back_button.place(x = 50, y = 50, anchor = CENTER)  

def confirm_book():
    r = v.get()
    book_num = int(book_number_entry.get())
    book_name = book_name_entry.get()
    publication = book_publication_entry.get()
    author_name = book_author_entry.get()
    genre = book_genre_entry.get()
    price = float(book_price_entry.get())
    l=[book_num,book_name,publication,author_name,genre,price]
    if r==0:
        window = Toplevel(root)
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Please Select an option", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_add_widgets), admin_add()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        if r == 1:
            cursor.execute('select novel_no from novels')
            data=cursor.fetchall()
            novels=[]
            for i in data:
                novels.append(i[0])
            if book_num not in novels:
                x="insert into novels values(%s,%s,%s,%s,%s,%s,True)"
                cursor.execute(x,l)
                mycon.commit()
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Success")
                error_label = Label(window, text = "The Novel has been added", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_add_widgets), admin_add()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                
                error_label = Label(window, text = "The Novel Number already exists ", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_add_widgets), admin_add()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
        elif r==2:
            cursor.execute('select reference_book_no from reference')
            data=cursor.fetchall()
            reference=[]
            for i in data:
                reference.append(i[0])
            if book_num not in reference:
                x="insert into reference values(%s,%s,%s,%s,%s,%s,True)"
                cursor.execute(x,l)
                mycon.commit()
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Success")
                error_label = Label(window, text = "The Reference Book has been added", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_add_widgets), admin_add()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                
                error_label = Label(window, text = "The Reference Book Number already exists ", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_add_widgets), admin_add()])
                error_button.place(x = 150, y = 100, anchor = CENTER)

def admin_remove():
    global remove_book_choice_label, admin_remove_widgets, novel_button, reference_book_button, remove_book_no_label, remove_book_no_entry, remove_book_button, v
    remove(admin_widgets)

    v = IntVar()
        
    remove_book_choice_label = Label(root, text = "Do you wish to remove : ", font = ("Times New Roman", 17))
    remove_book_choice_label.place(x = 500, y = 150, anchor = CENTER)
    
    novel_button = Radiobutton(root, text = "Novel", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 1)
    novel_button.place(x = 250, y = 225, anchor = CENTER)
    
    reference_book_button = Radiobutton(root, text = "Reference Book", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 2)
    reference_book_button.place(x = 750, y = 225, anchor = CENTER)

    remove_book_no_label = Label(root, text = "Enter the number of the book you wish to remove : ", font = ("Times New Roman", 15))
    remove_book_no_label.place(x = 500, y = 300, anchor = CENTER)

    remove_book_no_entry = Entry(root, width = 40)
    remove_book_no_entry.place(x = 500, y = 350, anchor = CENTER)

    remove_book_button = Button(root, text = "Confirm Book Details", height = 1, width = 20, font = ("Times New Roman", 12), command = lambda:[remove_book(), back_button.destroy()])
    remove_book_button.place(x = 500, y = 425, anchor = CENTER)

    admin_remove_widgets = [remove_book_choice_label, novel_button, reference_book_button, remove_book_no_label, remove_book_no_entry, remove_book_button]

    back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(admin_remove_widgets), admin(), back_button.destroy()])
    back_button.place(x = 50, y = 50, anchor = CENTER)

def remove_book():
    r = v.get()
    book_no = int(remove_book_no_entry.get())
    if r==0:
        window = Toplevel(root)
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Please Select an option", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_remove_widgets), admin_remove()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        if r == 1:
            cursor.execute('select novel_no from novels where availability=1')
            data=cursor.fetchall()
            novel_avail=[]
            for i in data:
                novel_avail.append(i[0])
            cursor.execute('select novel_no from novels')
            data=cursor.fetchall()
            novel=[]
            for i in data:
                novel.append(i[0])
            if (book_no not in novel_avail) and (book_no in novel):
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                
                error_label = Label(window, text = '''The Novel has been borrowed.
Wait for it to be returned to remove it.''', font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)

                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_remove_widgets), admin_remove()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            elif book_no not in novel:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                
                error_label = Label(window, text = "The Novel Number doesnt exist. ", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_remove_widgets), admin_remove()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                a='delete from novels where novel_no={}'.format(book_no)
                cursor.execute(a)
                mycon.commit()
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Success")
                error_label = Label(window, text = "The Novel has been removed", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_remove_widgets), admin_remove()])
                error_button.place(x = 150, y = 100, anchor = CENTER)

        elif r == 2:
            cursor.execute('select reference_book_no from reference where availability=1')
            data=cursor.fetchall()
            reference_avail=[]
            for i in data:
                reference_avail.append(i[0])
            cursor.execute('select reference_book_no from reference')
            data=cursor.fetchall()
            reference=[]
            for i in data:
                reference.append(i[0])
            if (book_no not in reference_avail) and (book_no in reference):
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                
                error_label = Label(window, text = '''The Reference Book has been borrowed.
Wait for it to be returned to remove it.''', font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)

                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_remove_widgets), admin_remove()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            elif book_no not in reference:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                
                error_label = Label(window, text = "The Reference Book Number doesnt exist. ", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_remove_widgets), admin_remove()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                a='delete from reference where reference_book_no={}'.format(book_no)
                cursor.execute(a)
                mycon.commit()
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Success")
                error_label = Label(window, text = "The Reference Book has been removed", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_remove_widgets), admin_remove()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
    
def admin_edit():
    global edit_book_choice_label, novel_button, reference_book_button, edit_book_no_label, edit_book_no_entry, edit_choice_label, edit_choice_menu, edit_choice_entry, confirm_edit_button, admin_edit_widgets, v, o
    remove(admin_widgets)

    v = IntVar()
    o = StringVar()
    o.set("Detail to Edit : ")
        
    edit_book_choice_label = Label(root, text = "Do you wish to edit : ", font = ("Times New Roman", 17))
    edit_book_choice_label.place(x = 500, y = 150, anchor = CENTER)
    
    novel_button = Radiobutton(root, text = "Novel", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 1)
    novel_button.place(x = 250, y = 200, anchor = CENTER)
    
    reference_book_button = Radiobutton(root, text = "Reference Book", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 2)
    reference_book_button.place(x = 750, y = 200, anchor = CENTER)

    edit_book_no_label = Label(root, text = "Enter the Book Number : ", font = ("Times New Roman", 14))
    edit_book_no_label.place(x = 500, y = 250, anchor = E)

    edit_book_no_entry = Entry(root, width = 40)
    edit_book_no_entry.place(x = 500, y = 250, anchor = W)

    edit_choice_label = Label(root, text = "Which detail do you wish to edit : ", font = ("Times New Roman", 14))
    edit_choice_label.place(x = 500, y = 300, anchor = CENTER)

    edit_choice_menu = OptionMenu(root, o, "Book Name", "Publication", "Author Name", "Genre/Subject", "Price")
    edit_choice_menu.place(x = 475, y = 350, anchor = E)
    edit_choice_menu.config(width =25)

    edit_choice_entry = Entry(root, width = 40)
    edit_choice_entry.place(x = 500, y = 350, anchor = W)

    confirm_edit_button = Button(root, text = "EDIT", height = 1, width = 20, font = ("Times New Roman", 12), command = lambda:[edit_book(), back_button.destroy(), ])
    confirm_edit_button.place(x = 500, y = 425, anchor = CENTER)


    admin_edit_widgets = [edit_book_choice_label, novel_button, reference_book_button, edit_book_no_label, edit_book_no_entry, edit_choice_label, edit_choice_menu, edit_choice_entry, confirm_edit_button]

    back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(admin_edit_widgets), admin(), back_button.destroy()])
    back_button.place(x = 50, y = 50, anchor = CENTER)

def edit_book():
    r = v.get()
    s = o.get()
    book_no = int(edit_book_no_entry.get())

    if r == 0 or s == "Detail to Edit : ":
        window = Toplevel(root)
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Please Select an option", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_edit_widgets), admin_edit()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
        
    else:
        if r == 1:
            cursor.execute('select novel_no from novels')
            data=cursor.fetchall()
            novel=[]
            for i in data:
                novel.append(i[0])
            if book_no in novel:
                if s == "Book Name":
                    detail = edit_choice_entry.get()
                    a='update novels set Novel_Name="{}" where novel_no={}'.format(detail,book_no)
                    cursor.execute(a)
                    mycon.commit()
                    
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success")
                    
                    error_label = Label(window, text = "The Novel Name has been edited", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_edit_widgets), admin_edit()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                    
                elif s == "Publication":
                    detail = edit_choice_entry.get()
                    a='update novels set Publication="{}" where novel_no={}'.format(detail,book_no)
                    cursor.execute(a)
                    mycon.commit()

                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success")
                    
                    error_label = Label(window, text = "The Publication has been edited", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_edit_widgets), admin_edit()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                    
                elif s == "Author Name":
                    detail = edit_choice_entry.get()
                    a='update novels set Author_name="{}" where novel_no={}'.format(detail,book_no)
                    cursor.execute(a)
                    mycon.commit()

                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success")
                    
                    error_label = Label(window, text = "The Author's Name has been edited", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_edit_widgets), admin_edit()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                    
                elif s == "Genre/Subject":
                    detail = edit_choice_entry.get()
                    a='update novels set Genre="{}" where novel_no={}'.format(detail,book_no)
                    cursor.execute(a)
                    mycon.commit()

                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success")
                    
                    error_label = Label(window, text = "The Genre has been edited", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_edit_widgets), admin_edit()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                    
                elif s == "Price":
                    detail = float(edit_choice_entry.get())
                    a='update novels set Price={} where novel_no={}'.format(detail,book_no)
                    cursor.execute(a)
                    mycon.commit()

                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success")
                    
                    error_label = Label(window, text = "The Price has been edited", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_edit_widgets), admin_edit()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                    
            else:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "Novel Number does not exist", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_edit_widgets), admin_edit()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
                
        elif r == 2:
            cursor.execute('select reference_book_no from reference')
            data=cursor.fetchall()
            reference=[]
            for i in data:
                reference.append(i[0])
            if book_no in reference:
                if s == "Book Name":
                    detail = edit_choice_entry.get()
                    a='update reference set Reference_Book_Name="{}" where reference_book_no={}'.format(detail,book_no)
                    cursor.execute(a)
                    mycon.commit()
                    
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success")
                    
                    error_label = Label(window, text = "The Reference Book Name has been edited", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_edit_widgets), admin_edit()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                    
                elif s == "Publication":
                    detail = edit_choice_entry.get()
                    a='update reference set Publication="{}" where reference_book_no={}'.format(detail,book_no)
                    cursor.execute(a)
                    mycon.commit()

                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success")
                    
                    error_label = Label(window, text = "The Publication has been edited", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_edit_widgets), admin_edit()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                    
                elif s == "Author Name":
                    detail = edit_choice_entry.get()
                    a='update reference set Author_Name="{}" where reference_book_no={}'.format(detail,book_no)
                    cursor.execute(a)
                    mycon.commit()

                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success")
                    
                    error_label = Label(window, text = "The Author's Name has been edited", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_edit_widgets), admin_edit()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                    
                elif s == "Genre/Subject":
                    detail = edit_choice_entry.get()
                    a='update reference set Genre="{}" where reference_book_no={}'.format(detail,book_no)
                    cursor.execute(a)
                    mycon.commit()

                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success")
                    
                    error_label = Label(window, text = "The Subject has been edited", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_edit_widgets), admin_edit()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                    
                elif s == "Price":
                    detail = float(edit_choice_entry.get())
                    a='update reference set Price={} where reference_book_no={}'.format(detail,book_no)
                    cursor.execute(a)
                    mycon.commit()

                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success")
                    
                    error_label = Label(window, text = "The Price has been edited", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_edit_widgets), admin_edit()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                    
            else:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "Reference Book Number does not exist", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_edit_widgets), admin_edit()])
                error_button.place(x = 150, y = 100, anchor = CENTER)

def admin_list():
    global list_label, list_student_novel_button, list_student_reference_button, list_teacher_novel_button, list_teacher_reference_button, list_button, v, admin_list_widgets
    remove(admin_widgets)

    v = IntVar()
    
    list_label = Label(root, text = "What do you wish to see : ", font = ("Times New Roman", 14))
    list_label.place(x = 500, y = 150, anchor = CENTER)

    list_student_novel_button = Radiobutton(root, text = "Student Novels", height = 2, width = 18, font = ("Times New Roman", 12), variable = v, value = 1)
    list_student_novel_button.place(x = 125, y = 250, anchor = CENTER)

    list_student_reference_button = Radiobutton(root, text = "Student Reference Books", height = 2, width = 18, font = ("Times New Roman", 12), variable = v, value = 2)
    list_student_reference_button.place(x = 375, y = 250, anchor = CENTER)

    list_teacher_novel_button = Radiobutton(root, text = "Teacher Novels", height = 2, width = 18, font = ("Times New Roman", 12), variable = v, value = 3)
    list_teacher_novel_button.place(x = 575, y = 250, anchor = CENTER)

    list_teacher_reference_button = Radiobutton(root, text = "Teacher Reference Books", height = 2, width = 18, font = ("Times New Roman", 12), variable = v, value = 4)
    list_teacher_reference_button.place(x = 775, y = 250, anchor = CENTER)

    list_button = Button(root, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[list_borrowed(), back_button.destroy()])
    list_button.place(x = 500, y = 350, anchor = CENTER)

    admin_list_widgets = [list_label, list_student_novel_button, list_student_reference_button, list_teacher_novel_button, list_teacher_reference_button, list_button]

    back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(admin_list_widgets), admin(), back_button.destroy()])
    back_button.place(x = 50, y = 50, anchor = CENTER)

def list_borrowed():
    global lst, total_rows, total_columns
    r = v.get()
    if r == 0:
        window = Toplevel(root)
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Please Select an option", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(choose_reference_edit_widgets), choose_reference_edit()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        if r == 1:
            cursor.execute('select novels.novel_no,novel_name,student_id,student_name,class,section from novels,students where novels.novel_no=students.novel_no')
            student_novel=cursor.fetchall()
            if student_novel == []:
                window = Tk()
                window.geometry("300x150")
                window.title("Error")
                error_label = Label(window, text = "Students have not borrowed any Novels", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_list_widgets), admin_list()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                lst = [("Novel Number", "Novel Name", "Student ID", "Student Name", "Class", "Section")]+student_novel
                window = Tk()
                window.title("Student Novels")
                total_rows = len(lst)
                total_columns = len(lst[0])
                t = Table(window)
                back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(admin_list_widgets), admin(), back_button.destroy()])
                back_button.place(x = 50, y = 50, anchor = CENTER)
        elif r == 2:
            cursor.execute('select reference.reference_book_no,reference_book_name,subject,student_id,student_name,class,section from reference,students where students.reference_book_no=reference.reference_book_no')
            student_reference=cursor.fetchall()
            if student_reference == []:
                window = Tk()
                window.geometry("300x150")
                window.title("Error")
                error_label = Label(window, text = "Students have not borrowed any Reference Books", font = ("Times New Roman", 11))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_list_widgets), admin_list()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                lst = [("Reference Book Number", "Reference Book Name", "Student ID", "Student Name", "Class", "Section")]+student_reference
                window = Tk()
                window.title("Student Reference")
                total_rows = len(lst)
                total_columns = len(lst[0])
                t = Table(window)
                back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(admin_list_widgets), admin(), back_button.destroy()])
                back_button.place(x = 50, y = 50, anchor = CENTER)
        elif r == 3:
            cursor.execute('select novels.novel_no,novel_name,teacher_id,teacher_name from teacher,novels where teacher.novel_no=novels.novel_no')
            teacher_novel=cursor.fetchall()
            if teacher_novel == []:
                window = Tk()
                window.geometry("300x150")
                window.title("Error")
                error_label = Label(window, text = "Teachers have not borrowed any Novels", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_list_widgets), admin_list()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                lst = [("Novel Number", "Novel Name", "Teacher ID", "Teacher Name")]+teacher_novel
                window = Tk()
                window.title("Teacher Novels")
                total_rows = len(lst)
                total_columns = len(lst[0])
                t = Table(window)
                back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(admin_list_widgets), admin(), back_button.destroy()])
                back_button.place(x = 50, y = 50, anchor = CENTER)
        elif r == 4:
            cursor.execute('select reference_book_no,reference_book_name,teacher_id,teacher_name from teacher,reference where reference_book_no in (reference_book_no_1,reference_book_no_2,reference_book_no_3)')
            teacher_reference=cursor.fetchall()
            if teacher_reference == []:
                window = Tk()
                window.geometry("300x150")
                window.title("Error")
                error_label = Label(window, text = "Teachers have not borrowed any Reference Books", font = ("Times New Roman", 11))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_list_widgets), admin_list()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                lst = [("Reference Book Number", "Reference Book Name", "Teacher ID", "Teacher Name")]+teacher_reference
                window = Tk()
                window.title("Teacher Reference Books")
                total_rows = len(lst)
                total_columns = len(lst[0])
                t = Table(window)
                back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(admin_list_widgets), admin(), back_button.destroy()])
                back_button.place(x = 50, y = 50, anchor = CENTER)

def admin_delete_user():
    global delete_user_choice_label, delete_student_button, delete_teacher_button, admin_delete_user_widgets, v, ID_entry, ID_entry_label, ID_button
    remove(admin_widgets)

    v = IntVar()
        
    delete_user_choice_label = Label(root, text = "Do you wish to delete : ", font = ("Times New Roman", 17))
    delete_user_choice_label.place(x = 500, y = 150, anchor = CENTER)
    
    delete_student_button = Radiobutton(root, text = "Student", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 2)
    delete_student_button.place(x = 250, y = 225, anchor = CENTER)
    
    delete_teacher_button = Radiobutton(root, text = "Teacher", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 1)
    delete_teacher_button.place(x = 750, y = 225, anchor = CENTER)

    ID_entry = Entry(root, width = 40)
    ID_entry.place(x = 500, y = 275, anchor = W)

    ID_entry_label = Label(root, text = "Enter the ID number : ", font = ("Times New Roman", 17))
    ID_entry_label.place(x = 500, y = 275, anchor = E)

    ID_button = Button(root, text = "Delete", height = 2, width = 10, font = ("Times New Roman", 12), command = lambda:[check_delete(), back_button.destroy()])
    ID_button.place(x = 500, y = 350, anchor = CENTER)

    admin_delete_user_widgets = [delete_user_choice_label, delete_student_button, delete_teacher_button, ID_entry, ID_entry_label, ID_button]

    back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(admin_delete_user_widgets), admin(), back_button.destroy()])
    back_button.place(x = 50, y = 50, anchor = CENTER)

def check_delete():
    r = v.get()
    ID_No = int(ID_entry.get())
    if r == 0:
        window = Toplevel(root)
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Please Select an option", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_delete_user_widgets), admin_delete_user()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        if r == 1:
            cursor.execute('select Teacher_ID from teacher')
            data=cursor.fetchall()
            teacher=[]
            for i in data:
                teacher.append(i[0])
            if ID_No not in teacher:
                window = Tk()
                window.geometry("300x150")
                window.title("Error")
                error_label = Label(window, text = "ID does not exist", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_delete_user_widgets), admin_delete_user()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                cursor.execute('select novel_no,reference_book_no_1,reference_book_no_2,reference_book_no_3 from teacher where teacher_ID={}'.format(ID_No))
                borrowed_books=cursor.fetchall()
                if borrowed_books==[(None,None,None,None)]:
                    cursor.execute('delete from teacher where teacher_ID={}'.format(ID_No))
                    mycon.commit()
                    window = Tk()
                    window.geometry("300x150")
                    window.title("Success")
                    error_label = Label(window, text = "User has been removed.", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_delete_user_widgets), admin_delete_user()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                else:
                    window = Tk()
                    window.geometry("300x150")
                    window.title("Error")
                    error_label = Label(window, text = '''User has borrowed books.
    Wait for them to return it to delete the account.''', font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_delete_user_widgets), admin_delete_user()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
        elif r==2:
            cursor.execute('select Student_ID,Student_Name from students')
            data=cursor.fetchall()
            student=[]
            for i in data:
                student.append(i[0])
            if ID_No not in student:
                window = Tk()
                window.geometry("300x150")
                window.title("Error")
                error_label = Label(window, text = "ID does not exist", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_delete_user_widgets), admin_delete_user()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                cursor.execute('select novel_no,reference_book_no from students where student_ID={}'.format(ID_No))
                borrowed_books=cursor.fetchall()
                if borrowed_books==[(None,None)]:
                    cursor.execute('delete from students where student_ID={}'.format(ID_No))
                    mycon.commit()
                    window = Tk()
                    window.geometry("300x150")
                    window.title("Success")
                    error_label = Label(window, text = "User has been removed.", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_delete_user_widgets), admin_delete_user()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                else:
                    window = Tk()
                    window.geometry("300x150")
                    window.title("Error")
                    error_label = Label(window, text = '''User has borrowed books.
    Wait for them to return it to delete the account.''', font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(admin_delete_user_widgets), admin_delete_user()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)

def student_login():
    remove(home_widgets)

    global student_label, student_login_label, student_login_label, student_id_entry, student_pwd_label, student_pwd_entry, student_login_button, student_signup_button, student_login_widgets, student_id_label
    
    student_label = Label(root, text = "STUDENT", font = ("Times New Roman", 20))
    student_label.place(x = 500, y = 75, anchor = CENTER)

    student_login_label = Label(root, text = "Login", font = ("Times New Roman", 17))
    student_login_label.place(x = 500, y = 150, anchor = CENTER)

    student_id_label = Label(root, text = "Enter ID Number : ", font = ("Times New Roman", 14))
    student_id_label.place(x = 500, y = 200, anchor = E)

    student_id_entry = Entry(root, width = 40)
    student_id_entry.place(x = 500, y = 200, anchor = W)

    student_pwd_label = Label(root, text = "Enter the Password : ", font = ("Times New Roman", 14))
    student_pwd_label.place(x = 500, y = 225, anchor = E)

    student_pwd_entry = Entry(root, width = 40, show = "*")
    student_pwd_entry.place(x = 500, y = 225, anchor = W)

    student_login_button = Button(root, text = "Login", height = 1, width = 15, font = ("Times New Roman", 14), command = lambda:[get_student_no(), student(), back_button.destroy()])
    student_login_button.place(x = 500, y = 275, anchor = CENTER)

    student_signup_button = Button(root, text = "Sign Up", height = 1, width = 15, font = ("Times New Roman", 14), command = lambda:[student_signup(), back_button.destroy()])
    student_signup_button.place(x = 700, y = 325, anchor = CENTER)

    student_login_widgets = [student_login_label, student_id_entry, student_pwd_label, student_pwd_entry, student_login_button, student_signup_button, student_id_label]

    back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(student_login_widgets), home(), back_button.destroy(), student_label.destroy()])
    back_button.place(x = 50, y = 50, anchor = CENTER)

def get_student_no():
    global student_no, student_password
    student_no = int(student_id_entry.get())
    student_password = student_pwd_entry.get()

def student_signup():
    remove(student_login_widgets)

    global student_sec_entry, student_sec_label,  student_class_entry, student_class_label, student_name_entry, student_name_label, student_signup_pwd_entry, student_signup_pwd_label, student_signup_id_label, student_signup_id_entry, student_signup_label, student_signup_widgets

    student_signup_label = Label(root, text = "Sign Up", font = ("Times New Roman", 17))
    student_signup_label.place(x = 500, y = 150, anchor = CENTER)

    student_signup_id_label = Label(root, text = "Enter ID Number : ", font = ("Times New Roman", 14))
    student_signup_id_label.place(x = 500, y = 200, anchor = E)

    student_signup_id_entry = Entry(root, width = 40)
    student_signup_id_entry.place(x = 500, y = 200, anchor = W)

    student_signup_pwd_label = Label(root, text = "Enter the Password : ", font = ("Times New Roman", 14))
    student_signup_pwd_label.place(x = 500, y = 225, anchor = E)

    student_signup_pwd_entry = Entry(root, width = 40, show = "*")
    student_signup_pwd_entry.place(x = 500, y = 225, anchor = W)

    student_name_label = Label(root, text = "Enter Student Name : ", font = ("Times New Roman", 14))
    student_name_label.place(x = 500, y = 250, anchor = E)

    student_name_entry = Entry(root, width = 40)
    student_name_entry.place(x = 500, y = 250, anchor = W)

    student_class_label = Label(root, text = "Enter Class : ", font = ("Times New Roman", 14))
    student_class_label.place(x = 500, y = 275, anchor = E)

    student_class_entry = Entry(root, width = 40)
    student_class_entry.place(x = 500, y = 275, anchor = W)

    student_sec_label = Label(root, text = "Enter Section : ", font = ("Times New Roman", 14))
    student_sec_label.place(x = 500, y = 300, anchor = E)

    student_sec_entry = Entry(root, width = 40)
    student_sec_entry.place(x = 500, y = 300, anchor = W)

    student_signup_button = Button(root, text = "Sign Up", height = 1, width = 15, font = ("Times New Roman", 14), command = lambda:[student_signup_confirm(), back_button.destroy()])
    student_signup_button.place(x = 500, y = 350, anchor = CENTER)

    student_signup_widgets = [student_sec_entry, student_sec_label,  student_class_entry, student_class_label, student_name_entry, student_name_label, student_signup_pwd_entry, student_signup_pwd_label, student_signup_id_label, student_signup_id_entry, student_signup_label, student_signup_button]

    back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(student_signup_widgets), student_login(), back_button.destroy()])
    back_button.place(x = 50, y = 50, anchor = CENTER)

def student_signup_confirm():
    cursor.execute('select Student_ID from Students')
    data=cursor.fetchall()
    student=[]
    for i in data:
        student.append(i[0])
    student_no = int(student_signup_id_entry.get())
    if student_no in student:
        window = Tk()
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Student ID already exists", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_signup_widgets), student_login()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        student_password = student_signup_pwd_entry.get()
        student_name = student_name_entry.get()
        _class = student_class_entry.get()
        section = student_sec_entry.get()
        a='insert into students(student_ID,student_password,student_name,class,section) values({},"{}","{}",{},"{}")'.format(student_no,student_password,student_name,_class,section)
        cursor.execute(a)
        mycon.commit()
        window = Tk()
        window.geometry("300x150")
        window.title("Success")
        error_label = Label(window, text = "Successfully Signed Up", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_signup_widgets), student_login()])
        error_button.place(x = 150, y = 100, anchor = CENTER)

def student():
    global a
    a = 1
    cursor.execute('select Student_ID from Students')
    data=cursor.fetchall()
    student=[]
    for i in data:
        student.append(i[0])
    cursor.execute('select student_Password from students where student_ID={}'.format(student_no))
    password_student=cursor.fetchall()

    if student_no not in student:
        window = Tk()
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "You have not signed up yet", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_login_widgets), student_signup()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    elif (student_no in student) and (student_password != password_student[0][0]):
        window = Tk()
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Incorrect Password", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_login_widgets), student_login()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        remove(student_login_widgets)

        global student_choice_label, student_borrow_button, student_return_button, student_view_button, student_extend_button, student_check_button, student_widgets

        student_choice_label = Label(root, text = "Do you wish to : ", font = ("Times New Roman", 17))
        student_choice_label.place(x = 500, y = 150, anchor = CENTER)
        
        student_borrow_button = Button(root, text = "Borrow Books", height = 2, width = 17, font = ("Times New Roman", 12), command = lambda:[student_borrow(), back_button.destroy()])
        student_borrow_button.place(x = 100, y = 275, anchor = CENTER)

        student_return_button = Button(root, text = "Return Books", height = 2, width = 17, font = ("Times New Roman", 12), command = lambda:[student_return(), back_button.destroy()])
        student_return_button.place(x = 300, y = 275, anchor = CENTER)
        
        student_view_button = Button(root, text = "View Borrowed Books", height = 2, width = 17, font = ("Times New Roman", 12), command = lambda:[student_view()])
        student_view_button.place(x = 500, y = 275, anchor = CENTER)
        
        student_extend_button = Button(root, text = "Extend Borrowed Books", height = 2, width = 17, font = ("Times New Roman", 12), command = lambda:[student_extend(), back_button.destroy()])
        student_extend_button.place(x = 700, y = 275, anchor = CENTER)
        
        student_check_button = Button(root, text = "List Available Books", height = 2, width = 17, font = ("Times New Roman", 12), command = lambda:[_filter(), back_button.destroy(), remove(student_widgets)])
        student_check_button.place(x = 900, y = 275, anchor = CENTER)

        student_widgets = [student_choice_label, student_borrow_button, student_return_button, student_view_button, student_extend_button, student_check_button]

        back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(student_widgets), home(), back_button.destroy(), student_label.destroy()])
        back_button.place(x = 50, y = 50, anchor = CENTER)

def student_borrow():
    cursor.execute('select novel_no from novels')
    data=cursor.fetchall()
    novel=[]
    for i in data:
        novel.append(i[0])
    cursor.execute('select reference_book_no from reference')
    data=cursor.fetchall()
    reference=[]
    for i in data:
        reference.append(i[0])

    cursor.execute('select Novel_no,Reference_Book_No from students where Student_ID={}'.format(student_no))
    borrowed_books=cursor.fetchall()

    if novel == [] and reference == []:
        window = Tk()
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "No Books available", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_widgets), student()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    elif borrowed_books[0][0] != None and borrowed_books[0][1] != None:
        window = Tk()
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = '''You have already borrowed 2 books.
Please Return them to borrow more.''', font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_widgets), student()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        global student_borrow_choice_label, student_borrow_novel_button, student_borrow_reference_button, book_no_entry, book_no_entry_label, student_borrow_button, v, student_borrow_widgets
        remove(student_widgets)

        v = IntVar()
            
        student_borrow_choice_label = Label(root, text = "Do you wish to borrow : ", font = ("Times New Roman", 17))
        student_borrow_choice_label.place(x = 500, y = 150, anchor = CENTER)
        
        student_borrow_novel_button = Radiobutton(root, text = "Novel", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 1)
        student_borrow_novel_button.place(x = 250, y = 225, anchor = CENTER)
        
        student_borrow_reference_button = Radiobutton(root, text = "Reference Book", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 2)
        student_borrow_reference_button.place(x = 750, y = 225, anchor = CENTER)

        book_no_entry = Entry(root, width = 40)
        book_no_entry.place(x = 500, y = 275, anchor = W)

        book_no_entry_label = Label(root, text = "Enter the Book Number : ", font = ("Times New Roman", 17))
        book_no_entry_label.place(x = 500, y = 275, anchor = E)

        student_borrow_button = Button(root, text = "Borrow", height = 2, width = 10, font = ("Times New Roman", 12), command = lambda:[check_student_borrow(), back_button.destroy()])
        student_borrow_button.place(x = 500, y = 350, anchor = CENTER)

        student_borrow_widgets = [student_borrow_choice_label, student_borrow_novel_button, student_borrow_reference_button, book_no_entry, book_no_entry_label, student_borrow_button]

        back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(student_borrow_widgets), student(), back_button.destroy()])
        back_button.place(x = 50, y = 50, anchor = CENTER)

def check_student_borrow():
    r = v.get()
    if r == 0:
        window = Toplevel(root)
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Please Select an option", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_borrow_widgets), student_borrow()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        cursor.execute('select Novel_no,Reference_Book_No from students where Student_ID={}'.format(student_no))
        borrowed_books=cursor.fetchall()
        cursor.execute('select Novel_No from Novels where Availability=1')
        data=cursor.fetchall()
        availability_novels=[]
        for i in data:
            availability_novels.append(i[0])
        cursor.execute('select Reference_Book_No from Reference where Availability=1')
        data=cursor.fetchall()
        availability_reference=[]
        for i in data:
            availability_reference.append(i[0])
        cursor.execute('select novel_no from novels')
        data=cursor.fetchall()
        novel=[]
        for i in data:
            novel.append(i[0])
        cursor.execute('select reference_book_no from reference')
        data=cursor.fetchall()
        reference=[]
        for i in data:
            reference.append(i[0])
        book_no = int(book_no_entry.get())
        if r == 1:
            if borrowed_books[0][0]!=None:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "You have already borrowed a Novel", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_borrow_widgets), student_borrow()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                if book_no not in novel:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error!")
                    error_label = Label(window, text = "Novel Number doesn't exist", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_borrow_widgets), student_borrow()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                elif (book_no in novel) and (book_no not in availability_novels):
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error!")
                    error_label = Label(window, text = "Novel is not available", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_borrow_widgets), student_borrow()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                else:
                    a='update Students set Novel_No={},Novel_Date="{}" where student_ID={}'.format(book_no,date,student_no)
                    cursor.execute(a)
                    mycon.commit()
                    a1='update Novels set Availability=False where Novel_No={}'.format(book_no)
                    cursor.execute(a1)
                    mycon.commit()
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success!")
                    error_label = Label(window, text = "Novel has been borrowed", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_borrow_widgets), student_borrow()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
        elif r == 2:
            if borrowed_books[0][1]!=None:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "You have already borrowed a Reference Book", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_borrow_widgets), student_borrow()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                if book_no not in reference:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error!")
                    error_label = Label(window, text = "Reference Book Number doesn't exist", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_borrow_widgets), student_borrow()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                elif (book_no in reference) and (book_no not in availability_reference):
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error!")
                    error_label = Label(window, text = "Reference Book is not available", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_borrow_widgets), student_borrow()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                else:
                    a='update students set Reference_Book_No={},Reference_Book_Date="{}" where student_ID={}'.format(book_no,date,student_no)
                    cursor.execute(a)
                    mycon.commit()
                    a1='update Reference set Availability=False where Reference_Book_No={}'.format(book_no)
                    cursor.execute(a1)
                    mycon.commit()
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success!")
                    error_label = Label(window, text = "Reference Book has been borrowed", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_borrow_widgets), student_borrow()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)

def student_return():
    cursor.execute('select Novel_no,Reference_Book_No from students where Student_ID={}'.format(student_no))
    borrowed_books=cursor.fetchall()

    if borrowed_books[0][0] == None and borrowed_books[0][1] == None:
        window = Tk()
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = '''You have not borrowed any books''', font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_widgets), student()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        global student_return_choice_label, student_return_novel_button, student_return_reference_button, book_no_entry, book_no_entry_label, student_return_button, v, student_return_widgets
        remove(student_widgets)

        v = IntVar()
            
        student_return_choice_label = Label(root, text = "Do you wish to borrow : ", font = ("Times New Roman", 17))
        student_return_choice_label.place(x = 500, y = 150, anchor = CENTER)
        
        student_return_novel_button = Radiobutton(root, text = "Novel", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 1)
        student_return_novel_button.place(x = 250, y = 225, anchor = CENTER)
        
        student_return_reference_button = Radiobutton(root, text = "Reference Book", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 2)
        student_return_reference_button.place(x = 750, y = 225, anchor = CENTER)

        book_no_entry = Entry(root, width = 40)
        book_no_entry.place(x = 500, y = 275, anchor = W)

        book_no_entry_label = Label(root, text = "Enter the Book Number : ", font = ("Times New Roman", 17))
        book_no_entry_label.place(x = 500, y = 275, anchor = E)

        student_return_button = Button(root, text = "Return", height = 2, width = 10, font = ("Times New Roman", 12), command = lambda:[check_student_return(), back_button.destroy()])
        student_return_button.place(x = 500, y = 350, anchor = CENTER)

        student_return_widgets = [student_return_choice_label, student_return_novel_button, student_return_reference_button, book_no_entry, book_no_entry_label, student_return_button]

        back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(student_return_widgets), student(), back_button.destroy()])
        back_button.place(x = 50, y = 50, anchor = CENTER)

def check_student_return():
    r = v.get()
    if r == 0:
        window = Toplevel(root)
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Please Select an option", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_return_widgets), student_return()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        cursor.execute('select novel_no from novels')
        data=cursor.fetchall()
        novel=[]
        for i in data:
            novel.append(i[0])
        cursor.execute('select reference_book_no from reference')
        data=cursor.fetchall()
        reference=[]
        for i in data:
            reference.append(i[0])
        book_no = int(book_no_entry.get())
        cursor.execute('select Novel_no,Reference_Book_No from students where Student_ID={}'.format(student_no))
        borrowed_books=cursor.fetchall()
        if r == 1:
            if borrowed_books[0][0]==None:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "You have not borrowed a Novel", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_return_widgets), student_return()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                if book_no not in novel:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error!")
                    error_label = Label(window, text = "Novel Number doesn't exist", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_return_widgets), student_return()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                elif book_no == borrowed_books[0][0]:
                    a1='select datediff("{}",Novel_Date) from Students where student_ID={}'.format(date,student_no)
                    cursor.execute(a1)
                    date_difference=cursor.fetchall()
                    d = IntVar()
                    d.set(date_difference)
                    a='update students set Novel_No=NULL,Novel_date=NULL where student_ID={}'.format(student_no)
                    cursor.execute(a)
                    mycon.commit()
                    a2='update Novels set Availability=True where novel_no={}'.format(book_no)
                    cursor.execute(a2)
                    mycon.commit()
                    if date_difference[0][0]>15:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success!")
                        error_label1 = Label(window, text = "Fine Amount", font = ("Times New Roman", 12))
                        error_label1.place(x = 150, y = 25, anchor = CENTER)
                        
                        error_label2 = Label(window, textvariable = d, font = ("Times New Roman", 12))
                        error_label2.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_label3 = Label(window, text = "Please Pay the amount at the desk", font = ("Times New Roman", 12))
                        error_label3.place(x = 150, y = 75, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_return_widgets), student_return()])
                        error_button.place(x = 150, y = 125, anchor = CENTER)
                    else:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success")
                        error_label = Label(window, text = "Novel has been returned", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_return_widgets), student_return()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                else:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error")
                    error_label = Label(window, text = "You have not borrowed this Novel", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_return_widgets), student_return()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                    
        elif r == 2:
            if borrowed_books[0][1]==None:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "You have not borrowed a Reference Book", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_return_widgets), student_return()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                if book_no not in reference:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error!")
                    error_label = Label(window, text = "Reference Book Number doesn't exist", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_return_widgets), student_return()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                elif book_no == borrowed_books[0][1]:
                    a1='select datediff("{}",Reference_Book_Date) from students where student_ID={}'.format(date,student_no)
                    cursor.execute(a1)
                    date_difference=cursor.fetchall()
                    d = IntVar()
                    d.set(date_difference)
                    a='update students set Reference_Book_No=NULL,Reference_Book_Date=NULL where Student_ID={}'.format(student_no)
                    cursor.execute(a)
                    mycon.commit()
                    a2='update Reference set Availability=True where reference_book_no={}'.format(book_no)
                    cursor.execute(a2)
                    mycon.commit()
                    if date_difference[0][0]>15:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success!")
                        error_label1 = Label(window, text = "Fine Amount", font = ("Times New Roman", 12))
                        error_label1.place(x = 150, y = 25, anchor = CENTER)
                        
                        error_label2 = Label(window, textvariable = d, font = ("Times New Roman", 12))
                        error_label2.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_label3 = Label(window, text = "Please Pay the amount at the desk", font = ("Times New Roman", 12))
                        error_label3.place(x = 150, y = 75, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_return_widgets), student_return()])
                        error_button.place(x = 150, y = 125, anchor = CENTER)
                    else:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success")
                        error_label = Label(window, text = "Reference Book has been returned", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_return_widgets), student_return()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                else:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error")
                    error_label = Label(window, text = "You have not borrowed this Reference Book", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_return_widgets), student_return()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)

def student_view():
    global total_rows, total_columns, lst
    cursor.execute('select Novel_no,Reference_Book_No from students where student_ID={}'.format(student_no))
    borrowed_books=cursor.fetchall()
    
    if borrowed_books[0][0] == None and borrowed_books[0][1] == None:
        window = Toplevel(root)
        window.geometry("300x150")
        window.title("Success")
        error_label = Label(window, text = "You have not borrowed any books", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_widgets), student()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        cursor.execute('select novels.novel_no,novel_name,novel_date from students,novels where novels.novel_no=students.novel_no and student_ID={}'.format(student_no))
        borrowed_novel=cursor.fetchall()

        cursor.execute('select reference.reference_book_no,reference_book_name,reference_book_date from students,reference where students.reference_book_no=reference.reference_book_no and student_ID={}'.format(student_no))
        borrowed_reference=cursor.fetchall()

        novel = [("Novel Number", "Novel Name", "Date Borrowed")]
        reference = [("Reference Book Number", "Reference Book Name", "Date Borrowed")]
        if borrowed_novel == []:
            lst = reference + borrowed_reference
        elif borrowed_reference == []:
            lst = novel + borrowed_novel
        else:
            lst = novel + borrowed_novel + reference + borrowed_reference
        window = Tk()
        window.title("Borrowed Books")
        total_rows = len(lst)
        total_columns = len(lst[0])
        t = Table(window) 

def student_extend():
    cursor.execute('select Novel_no,Reference_Book_No from students where Student_ID={}'.format(student_no))
    borrowed_books=cursor.fetchall()

    if borrowed_books[0][0] == None and borrowed_books[0][1] == None:
        window = Tk()
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = '''You have not borrowed any books''', font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_widgets), student()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        global student_extend_choice_label, student_extend_novel_button, student_extend_reference_button, book_no_entry, book_no_entry_label, student_extend_button, v, student_extend_widgets
        remove(student_widgets)

        v = IntVar()
            
        student_extend_choice_label = Label(root, text = "Do you wish to extend the return date of : ", font = ("Times New Roman", 17))
        student_extend_choice_label.place(x = 500, y = 150, anchor = CENTER)
        
        student_extend_novel_button = Radiobutton(root, text = "Novel", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 1)
        student_extend_novel_button.place(x = 250, y = 225, anchor = CENTER)
        
        student_extend_reference_button = Radiobutton(root, text = "Reference Book", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 2)
        student_extend_reference_button.place(x = 750, y = 225, anchor = CENTER)

        book_no_entry = Entry(root, width = 40)
        book_no_entry.place(x = 500, y = 275, anchor = W)

        book_no_entry_label = Label(root, text = "Enter the Book Number : ", font = ("Times New Roman", 17))
        book_no_entry_label.place(x = 500, y = 275, anchor = E)

        student_extend_button = Button(root, text = "Return", height = 2, width = 10, font = ("Times New Roman", 12), command = lambda:[check_student_extend(), back_button.destroy()])
        student_extend_button.place(x = 500, y = 350, anchor = CENTER)

        student_extend_widgets = [student_extend_choice_label, student_extend_novel_button, student_extend_reference_button, book_no_entry, book_no_entry_label, student_extend_button]

        back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(student_extend_widgets), student(), back_button.destroy()])
        back_button.place(x = 50, y = 50, anchor = CENTER)

def check_student_extend():
    r = v.get()
    if r == 0:
        window = Toplevel(root)
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Please Select an option", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_extend_widgets), student_extend()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        cursor.execute('select novel_no from novels')
        data=cursor.fetchall()
        novel=[]
        for i in data:
            novel.append(i[0])
        cursor.execute('select reference_book_no from reference')
        data=cursor.fetchall()
        reference=[]
        for i in data:
            reference.append(i[0])
        book_no = int(book_no_entry.get())
        cursor.execute('select Novel_no,Reference_Book_No from students where Student_ID={}'.format(student_no))
        borrowed_books=cursor.fetchall()
        if r == 1:
            if borrowed_books[0][0]==None:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "You have not borrowed a Novel", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_extend_widgets), student_extend()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            elif book_no == borrowed_books[0][0]:
                a1='select datediff("{}",Novel_Date) from students where student_ID={}'.format(date,student_no)
                cursor.execute(a1)
                date_difference=cursor.fetchall()
                d = IntVar()
                d.set(date_difference)
                if date_difference[0][0]>15:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success!")
                    error_label1 = Label(window, text = "You have exceeded the time to return the book.", font = ("Times New Roman", 12))
                    error_label1.place(x = 150, y = 25, anchor = CENTER)
                    
                    error_label2 = Label(window, textvariable = d, font = ("Times New Roman", 12))
                    error_label2.place(x = 150, y = 75, anchor = CENTER)
                    
                    error_label3 = Label(window, text = "Please Pay the below amount at the desk", font = ("Times New Roman", 12))
                    error_label3.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_extend_widgets), student_extend()])
                    error_button.place(x = 150, y = 125, anchor = CENTER)
                else:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success")
                    error_label = Label(window, text = "Time to return the book has been extended", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_extend_widgets), student_extend()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                a='update students set Novel_Date="{}" where student_ID={}'.format(date,student_no)
                cursor.execute(a)
                mycon.commit()
            else:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error")
                error_label = Label(window, text = "You have not borrowed this Novel", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_extend_widgets), student_extend()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
        elif r == 2:
            if borrowed_books[0][1]==None:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "You have not borrowed a Reference Book", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_extend_widgets), student_extend()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                if book_no not in reference:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error!")
                    error_label = Label(window, text = "Reference Book Number doesn't exist", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_extend_widgets), student_extend()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                elif book_no == borrowed_books[0][1]:
                    a1='select datediff("{}",Reference_Book_Date) from students where student_ID={}'.format(date,student_no)
                    cursor.execute(a1)
                    date_difference=cursor.fetchall()
                    d = IntVar()
                    d.set(date_difference)
                    if date_difference[0][0]>15:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success!")
                        error_label1 = Label(window, text = "You have exceeded the time to return the book.", font = ("Times New Roman", 12))
                        error_label1.place(x = 150, y = 25, anchor = CENTER)
                        
                        error_label2 = Label(window, textvariable = d, font = ("Times New Roman", 12))
                        error_label2.place(x = 150, y = 75, anchor = CENTER)
                        
                        error_label3 = Label(window, text = "Please Pay the below amount at the desk", font = ("Times New Roman", 12))
                        error_label3.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_extend_widgets), student_extend()])
                        error_button.place(x = 150, y = 125, anchor = CENTER)
                    else:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success")
                        error_label = Label(window, text = "Time to return the book has been extended", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_extend_widgets), student_extend()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                    a='update students set Reference_Book_Date="{}" where student_ID={}'.format(date,student_no)
                    cursor.execute(a)
                    mycon.commit()
                else:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error")
                    error_label = Label(window, text = "You have not borrowed this Reference Book", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_extend_widgets), student_extend()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)

def teacher_login():
    remove(home_widgets)

    global teacher_label, teacher_login_label, teacher_id_label, teacher_id_entry, teacher_pwd_label, teacher_pwd_entry, teacher_login_button, teacher_signup_button, teacher_login_widgets
    
    teacher_label = Label(root, text = "TEACHER", font = ("Times New Roman", 20))
    teacher_label.place(x = 500, y = 75, anchor = CENTER)

    teacher_login_label = Label(root, text = "Login", font = ("Times New Roman", 17))
    teacher_login_label.place(x = 500, y = 150, anchor = CENTER)

    teacher_id_label = Label(root, text = "Enter ID Number : ", font = ("Times New Roman", 14))
    teacher_id_label.place(x = 500, y = 200, anchor = E)

    teacher_id_entry = Entry(root, width = 40)
    teacher_id_entry.place(x = 500, y = 200, anchor = W)

    teacher_pwd_label = Label(root, text = "Enter the Password : ", font = ("Times New Roman", 14))
    teacher_pwd_label.place(x = 500, y = 225, anchor = E)

    teacher_pwd_entry = Entry(root, width = 40, show = "*")
    teacher_pwd_entry.place(x = 500, y = 225, anchor = W)

    teacher_login_button = Button(root, text = "Login", height = 1, width = 15, font = ("Times New Roman", 14), command = lambda:[get_teacher_no(), teacher(), back_button.destroy()])
    teacher_login_button.place(x = 500, y = 275, anchor = CENTER)

    teacher_signup_button = Button(root, text = "Sign Up", height = 1, width = 15, font = ("Times New Roman", 14), command = lambda:[teacher_signup(), back_button.destroy()])
    teacher_signup_button.place(x = 700, y = 325, anchor = CENTER)

    teacher_login_widgets = [teacher_login_label, teacher_id_label, teacher_id_entry, teacher_pwd_label, teacher_pwd_entry, teacher_login_button, teacher_signup_button]

    back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(teacher_login_widgets), home(), back_button.destroy(), teacher_label.destroy()])
    back_button.place(x = 50, y = 50, anchor = CENTER)

def get_teacher_no():
    global teacher_no, teacher_password
    teacher_no = int(teacher_id_entry.get())
    teacher_password = teacher_pwd_entry.get()

def teacher_signup():
    remove(teacher_login_widgets)

    global teacher_name_entry, teacher_name_label, teacher_signup_pwd_entry, teacher_signup_pwd_label, teacher_signup_id_label, teacher_signup_id_entry, teacher_signup_label, teacher_signup_widgets

    teacher_signup_label = Label(root, text = "Sign Up", font = ("Times New Roman", 17))
    teacher_signup_label.place(x = 500, y = 150, anchor = CENTER)

    teacher_signup_id_label = Label(root, text = "Enter ID Number : ", font = ("Times New Roman", 14))
    teacher_signup_id_label.place(x = 500, y = 225, anchor = E)

    teacher_signup_id_entry = Entry(root, width = 40)
    teacher_signup_id_entry.place(x = 500, y = 225, anchor = W)

    teacher_signup_pwd_label = Label(root, text = "Enter the Password : ", font = ("Times New Roman", 14))
    teacher_signup_pwd_label.place(x = 500, y = 250, anchor = E)

    teacher_signup_pwd_entry = Entry(root, width = 40, show = "*")
    teacher_signup_pwd_entry.place(x = 500, y = 250, anchor = W)

    teacher_name_label = Label(root, text = "Enter Teacher Name : ", font = ("Times New Roman", 14))
    teacher_name_label.place(x = 500, y = 275, anchor = E)

    teacher_name_entry = Entry(root, width = 40)
    teacher_name_entry.place(x = 500, y = 275, anchor = W)

    teacher_signup_button = Button(root, text = "Sign Up", height = 1, width = 15, font = ("Times New Roman", 14), command = lambda:[teacher_signup_confirm(), back_button.destroy()])
    teacher_signup_button.place(x = 500, y = 350, anchor = CENTER)

    teacher_signup_widgets = [teacher_name_entry, teacher_name_label, teacher_signup_pwd_entry, teacher_signup_pwd_label, teacher_signup_id_label, teacher_signup_id_entry, teacher_signup_label, teacher_signup_button]

    back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(teacher_signup_widgets), teacher_login(), back_button.destroy()])
    back_button.place(x = 50, y = 50, anchor = CENTER)

def teacher_signup_confirm():
    cursor.execute('select Teacher_ID from Teacher')
    data=cursor.fetchall()
    teacher=[]
    for i in data:
        teacher.append(i[0])
    teacher_no = int(teacher_signup_id_entry.get())
    if teacher_no in teacher:
        window = Tk()
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Teacher ID already exists", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_signup_widgets), teacher_login()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        teacher_password =teacher_signup_pwd_entry.get()
        teacher_name=teacher_name_entry.get()
        a='insert into teacher(teacher_ID,teacher_password,teacher_name) values({},"{}","{}")'.format(teacher_no,teacher_password,teacher_name)
        cursor.execute(a)
        mycon.commit()
        window = Tk()
        window.geometry("300x150")
        window.title("Success")
        error_label = Label(window, text = "Successfully Signed Up", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_signup_widgets), teacher_login()])
        error_button.place(x = 150, y = 100, anchor = CENTER)

def teacher():
    global a
    a = 2
    cursor.execute('select Teacher_ID from Teacher')
    data=cursor.fetchall()
    teacher=[]
    for i in data:
        teacher.append(i[0])
    cursor.execute('select Teacher_Password from teacher where teacher_ID={}'.format(teacher_no))
    password_teacher=cursor.fetchall()

    if teacher_no not in teacher:
        window = Tk()
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "You have not signed up yet", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_login_widgets), teacher_signup()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    elif (teacher_no in teacher) and (teacher_password != password_teacher[0][0]):
        window = Tk()
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Incorrect Password", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_login_widgets), teacher_login()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        remove(teacher_login_widgets)

        global teacher_choice_label, teacher_borrow_button, teacher_return_button, teacher_view_button, teacher_extend_button, teacher_check_button, teacher_widgets

        teacher_choice_label = Label(root, text = "Do you wish to : ", font = ("Times New Roman", 17))
        teacher_choice_label.place(x = 500, y = 150, anchor = CENTER)
        
        teacher_borrow_button = Button(root, text = "Borrow Books", height = 2, width = 17, font = ("Times New Roman", 12), command = lambda:[teacher_borrow(), back_button.destroy()])
        teacher_borrow_button.place(x = 100, y = 275, anchor = CENTER)

        teacher_return_button = Button(root, text = "Return Books", height = 2, width = 17, font = ("Times New Roman", 12), command = lambda:[teacher_return(), back_button.destroy()])
        teacher_return_button.place(x = 300, y = 275, anchor = CENTER)
        
        teacher_view_button = Button(root, text = "View Borrowed Books", height = 2, width = 17, font = ("Times New Roman", 12), command = lambda:[teacher_view()])
        teacher_view_button.place(x = 500, y = 275, anchor = CENTER)
        
        teacher_extend_button = Button(root, text = "Extend Borrowed Books", height = 2, width = 17, font = ("Times New Roman", 12), command = lambda:[teacher_extend(), back_button.destroy()])
        teacher_extend_button.place(x = 700, y = 275, anchor = CENTER)
        
        teacher_check_button = Button(root, text = "List Available Books", height = 2, width = 17, font = ("Times New Roman", 12), command = lambda:[_filter(), back_button.destroy(), remove(teacher_widgets)])
        teacher_check_button.place(x = 900, y = 275, anchor = CENTER)

        teacher_widgets = [teacher_choice_label, teacher_borrow_button, teacher_return_button, teacher_view_button, teacher_extend_button, teacher_check_button]

        back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(teacher_widgets), home(), back_button.destroy(), teacher_label.destroy()])
        back_button.place(x = 50, y = 50, anchor = CENTER)

def teacher_borrow():
    cursor.execute('select novel_no from novels')
    data=cursor.fetchall()
    novel=[]
    for i in data:
        novel.append(i[0])
    cursor.execute('select reference_book_no from reference')
    data=cursor.fetchall()
    reference=[]
    for i in data:
        reference.append(i[0])

    cursor.execute('select Novel_no,Reference_Book_No_1,Reference_Book_No_2,Reference_Book_No_3 from Teacher where Teacher_ID={}'.format(teacher_no))
    borrowed_books=cursor.fetchall()

    if novel == [] and reference == []:
        window = Tk()
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "No Books available", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_widgets), teacher()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    elif borrowed_books[0][0]!=None and borrowed_books[0][1]!=None and borrowed_books[0][2]!=None and borrowed_books[0][3]!=None:
        window = Tk()
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = '''You have already borrowed 4 books.
Please Return them to borrow more.''', font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_widgets), teacher()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        global teacher_borrow_choice_label, teacher_borrow_novel_button, teacher_borrow_reference_button, book_no_entry, book_no_entry_label, teacher_borrow_button, v, teacher_borrow_widgets
        remove(teacher_widgets)

        v = IntVar()
            
        teacher_borrow_choice_label = Label(root, text = "Do you wish to borrow : ", font = ("Times New Roman", 17))
        teacher_borrow_choice_label.place(x = 500, y = 150, anchor = CENTER)
        
        teacher_borrow_novel_button = Radiobutton(root, text = "Novel", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 1)
        teacher_borrow_novel_button.place(x = 250, y = 225, anchor = CENTER)
        
        teacher_borrow_reference_button = Radiobutton(root, text = "Reference Book", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 2)
        teacher_borrow_reference_button.place(x = 750, y = 225, anchor = CENTER)

        book_no_entry = Entry(root, width = 40)
        book_no_entry.place(x = 500, y = 275, anchor = W)

        book_no_entry_label = Label(root, text = "Enter the Book Number : ", font = ("Times New Roman", 17))
        book_no_entry_label.place(x = 500, y = 275, anchor = E)

        teacher_borrow_button = Button(root, text = "Borrow", height = 2, width = 10, font = ("Times New Roman", 12), command = lambda:[check_teacher_borrow(), back_button.destroy()])
        teacher_borrow_button.place(x = 500, y = 350, anchor = CENTER)

        teacher_borrow_widgets = [teacher_borrow_choice_label, teacher_borrow_novel_button, teacher_borrow_reference_button, book_no_entry, book_no_entry_label, teacher_borrow_button]

        back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(teacher_borrow_widgets), teacher(), back_button.destroy()])
        back_button.place(x = 50, y = 50, anchor = CENTER)

def check_teacher_borrow():
    r = v.get()
    if r == 0:
        window = Toplevel(root)
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Please Select an option", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_borrow_widgets), teacher_borrow()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        cursor.execute('select Novel_no,Reference_Book_No_1,Reference_Book_No_2,Reference_Book_No_3 from Teacher where Teacher_ID={}'.format(teacher_no))
        borrowed_books=cursor.fetchall()
        cursor.execute('select Novel_No from Novels where Availability=1')
        data=cursor.fetchall()
        availability_novels=[]
        for i in data:
            availability_novels.append(i[0])
        cursor.execute('select Reference_Book_No from Reference where Availability=1')
        data=cursor.fetchall()
        availability_reference=[]
        for i in data:
            availability_reference.append(i[0])
        cursor.execute('select novel_no from novels')
        data=cursor.fetchall()
        novel=[]
        for i in data:
            novel.append(i[0])
        cursor.execute('select reference_book_no from reference')
        data=cursor.fetchall()
        reference=[]
        for i in data:
            reference.append(i[0])
        book_no = int(book_no_entry.get())
        if r == 1:
            if borrowed_books[0][0]!=None:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "You have already borrowed a Novel", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_borrow_widgets), teacher_borrow()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                if book_no not in novel:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error!")
                    error_label = Label(window, text = "Novel Number doesn't exist", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_borrow_widgets), teacher_borrow()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                elif (book_no in novel) and (book_no not in availability_novels):
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error!")
                    error_label = Label(window, text = "Novel is not available", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_borrow_widgets), teacher_borrow()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                else:
                    a='update Teacher set Novel_No={},Novel_Date="{}" where teacher_ID={}'.format(book_no,date,teacher_no)
                    cursor.execute(a)
                    mycon.commit()
                    a1='update Novels set Availability=False where Novel_No={}'.format(book_no)
                    cursor.execute(a1)
                    mycon.commit()
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success!")
                    error_label = Label(window, text = "Novel has been borrowed", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_borrow_widgets), teacher_borrow()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
        elif r == 2:
            if borrowed_books[0][1]!=None and borrowed_books[0][2]!=None and borrowed_books[0][3]!=None:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "You have already borrowed three Reference Books", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_borrow_widgets), teacher_borrow()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                if book_no not in reference:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error!")
                    error_label = Label(window, text = "Reference Book Number doesn't exist", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_borrow_widgets), teacher_borrow()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                elif (book_no in reference) and (book_no not in availability_reference):
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error!")
                    error_label = Label(window, text = "Reference Book is not available", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_borrow_widgets), teacher_borrow()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                else:
                    if borrowed_books[0][1]==None:
                        a='update Teacher set Reference_Book_No_1={},Reference_Book_No_1_Date="{}" where teacher_ID={}'.format(book_no,date,teacher_no)
                        cursor.execute(a)
                        mycon.commit()
                        a1='update Reference set Availability=False where Reference_Book_No={}'.format(book_no)
                        cursor.execute(a1)
                        mycon.commit()
                    elif borrowed_books[0][2]==None:
                        a='update Teacher set Reference_Book_No_2={},Reference_Book_No_2_Date="{}" where teacher_ID={}'.format(book_no,date,teacher_no)
                        cursor.execute(a)
                        mycon.commit()
                        a1='update Reference set Availability=False where Reference_Book_No={}'.format(book_no)
                        cursor.execute(a1)
                        mycon.commit()
                    elif borrowed_books[0][3]==None:
                        a='update Teacher set Reference_Book_No_3={},Reference_Book_No_3_Date="{}" where teacher_ID={}'.format(book_no,date,teacher_no)
                        cursor.execute(a)
                        mycon.commit()
                        a1='update Reference set Availability=False where Reference_Book_No={}'.format(book_no)
                        cursor.execute(a1)
                        mycon.commit()
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success!")
                    error_label = Label(window, text = "Reference Book has been borrowed", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_borrow_widgets), teacher_borrow()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)

def teacher_return():
    cursor.execute('select Novel_no,Reference_Book_No_1,Reference_Book_No_2,Reference_Book_No_3 from Teacher where Teacher_ID={}'.format(teacher_no))
    borrowed_books=cursor.fetchall()

    if borrowed_books[0][0] == None and borrowed_books[0][1] == None and borrowed_books[0][2] == None and borrowed_books[0][3] == None:
        window = Tk()
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = '''You have not borrowed any books''', font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_widgets), student()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        global teacher_return_choice_label, teacher_return_novel_button, teacher_return_reference_button, book_no_entry, book_no_entry_label, teacher_return_button, v, teacher_return_widgets
        remove(teacher_widgets)

        v = IntVar()
            
        teacher_return_choice_label = Label(root, text = "Do you wish to borrow : ", font = ("Times New Roman", 17))
        teacher_return_choice_label.place(x = 500, y = 150, anchor = CENTER)
        
        teacher_return_novel_button = Radiobutton(root, text = "Novel", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 1)
        teacher_return_novel_button.place(x = 250, y = 225, anchor = CENTER)
        
        teacher_return_reference_button = Radiobutton(root, text = "Reference Book", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 2)
        teacher_return_reference_button.place(x = 750, y = 225, anchor = CENTER)

        book_no_entry = Entry(root, width = 40)
        book_no_entry.place(x = 500, y = 275, anchor = W)

        book_no_entry_label = Label(root, text = "Enter the Book Number : ", font = ("Times New Roman", 17))
        book_no_entry_label.place(x = 500, y = 275, anchor = E)

        teacher_return_button = Button(root, text = "Return", height = 2, width = 10, font = ("Times New Roman", 12), command = lambda:[check_teacher_return(), back_button.destroy()])
        teacher_return_button.place(x = 500, y = 350, anchor = CENTER)

        teacher_return_widgets = [teacher_return_choice_label, teacher_return_novel_button, teacher_return_reference_button, book_no_entry, book_no_entry_label, teacher_return_button]

        back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(teacher_return_widgets), teacher(), back_button.destroy()])
        back_button.place(x = 50, y = 50, anchor = CENTER)

def check_teacher_return():
    r = v.get()
    if r == 0:
        window = Toplevel(root)
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Please Select an option", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_return_widgets), teacher_return()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        cursor.execute('select novel_no from novels')
        data=cursor.fetchall()
        novel=[]
        for i in data:
            novel.append(i[0])
        cursor.execute('select reference_book_no from reference')
        data=cursor.fetchall()
        reference=[]
        for i in data:
            reference.append(i[0])
        book_no = int(book_no_entry.get())
        cursor.execute('select Novel_no,Reference_Book_No_1,Reference_Book_No_2,Reference_Book_No_3 from Teacher where Teacher_ID={}'.format(teacher_no))
        borrowed_books=cursor.fetchall()
        if r == 1:
            if borrowed_books[0][0]==None:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "You have not borrowed a Novel", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_return_widgets), teacher_return()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                if book_no not in novel:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error!")
                    error_label = Label(window, text = "Novel Number doesn't exist", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_return_widgets), teacher_return()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                elif book_no == borrowed_books[0][0]:
                    a1='select datediff("{}",Novel_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                    cursor.execute(a1)
                    date_difference=cursor.fetchall()
                    a='update teacher set Novel_No=NULL,Novel_date=NULL where Teacher_ID={}'.format(teacher_no)
                    cursor.execute(a)
                    mycon.commit()
                    a2='update Novels set Availability=True where novel_no={}'.format(book_no)
                    cursor.execute(a2)
                    mycon.commit()
                    d = IntVar()
                    d.set(date_difference)
                    if date_difference[0][0]>30:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success!")
                        error_label1 = Label(window, text = "Fine Amount", font = ("Times New Roman", 12))
                        error_label1.place(x = 150, y = 25, anchor = CENTER)
                        
                        error_label2 = Label(window, textvariable = d, font = ("Times New Roman", 12))
                        error_label2.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_label3 = Label(window, text = "Please Pay the amount at the desk", font = ("Times New Roman", 12))
                        error_label3.place(x = 150, y = 75, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_return_widgets), teacher_return()])
                        error_button.place(x = 150, y = 125, anchor = CENTER)
                    else:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success")
                        error_label = Label(window, text = "Novel has been returned", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_return_widgets), teacher_return()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                else:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error")
                    error_label = Label(window, text = "You have not borrowed this Novel", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_return_widgets), teacher_return()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                    
        elif r == 2:
            if borrowed_books[0][1]==None:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "You have not borrowed a Reference Book", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_return_widgets), teacher_return()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                if book_no not in reference:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error!")
                    error_label = Label(window, text = "Reference Book Number doesn't exist", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_return_widgets), teacher_return()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                elif book_no == borrowed_books[0][1]:
                    a1='select datediff("{}",Reference_Book_No_1_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                    cursor.execute(a1)
                    date_difference=cursor.fetchall()
                    a='update teacher set Reference_Book_No_1=NULL,Reference_Book_No_1_Date=NULL where Teacher_ID={}'.format(teacher_no)
                    cursor.execute(a)
                    mycon.commit()
                    a2='update Reference set Availability=True where reference_book_no={}'.format(book_no)
                    cursor.execute(a2)
                    mycon.commit()
                    d = IntVar()
                    d.set(date_difference)
                    if date_difference[0][0]>30:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success!")
                        error_label1 = Label(window, text = "Fine Amount", font = ("Times New Roman", 12))
                        error_label1.place(x = 150, y = 25, anchor = CENTER)
                        
                        error_label2 = Label(window, textvariable = d, font = ("Times New Roman", 12))
                        error_label2.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_label3 = Label(window, text = "Please Pay the amount at the desk", font = ("Times New Roman", 12))
                        error_label3.place(x = 150, y = 75, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_return_widgets), teacher_return()])
                        error_button.place(x = 150, y = 125, anchor = CENTER)
                    else:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success")
                        error_label = Label(window, text = "Reference Book has been returned", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_return_widgets), teacher_return()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                elif book_no == borrowed_books[0][2]:
                    a1='select datediff("{}",Reference_Book_No_2_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                    cursor.execute(a1)
                    date_difference=cursor.fetchall()
                    a='update teacher set Reference_Book_No_2=NULL,Reference_Book_No_2_Date=NULL where Teacher_ID={}'.format(teacher_no)
                    cursor.execute(a)
                    mycon.commit()
                    a2='update Reference set Availability=True where reference_book_no={}'.format(book_no)
                    cursor.execute(a2)
                    mycon.commit()
                    d = IntVar()
                    d.set(date_difference)
                    if date_difference[0][0]>30:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success!")
                        error_label1 = Label(window, text = "Fine Amount", font = ("Times New Roman", 12))
                        error_label1.place(x = 150, y = 25, anchor = CENTER)
                        
                        error_label2 = Label(window, textvariable = d, font = ("Times New Roman", 12))
                        error_label2.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_label3 = Label(window, text = "Please Pay the amount at the desk", font = ("Times New Roman", 12))
                        error_label3.place(x = 150, y = 75, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_return_widgets), teacher_return()])
                        error_button.place(x = 150, y = 125, anchor = CENTER)
                    else:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success")
                        error_label = Label(window, text = "Reference Book has been returned", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_return_widgets), teacher_return()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                elif book_no == borrowed_books[0][3]:
                    a1='select datediff("{}",Reference_Book_No_3_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                    cursor.execute(a1)
                    date_difference=cursor.fetchall()
                    a='update teacher set Reference_Book_No_3=NULL,Reference_Book_No_3_Date=NULL where Teacher_ID={}'.format(teacher_no)
                    cursor.execute(a)
                    mycon.commit()
                    a2='update Reference set Availability=True where reference_book_no={}'.format(book_no)
                    cursor.execute(a2)
                    mycon.commit()
                    d = IntVar()
                    d.set(date_difference)
                    if date_difference[0][0]>30:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success!")
                        error_label1 = Label(window, text = "Fine Amount", font = ("Times New Roman", 12))
                        error_label1.place(x = 150, y = 25, anchor = CENTER)
                        
                        error_label2 = Label(window, textvariable = d, font = ("Times New Roman", 12))
                        error_label2.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_label3 = Label(window, text = "Please Pay the amount at the desk", font = ("Times New Roman", 12))
                        error_label3.place(x = 150, y = 75, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_return_widgets), teacher_return()])
                        error_button.place(x = 150, y = 125, anchor = CENTER)
                    else:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success")
                        error_label = Label(window, text = "Reference Book has been returned", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_return_widgets), teacher_return()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                else:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error")
                    error_label = Label(window, text = "You have not borrowed this Reference Book", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_return_widgets), teacher_return()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)

def teacher_view():
    global total_rows, total_columns, lst
    cursor.execute('select Novel_no,Reference_Book_No_1,Reference_Book_No_2,Reference_Book_No_3 from Teacher where Teacher_ID={}'.format(teacher_no))
    borrowed_books=cursor.fetchall()
    
    if borrowed_books[0][0] == None and borrowed_books[0][1] == None and borrowed_books[0][2] == None and borrowed_books[0][3] == None:
        window = Toplevel(root)
        window.geometry("300x150")
        window.title("Success")
        error_label = Label(window, text = "You have not borrowed any books", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_widgets), teacher()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        cursor.execute('select novels.novel_no,novel_name,novel_date from teacher,novels where novels.novel_no=teacher.novel_no and teacher_ID={}'.format(teacher_no))
        borrowed_novel=cursor.fetchall()

        cursor.execute('select reference_book_no,reference_book_name,reference_book_no_1_date from teacher,reference where teacher.reference_book_no_1=reference.reference_book_no and teacher_ID={}'.format(teacher_no))
        borrowed_reference_1=cursor.fetchall()

        cursor.execute('select reference_book_no,reference_book_name,reference_book_no_2_date from teacher,reference where teacher.reference_book_no_2=reference.reference_book_no and teacher_ID={}'.format(teacher_no))
        borrowed_reference_2=cursor.fetchall()

        cursor.execute('select reference_book_no,reference_book_name,reference_book_no_3_date from teacher,reference where teacher.reference_book_no_3=reference.reference_book_no and teacher_ID={}'.format(teacher_no))
        borrowed_reference_3=cursor.fetchall()

        borrowed_reference = borrowed_reference_1 + borrowed_reference_2 + borrowed_reference_3

        novel = [("Novel Number", "Novel Name", "Date Borrowed")]
        reference = [("Reference Book Number", "Reference Book Name", "Date Borrowed")]
        if borrowed_novel == []:
            lst = reference + borrowed_reference
        elif borrowed_reference == []:
            lst = novel + borrowed_novel
        else:
            lst = novel + borrowed_novel + reference + borrowed_reference
        window = Tk()
        window.title("Borrowed Books")
        total_rows = len(lst)
        total_columns = len(lst[0])
        t = Table(window) 

def teacher_extend():
    cursor.execute('select Novel_no,Reference_Book_No_1,Reference_Book_No_2,Reference_Book_No_3 from Teacher where Teacher_ID={}'.format(teacher_no))
    borrowed_books=cursor.fetchall()

    if borrowed_books[0][0] == None and borrowed_books[0][1] == None and borrowed_books[0][2] == None and borrowed_books[0][3] == None:
        window = Tk()
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = '''You have not borrowed any books''', font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_widgets), student()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        global teacher_extend_choice_label, teacher_extend_novel_button, teacher_extend_reference_button, book_no_entry, book_no_entry_label, teacher_extend_button, v, teacher_extend_widgets
        remove(teacher_widgets)

        v = IntVar()
            
        teacher_extend_choice_label = Label(root, text = "Do you wish to extend the return date of : ", font = ("Times New Roman", 17))
        teacher_extend_choice_label.place(x = 500, y = 150, anchor = CENTER)
        
        teacher_extend_novel_button = Radiobutton(root, text = "Novel", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 1)
        teacher_extend_novel_button.place(x = 250, y = 225, anchor = CENTER)
        
        teacher_extend_reference_button = Radiobutton(root, text = "Reference Book", height = 2, width = 20, font = ("Times New Roman", 12), variable = v, value = 2)
        teacher_extend_reference_button.place(x = 750, y = 225, anchor = CENTER)

        book_no_entry = Entry(root, width = 40)
        book_no_entry.place(x = 500, y = 275, anchor = W)

        book_no_entry_label = Label(root, text = "Enter the Book Number : ", font = ("Times New Roman", 17))
        book_no_entry_label.place(x = 500, y = 275, anchor = E)

        teacher_extend_button = Button(root, text = "Return", height = 2, width = 10, font = ("Times New Roman", 12), command = lambda:[check_teacher_extend(), back_button.destroy()])
        teacher_extend_button.place(x = 500, y = 350, anchor = CENTER)

        teacher_extend_widgets = [teacher_extend_choice_label, teacher_extend_novel_button, teacher_extend_reference_button, book_no_entry, book_no_entry_label, teacher_extend_button]

        back_button = Button(root, text = "<- Back", height = 1, width = 8, font = ("Times New Roman", 12), command = lambda:[remove(teacher_extend_widgets), teacher(), back_button.destroy()])
        back_button.place(x = 50, y = 50, anchor = CENTER)

def check_teacher_extend():
    r = v.get()
    if r == 0:
        window = Toplevel(root)
        window.geometry("300x150")
        window.title("Error!")
        error_label = Label(window, text = "Please Select an option", font = ("Times New Roman", 12))
        error_label.place(x = 150, y = 50, anchor = CENTER)
        
        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_extend_widgets), teacher_extend()])
        error_button.place(x = 150, y = 100, anchor = CENTER)
    else:
        cursor.execute('select novel_no from novels')
        data=cursor.fetchall()
        novel=[]
        for i in data:
            novel.append(i[0])
        cursor.execute('select reference_book_no from reference')
        data=cursor.fetchall()
        reference=[]
        for i in data:
            reference.append(i[0])
        book_no = int(book_no_entry.get())
        cursor.execute('select Novel_no,Reference_Book_No_1,Reference_Book_No_2,Reference_Book_No_3 from Teacher where Teacher_ID={}'.format(teacher_no))
        borrowed_books=cursor.fetchall()
        if r == 1:
            if borrowed_books[0][0]==None:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "You have not borrowed a Novel", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_extend_widgets), teacher_extend()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            elif book_no == borrowed_books[0][0]:
                a1='select datediff("{}",Novel_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                cursor.execute(a1)
                date_difference=cursor.fetchall()
                d = IntVar()
                d.set(date_difference)
                if date_difference[0][0]>30:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success!")
                    error_label1 = Label(window, text = "You have exceeded the time to return the book.", font = ("Times New Roman", 12))
                    error_label1.place(x = 150, y = 25, anchor = CENTER)
                    
                    error_label2 = Label(window, textvariable = d, font = ("Times New Roman", 12))
                    error_label2.place(x = 150, y = 75, anchor = CENTER)
                    
                    error_label3 = Label(window, text = "Please Pay the below amount at the desk", font = ("Times New Roman", 12))
                    error_label3.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_extend_widgets), teacher_extend()])
                    error_button.place(x = 150, y = 125, anchor = CENTER)
                else:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Success")
                    error_label = Label(window, text = "Time to return the book has been extended", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_extend_widgets), teacher_extend()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                a='update teacher set Novel_Date="{}" where teacher_ID={}'.format(date,teacher_no)
                cursor.execute(a)
                mycon.commit()
            else:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error")
                error_label = Label(window, text = "You have not borrowed this Novel", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_extend_widgets), teacher_extend()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
        elif r == 2:
            if borrowed_books[0][1]==None and borrowed_books[0][2]==None and borrowed_books[0][3]==None:
                window = Toplevel(root)
                window.geometry("300x150")
                window.title("Error!")
                error_label = Label(window, text = "You have not borrowed a Reference Book", font = ("Times New Roman", 12))
                error_label.place(x = 150, y = 50, anchor = CENTER)
                
                error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_extend_widgets), teacher_extend()])
                error_button.place(x = 150, y = 100, anchor = CENTER)
            else:
                if book_no not in reference:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error!")
                    error_label = Label(window, text = "Reference Book Number doesn't exist", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_extend_widgets), teacher_extend()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)
                elif book_no == borrowed_books[0][1]:
                    a1='select datediff("{}",Reference_Book_No_1_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                    cursor.execute(a1)
                    date_difference=cursor.fetchall()
                    d = IntVar()
                    d.set(date_difference)
                    if date_difference[0][0]>30:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success!")
                        error_label1 = Label(window, text = "You have exceeded the time to return the book.", font = ("Times New Roman", 12))
                        error_label1.place(x = 150, y = 25, anchor = CENTER)
                        
                        error_label2 = Label(window, textvariable = d, font = ("Times New Roman", 12))
                        error_label2.place(x = 150, y = 75, anchor = CENTER)
                        
                        error_label3 = Label(window, text = "Please Pay the below amount at the desk", font = ("Times New Roman", 12))
                        error_label3.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_extend_widgets), teacher_extend()])
                        error_button.place(x = 150, y = 125, anchor = CENTER)
                    else:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success")
                        error_label = Label(window, text = "Time to return the book has been extended", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_extend_widgets), teacher_extend()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                    a='update teacher set Reference_Book_No_1_Date="{}" where teacher_ID={}'.format(date,teacher_no)
                    cursor.execute(a)
                    mycon.commit()
                elif book_no == borrowed_books[0][2]:
                    a1='select datediff("{}",Reference_Book_No_2_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                    cursor.execute(a1)
                    date_difference=cursor.fetchall()
                    d = IntVar()
                    d.set(date_difference)
                    if date_difference[0][0]>30:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success!")
                        error_label1 = Label(window, text = "You have exceeded the time to return the book.", font = ("Times New Roman", 12))
                        error_label1.place(x = 150, y = 25, anchor = CENTER)
                        
                        error_label2 = Label(window, textvariable = d, font = ("Times New Roman", 12))
                        error_label2.place(x = 150, y = 75, anchor = CENTER)
                        
                        error_label3 = Label(window, text = "Please Pay the below amount at the desk", font = ("Times New Roman", 12))
                        error_label3.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_extend_widgets), teacher_extend()])
                        error_button.place(x = 150, y = 125, anchor = CENTER)
                    else:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success")
                        error_label = Label(window, text = "Time to return the book has been extended", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_extend_widgets), teacher_extend()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                    a='update teacher set Reference_Book_No_2_Date="{}" where teacher_ID={}'.format(date,teacher_no)
                    cursor.execute(a)
                    mycon.commit()
                elif book_no == borrowed_books[0][3]:
                    a1='select datediff("{}",Reference_Book_No_3_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                    cursor.execute(a1)
                    date_difference=cursor.fetchall()
                    d = IntVar()
                    d.set(date_difference)
                    if date_difference[0][0]>30:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success!")
                        error_label1 = Label(window, text = "You have exceeded the time to return the book.", font = ("Times New Roman", 12))
                        error_label1.place(x = 150, y = 25, anchor = CENTER)
                        
                        error_label2 = Label(window, textvariable = d, font = ("Times New Roman", 12))
                        error_label2.place(x = 150, y = 75, anchor = CENTER)
                        
                        error_label3 = Label(window, text = "Please Pay the below amount at the desk", font = ("Times New Roman", 12))
                        error_label3.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_extend_widgets), teacher_extend()])
                        error_button.place(x = 150, y = 125, anchor = CENTER)
                    else:
                        window = Toplevel(root)
                        window.geometry("300x150")
                        window.title("Success")
                        error_label = Label(window, text = "Time to return the book has been extended", font = ("Times New Roman", 12))
                        error_label.place(x = 150, y = 50, anchor = CENTER)
                        
                        error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(teacher_extend_widgets), teacher_extend()])
                        error_button.place(x = 150, y = 100, anchor = CENTER)
                    a='update teacher set Reference_Book_No_3_Date="{}" where teacher_ID={}'.format(date,teacher_no)
                    cursor.execute(a)
                    mycon.commit()
                else:
                    window = Toplevel(root)
                    window.geometry("300x150")
                    window.title("Error")
                    error_label = Label(window, text = "You have not borrowed this Reference Book", font = ("Times New Roman", 12))
                    error_label.place(x = 150, y = 50, anchor = CENTER)
                    
                    error_button = Button(window, text = "OK", height = 1, width = 15, font = ("Times New Roman", 12), command = lambda:[window.destroy(), remove(student_extend_widgets), teacher_extend()])
                    error_button.place(x = 150, y = 100, anchor = CENTER)

from tkinter import *
import mysql.connector as m
from datetime import date

today = date.today()
mycon=m.connect(host='localhost',user='root',password='123456',database='library')
cursor=mycon.cursor()

root = Tk()
root.geometry("1000x500")
root.title("Library")

global novel_add_widgets, admin_add_widgets, admin_widgets

lib_label = Label(root, text = "WELCOME TO THE LIBRARY", font = ("Times New Roman", 17))
lib_label.place(x = 500, y = 75, anchor = CENTER)

date_label = Label(root, text = "Enter the date (YYYY-MM-DD) : ", font = ("Times New Roman", 14))
date_label.place(x = 500, y = 200, anchor = E)

date_entry = Entry(root, width = 40)
date_entry.insert(END, today)
date_entry.place(x = 500, y=200, anchor = W)

date_button = Button(root, text = "Confirm Date", height = 1, width = 10, font = ("Times New Roman", 12), command = lambda:[get_date(), home()])
date_button.place(x = 800, y = 200, anchor = CENTER)

date_widgets = [date_label, date_entry, date_button, lib_label]

quit_button = Button(root, text = "QUIT", height = 2, width = 10, font = ("Times New Roman", 12), command = root.destroy)
quit_button.place(x = 900, y = 425, anchor = CENTER)

root.mainloop()
