#Function to Filter Books
def _filter():
    cursor.execute('select Novel_No from novels where availability=1')
    data=cursor.fetchall()
    novels=[]
    for i in data:
        novels.append(i[0])
    cursor.execute('select Reference_Book_No from reference where availability=1')
    data=cursor.fetchall()
    reference=[]
    for i in data:
        reference.append(i[0])
    if novels!=[] or reference!=[]:
        while True:
            f=int(input('''What do you wish to filter for?
1. Novels
2. Reference Book
3. Quit\n'''))
            if f==1:
                if novels!=[]:
                    while True:
                        f1=int(input('''What do you wish to filter by?
1. Display All
2. Book Name
3. Publication
4. Author Name
5. Genre
6. Quit\n'''))
                        if f1==2:
                            book_name=input("Enter the book name: ")
                            a="select Novel_no, Novel_Name, Publication, Author_Name, Genre from novels where Novel_Name='{}' and Availability=1".format(book_name)
                            cursor.execute(a)
                            data=cursor.fetchall()
                            if data==[]:
                                print("Book not available")
                            else:
                                for i in data:
                                    print(i)
                        elif f1==3:
                            publication=input("Enter the name of the Publication")
                            a="select Novel_no, Novel_Name, Publication, Author_Name, Genre from novels where Publication='{}' and Availability=1".format(publication)
                            cursor.execute(a)
                            data=cursor.fetchall()
                            if data==[]:
                                print("Book not available")
                            else:
                                for i in data:
                                    print(i)
                        elif f1==4:
                            author_name=input("Enter the name of the Author")
                            a="select Novel_no, Novel_Name, Publication, Author_Name, Genre from novels where Author_Name='{}' and Availability=1".format(author_name)
                            cursor.execute(a)
                            data=cursor.fetchall()
                            if data==[]:
                                print("Book not available")
                            else:
                                for i in data:
                                    print(i)
                        elif f1==5:
                            Genre=input("Which Genre of books would you like to search")
                            a="select Novel_no, Novel_Name, Publication, Author_Name, Genre from novels where Genre='{}' and Availability=1".format(Genre)
                            cursor.execute(a)
                            data=cursor.fetchall()
                            if data==[]:
                                print("Book not available")
                            else:
                                for i in data:
                                    print(i)
                        elif f1==1:
                            a="select Novel_No,Novel_name,Publication,Author_Name,Genre from novels where availability=1"
                            cursor.execute(a)
                            data=cursor.fetchall()
                            if data==[]:
                                print("No available books")
                            else:
                                for i in data:
                                    print(i)
                        elif f1==6:
                            break
                        else:
                            print("Enter Valid Number")
                            continue
                else:
                    print("There are no Novels available. Please come back later")
            elif f==2:
                if reference!=[]:
                    while True:
                        f1=int(input('''What do you wish to filter by?
1. Display All
2. Book Name
3. Publication
4. Author Name
5. Subject
6. Quit\n'''))
                        if f1==2:
                                book_name=input("Enter the book name: ")
                                a="select Reference_Book_No, Reference_Book_Name, Publication, Author_Name, Subject from reference where Reference_Book_Name='{}' and Availability=1".format(book_name)
                                cursor.execute(a)
                                data=cursor.fetchall()
                                if data==[]:
                                    print("Book not available")
                                else:
                                    for i in data:
                                        print(i)
                        elif f1==3:
                            publication=input("Enter the name of the Publication")
                            a="select Reference_Book_No, Reference_Book_Name, Publication, Author_Name, Subject from reference where Publication='{}' and Availability=1".format(publication)
                            cursor.execute(a)
                            data=cursor.fetchall()
                            if data==[]:
                                print("Book not available")
                            else:
                                for i in data:
                                        print(i)
                        elif f1==4:
                            author_name=input("Enter the name of the Author")
                            a="select Reference_Book_No, Reference_Book_Name, Publication, Author_Name, Subject from reference where Author_Name='{}' and Availability=1".format(author_name)
                            cursor.execute(a)
                            data=cursor.fetchall()
                            if data==[]:
                                print("Book not available")
                            else:
                                for i in data:
                                        print(i)
                        elif f1==5:
                            Subject=input("Which Genre of books would you like to search")
                            a="select Reference_Book_No, Reference_Book_Name, Publication, Author_Name, Subject from reference where Subject='{}' and Availability=1".format(Subject)
                            cursor.execute(a)
                            data=cursor.fetchall()
                            if data==[]:
                                print("Book not available")
                            else:
                                for i in data:
                                        print(i)
                        elif f1==1:
                            a="select Reference_Book_No, Reference_Book_Name, Publication, Author_Name, Subject from reference where Availability=1"
                            cursor.execute(a)
                            data=cursor.fetchall()
                            if data==[]:
                                print("No books available")
                            else:
                                for i in data:
                                    print(i)
                        elif f1==6:
                            break
                        else:
                            print("Enter Valid Number")
                            continue
                else:
                    print("There are no Reference Books available. Please come back later.")
            elif f==3:
                break
            else:
                print("Enter Valid Number")
                continue
    else:
        print("There are no available books. Please come back later.")
#Function to Add Books
def admin_add():
    while True:
        cursor.execute('select novel_no from novels')
        data=cursor.fetchall()
        novels=[]
        for i in data:
            novels.append(i[0])
        cursor.execute('select reference_book_no from reference')
        data=cursor.fetchall()
        reference=[]
        for i in data:
            reference.append(i[0])
        tell=int(input('''Do you wish to add
1. Novels
2. Reference Books
3. Quit\n'''))
        if tell==1:
            book_num=int(input("Enter the Book Number:"))
            if book_num not in novels:
                book_name=input("Enter the Book Name:")
                publication=input("Enter the name of the Publication:")
                author_name=input("Enter Name of the Author:")
                genre=input("Enter the Genre:")
                price=float(input("Enter the Price:"))
                l=[book_num,book_name,publication,author_name,genre,price]
                x="insert into novels values(%s,%s,%s,%s,%s,%s,True)"
                cursor.execute(x,l)
                mycon.commit()
                print("The book has been added")
            else:
                print("Book Number already exists")
        elif tell==2:
            book_num=int(input("Enter the Book Number:"))
            if book_num not in reference:
                book_name=input("Enter the Book Name:")
                publication=input("Enter the name of the Publication:")
                author_name=input("Enter Name of the Author:")
                subject=input("Enter the Subject:")
                price=float(input("Enter the Price:"))
                l=[book_num,book_name,publication,author_name,subject,price]
                x="insert into reference values(%s,%s,%s,%s,%s,%s,True)"
                cursor.execute(x,l)
                mycon.commit()
                print("The book has been added")
            else:
                print("Book Number already exists")
        elif tell==3:
            break
        else:
            print('Enter valid number')
            continue

#Function to Remove Books
def admin_remove():
    while True:
        cursor.execute('select novel_no from novels where availability=1')
        data=cursor.fetchall()
        novel_avail=[]
        for i in data:
            novel_avail.append(i[0])
        cursor.execute('select reference_book_no from reference where availability=1')
        data=cursor.fetchall()
        reference_avail=[]
        for i in data:
            reference_avail.append(i[0])
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
        if novel!=[] or reference!=[]:
            tell=int(input('''Do you wish to remove
1. Novels
2. Reference Books
3. Quit\n'''))
            if tell==1:
                if novel!=[]:
                    novel_no=int(input("Enter the Novel Number:"))
                    if novel_no in novel:
                        if novel_no in novel_avail:
                            a='delete from novels where novel_no={}'.format(novel_no)
                            cursor.execute(a)
                            mycon.commit()
                            print("The book has been removed")
                        else:
                            print("The book has been borrowed. Wait till it is returned to remove it")
                    else:
                        print("Novel Number does not exist")
                else:
                    print("All Novels have been borrowed. Wait till they are returned to remove it")
            elif tell==2:
                if reference!=[]:
                    reference_book_no=int(input("Enter the Reference Book Number:"))
                    if reference_book_no in reference:
                        if reference_book_no in reference_avail:
                            a='delete from reference where reference_book_no={}'.format(reference_book_no)
                            cursor.execute(a)
                            mycon.commit()
                            print("The book has been removed")
                        else:
                            print("The book has been borrowed. Wait till it is returned to remove it")
                    else:
                        print("Reference Book Number does not exist")
                else:
                    print("All Reference Books have been borrowed. Wait till they are returned to remove it")
            elif tell==3:
                break
            else:
                print("Enter valid number")
                continue
        else:
            print("All the books have been borrowed. Wait till they have been returned to remove them")
            break

#Function to Edit Books
def admin_edit():
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
    print(reference)
    if novel!=[] or reference!=[]:
        while True:
            tell=int(input('''Do you wish to edit
1. Novels
2. Reference Books
3. Quit\n'''))
            if tell==1:
                book_no=int(input("Enter Novel number:"))
                if book_no in novel:
                    while True:
                        t1=int(input('''What do you wish to edit?
1. Book Name
2. Publication
3. Author Name
4. Genre
5. Price
6. Quit\n'''))
                        if t1==1:
                            book_name=input("Enter the name new name of the Novel:")
                            a='update novels set Novel_Name="{}" where novel_no={}'.format(book_name,book_no)
                            cursor.execute(a)
                            mycon.commit()
                        elif t1==2:
                            publication=input("Enter the new Publication:")
                            a='update novels set Publication="{}" where novel_no={}'.format(publication,book_no)
                            cursor.execute(a)
                            mycon.commit()
                        elif t1==3:
                            author_name=input("Enter the new Author Name:")
                            a='update novels set Author_name="{}" where novel_no={}'.format(author_name,book_no)
                            cursor.execute(a)
                            mycon.commit()
                        elif t1==4:
                            genre=input("Enter the new Genre:")
                            a='update novels set genre="{}" where novel_no={}'.format(genre,book_no)
                            cursor.execute(a)
                            mycon.commit()
                        elif t1==5:
                            price=float(input("Enter the new Price of the book:"))
                            a='update novels set price={} where novel_no={}'.format(price,book_no)
                            cursor.execute(a)
                            mycon.commit()
                        elif  t1==6:
                            break
                        else:
                            print("Enter valid number")
                            continue
                else:
                    print("Incorrect Novel Number")
            elif tell==2:
                book_no=int(input("Enter Reference Book number:"))
                if book_no in reference:
                    while True:
                        t1=int(input('''What do you wish to edit?
1. Book Name
2. Publication
3. Author Name
4. Subject
5. Price
6. Quit\n'''))
                        if t1==1:
                            book_name=input("Enter the name new name of the Novel:")
                            a='update reference set Novel_Name="{}" where reference_book_no={}'.format(book_name,book_no)
                            cursor.execute(a)
                            mycon.commit()
                        elif t1==2:
                            publication=input("Enter the new Publication:")
                            a='update reference set Publication="{}" where reference_book_no={}'.format(publication,book_no)
                            cursor.execute(a)
                            mycon.commit()
                        elif t1==3:
                            author_name=input("Enter the new Author Name:")
                            a='update reference set Author_name="{}" where reference_book_no={}'.format(author_name,book_no)
                            cursor.execute(a)
                            mycon.commit()
                        elif t1==4:
                            subject=input("Enter the changed Subject:")
                            a='update reference set genre="{}" where reference_book_no={}'.format(subject,book_no)
                            cursor.execute(a)
                            mycon.commit()
                        elif t1==5:
                            price=float(input("Enter the new Price of the book:"))
                            a='update reference set price={} where reference_book_no={}'.format(price,book_no)
                            cursor.execute(a)
                            mycon.commit()
                        elif t1==6:
                            break
                        else:
                            print("Enter valid number")
                            continue
                else:
                    print("Incorrect Reference Book Number")
            elif tell==3:
                break
    else:
        print("There are no books in the system")
        
#Function to View all Borrowed Books 
def admin_list():
    print("STUDENT NOVELS:")
    cursor.execute('select novels.novel_no,novel_name,student_id,student_name,class,section from novels,students where novels.novel_no=students.novel_no')
    student_novel=cursor.fetchall()
    if student_novel!=[]:
        for i in student_novel:
            print(i)
    else:
        print("Students have not borrowed any Novels")
    print("STUDENT REFERENCE BOOKS:")
    cursor.execute('select reference.reference_book_no,reference_book_name,subject,student_id,student_name,class,section from reference,students where students.reference_book_no=reference.reference_book_no')
    student_reference=cursor.fetchall()
    if student_reference!=[]:
        for i in student_reference:
            print(i)
    else:
        print("Students have not borrowed any Reference Books")
    print("TEACHER NOVELS:")
    cursor.execute('select novels.novel_no,novel_name,teacher_id,teacher_name from teacher,novels where teacher.novel_no=novels.novel_no')
    teacher_novel=cursor.fetchall()
    if teacher_novel!=[]:
        for i in teacher_novel:
            print(i)
    else:
        print("Teachers have not borrowed any Novels")
    print("TEACHER REFERENCE:")
    cursor.execute('select reference_book_no,reference_book_name,teacher_id,teacher_name from teacher,reference where reference_book_no in (reference_book_no_1,reference_book_no_2,reference_book_no_3)')
    teacher_reference=cursor.fetchall()
    if teacher_reference!=[]:
        for i in teacher_reference:
            print(i)
    else:
        print("Teachers have not borrowed any Reference Books")

#Function to Delete Users
def admin_delete_user():
    cursor.execute('select teacher_ID from teacher')
    data=cursor.fetchall()
    teacher=[]
    for i in data:
        teacher.append(i[0])
    cursor.execute('select student_ID from students')
    data=cursor.fetchall()
    student=[]
    for i in data:
        student.append(i[0])
    if teacher!=[] and student!=[]:
        while True:
            t=int(input('''Do you wish to remove
1. Teachers
2. Students
3. Quit\n'''))
            if t==1:
                cursor.execute('select Teacher_ID,Teacher_Name from teacher')
                data=cursor.fetchall()
                for i in data:
                    print(i)
                if teacher!=[]:
                    teacher_no=int(input("Enter the Teacher ID:"))
                    if teacher_no in teacher:
                        cursor.execute('select novel_no,reference_book_no_1,reference_book_no_2,reference_book_no_3 from teacher where teacher_ID={}'.format(teacher_no))
                        borrowed_books=cursor.fetchall()
                        if borrowed_books==[(None,None,None,None)]:
                            cursor.execute('delete from teacher where teacher_ID={}'.format(teacher_no))
                            mycon.commit()
                            print("The user has been deleted")
                        else:
                            print("The user has borrowed books. Wait for them to return it to remove them.")
                    else:
                        print("Invalid Teacher ID")
                else:
                    print("There are no Teachers using the Library")
            elif t==2:
                cursor.execute('select Student_ID,Student_Name from students')
                data=cursor.fetchall()
                for i in data:
                    print(i)
                if student!=[]:
                        student_no=int(input("Enter the Student ID:"))
                        if student_no in student:
                            cursor.execute('select novel_no,reference_book_no from students where student_ID={}'.format(student_no))
                            borrowed_books=cursor.fetchall()
                            if borrowed_books==[(None,None)]:
                                cursor.execute('delete from students where student_ID={}'.format(student_no))
                                mycon.commit()
                                print("The user has been deleted")
                            else:
                                print("The user has borrowed books. Wait for them to return it to remove them.")
                        else:
                            print("Invalid Student ID")
                else:
                    print("There are no Students using the Library")
            elif t==3:
                break
            else:
                continue
    else:
        print("There are no Users")
#Function for Teachers to Borrow Books
def teacher_borrow(teacher_no,date):
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
    while True:
        cursor.execute('select Novel_no,Reference_Book_No from students where Student_ID={}'.format(teacher_no))
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
        cursor.execute('select Novel_no,Reference_Book_No_1,Reference_Book_No_2,Reference_Book_No_3 from Teacher where Teacher_ID={}'.format(teacher_no))
        borrowed_books=cursor.fetchall()
        if borrowed_books[0][0]==None or borrowed_books[0][1]==None or borrowed_books[0][2]==None or borrowed_books[0][3]==None:
            if availability_novels!=[] or availability_reference!=[]:
                t=int(input('''Do you wish to borrow a
1. Novel
2. Reference Book
3. Quit\n'''))
                if t==1:
                    if availability_novels!=[]:
                        if borrowed_books[0][0]==None:
                            a="select Novel_No,Novel_name,Publication,Author_Name,Genre from novels where availability=1"
                            cursor.execute(a)
                            data=cursor.fetchall()
                            for i in data:
                                print(i)
                            novel_no=int(input("Enter the Novel Number you wish to borrow:"))
                            if novel_no in novel:
                                if novel_no in availability_novels:
                                    a='update Teacher set Novel_No={},Novel_Date="{}" where teacher_ID={}'.format(novel_no,date,teacher_no)
                                    cursor.execute(a)
                                    mycon.commit()
                                    a1='update Novels set Availability=False where Novel_No={}'.format(novel_no)
                                    cursor.execute(a1)
                                    mycon.commit()
                                    print("You have borrowed the book. Please return it in proper condition. Thank You")
                                else:
                                    print("The book is already taken. Please come back later.")
                            else:
                                print("Novel Number does not exist")
                        else:
                            print("You have already borrowed a Novel. Return it to borrow another one")
                    else:
                        print("No Novels are currently available. Please come back later")
                elif t==2:
                    if availability_reference!=[]:
                        if borrowed_books[0][1]==None or borrowed_books[0][2]==None or borrowed_books[0][3]==None:
                            cursor.execute('select Reference_Book_No, Reference_Book_Name,Publication,Author_Name,Subject from reference where availability=1')
                            data=cursor.fetchall()
                            for i in data:
                                print(i)
                            if borrowed_books[0][1]==None:
                                reference_book_no=int(input("Enter the Reference Book Number of the Book you wish to borrow:"))
                                if reference_book_no in reference:
                                    if reference_book_no in availability_reference:
                                        a='update Teacher set Reference_Book_No_1={},Reference_Book_No_1_Date="{}" where teacher_ID={}'.format(reference_book_no,date,teacher_no)
                                        cursor.execute(a)
                                        mycon.commit()
                                        a1='update Reference set Availability=False where Reference_Book_No={}'.format(reference_book_no)
                                        cursor.execute(a1)
                                        mycon.commit()
                                        print("You have borrowed the book. Please return it in proper condition. Thank You")
                                    else:
                                        print("The book is already taken. Please come back later.")
                                else:
                                    print("Reference Book Number does not exist")
                            elif borrowed_books[0][2]==None:
                                reference_book_no=int(input("Enter the Reference Book Number of the Book you wish to borrow:"))
                                if reference_book_no in reference:
                                    if reference_book_no in availability_reference:
                                        a='update Teacher set Reference_Book_No_2={},Reference_Book_No_2_Date="{}" where teacher_ID={}'.format(reference_book_no,date,teacher_no)
                                        cursor.execute(a)
                                        mycon.commit()
                                        a1='update Reference set Availability=False where Reference_Book_No={}'.format(reference_book_no)
                                        cursor.execute(a1)
                                        mycon.commit()
                                        print("You have borrowed the book. Please return it in proper condition. Thank You")
                                    else:
                                        print("The book is already taken. Please come back later.")
                                else:
                                    print("Reference Book Number does not exist")
                            elif borrowed_books[0][3]==None:
                                reference_book_no=int(input("Enter the Reference Book Number of the Book you wish to borrow:"))
                                if reference_book_no in reference:
                                    if reference_book_no in availability_reference:
                                        a='update Teacher set Reference_Book_No_3={},Reference_Book_No_3_Date="{}" where teacher_ID={}'.format(reference_book_no,date,teacher_no)
                                        cursor.execute(a)
                                        mycon.commit()
                                        a1='update Reference set Availability=False where Reference_Book_No={}'.format(reference_book_no)
                                        cursor.execute(a1)
                                        mycon.commit()
                                        print("You have borrowed the book. Please return it in proper condition. Thank You")
                                    else:
                                        print("The book is already taken. Please come back later.")
                                else:
                                    print("Reference Book Number does not exist")
                            else:
                                print("You have borrowed 3 reference books. Return one to borrow another.")
                        else:
                            print("You have borrowed 3 Reference Books. Return one to borrow another.")
                    else:
                        print("No Reference Books are currently available. Please come back later.")
                elif t==3:
                    break
                else:
                    print("Enter valid number")
            else:
                print("There are no books available")
                break
        else:
            print("You have borrowed 4 books. Please return one to borrow another one.")
            break
#Function for Teachers to Return Books 
def teacher_return(teacher_no,date):
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
    while True:
        cursor.execute('select Novel_no,Reference_Book_No_1,Reference_Book_No_2,Reference_Book_No_3 from Teacher where Teacher_ID={}'.format(teacher_no))
        borrowed_books=cursor.fetchall()
        if borrowed_books!=[(None,None,None,None)]:
            t=int(input('''Do you wish to return a
1. Novel
2. Reference Book
3. Quit\n'''))
            if t==1:
                if borrowed_books[0][0]!=None:
                    novel_no=int(input("Enter the Novel Number:"))
                    if novel_no in novel:
                        if borrowed_books[0][0]==novel_no:
                            a1='select datediff("{}",Novel_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            a='update teacher set Novel_No=NULL,Novel_date=NULL where Teacher_ID={}'.format(teacher_no)
                            cursor.execute(a)
                            mycon.commit()
                            a2='update Novels set Availability=True where novel_no={}'.format(novel_no)
                            cursor.execute(a2)
                            mycon.commit()
                            if date_difference[0][0]>30:
                                print("Pay a fine of ",(date_difference[0][0]-30)," at the desk")
                            else:
                                print("Thank You")
                            break
                        else:
                            print("Incorrect Novel Number")
                    else:
                        print("Novel Number does not exist")
                else:
                    print("You have not borrowed a novel")
            elif t==2:
                if borrowed_books[0][1]!=None or borrowed_books[0][2]!=None or borrowed_books[0][3]!=None:
                    reference_book_no=int(input("Enter the Reference Book Number:"))
                    if reference_book_no in reference:
                        if borrowed_books[0][1]==reference_book_no:
                            a1='select datediff("{}",Reference_Book_No_1_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            a='update teacher set Reference_Book_No_1=NULL,Reference_Book_No_1_Date=NULL where Teacher_ID={}'.format(teacher_no)
                            cursor.execute(a)
                            mycon.commit()
                            a2='update Reference set Availability=True where reference_book_no={}'.format(reference_book_no)
                            cursor.execute(a2)
                            mycon.commit()
                            if date_difference[0][0]>30:
                                print("Pay a fine of ",(date_difference[0][0]-30)," at the desk")
                            else:
                                print("Thank You")
                        elif borrowed_books[0][2]==reference_book_no:
                            a1='select datediff("{}",Reference_Book_No_2_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            a='update teacher set Reference_Book_No_2=NULL,Reference_Book_No_2_Date=NULL where Teacher_ID={}'.format(teacher_no)
                            cursor.execute(a)
                            mycon.commit()
                            a2='update Reference set Availability=True where reference_book_no={}'.format(reference_book_no)
                            cursor.execute(a2)
                            mycon.commit()
                            if date_difference[0][0]>30:
                                print("Pay a fine of ",(date_difference[0][0]-30)," at the desk")
                            else:
                                print("Thank You")
                        elif borrowed_books[0][3]==reference_book_no:
                            a1='select datediff("{}",Reference_Book_No_3_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            a='update teacher set Reference_Book_No_3=NULL,Reference_Book_No_3_Date=NULL where Teacher_ID={}'.format(teacher_no)
                            cursor.execute(a)
                            mycon.commit()
                            a2='update Reference set Availability=True where reference_book_no={}'.format(reference_book_no)
                            cursor.execute(a2)
                            mycon.commit()
                            if date_difference[0][0]>30:
                                print("Pay a fine of ",(date_difference[0][0]-30)," at the desk")
                            else:
                                print("Thank You")
                        else:
                            print("Incorrect Reference Book Number")
                    else:
                        print("Reference Book Number does not exist")
                else:
                    print("You have not borrowed any Reference Books")
            elif t==3:
                break
            else:
                print("Enter valid number")
        else:
            print("You have not borrowed any books")
            break

#Function for Teachers to View their borrowed books       
def teacher_view(teacher_no):
    cursor.execute('select Novel_no,Reference_Book_No_1,Reference_Book_No_2,Reference_Book_No_3 from Teacher where Teacher_ID={}'.format(teacher_no))
    borrowed_books=cursor.fetchall()
    if borrowed_books[0][0]!=None:
        cursor.execute('select novels.novel_no,novel_name from teacher,novels where novels.novel_no=teacher.novel_no and teacher_ID={}'.format(teacher_no))
        borrowed_novel=cursor.fetchall()
        print("Novel Number:",borrowed_novel[0][0],"\tNovel Name:",borrowed_novel[0][1])
    else:
        print("You have not borrowed a novel")
    if borrowed_books[0][1]!=None:
        cursor.execute('select reference_book_no,reference_book_name from teacher,reference where reference_book_no_1=reference_book_no and teacher_ID={}'.format(teacher_no))
        borrowed_novel=cursor.fetchall()
        print("Reference Book Number 1:",borrowed_novel[0][0],"\tReference Book Name 1:",borrowed_novel[0][1])
    else:
        print("Reference Book Slot Number 1 is empty")
    if borrowed_books[0][2]!=None:
        cursor.execute('select reference_book_no,reference_book_name from teacher,reference where reference_book_no_2=reference_book_no and teacher_ID={}'.format(teacher_no))
        borrowed_novel=cursor.fetchall()
        print("Reference Book Number 2:",borrowed_novel[0][0],"\tReference Book Name 2:",borrowed_novel[0][1])
    else:
        print("Reference Book Slot Number 2 is empty")
    if borrowed_books[0][3]!=None:
        cursor.execute('select reference_book_no,reference_book_name from teacher,reference where reference_book_no_3=reference_book_no and teacher_ID={}'.format(teacher_no))
        borrowed_novel=cursor.fetchall()
        print("Reference Book Number 3:",borrowed_novel[0][0],"\tReference Book Name 3:",borrowed_novel[0][1])
    else:
        print("Reference Book Slot Number 3 is empty")

#Function for Teachers to extend the time to return their borrowed books
def teacher_extend(teacher_no,date):
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
    while True:
        if borrowed_books!=[(None,None,None,None)]:
            tell=int(input('''Do you wish to extend time of
1. Novel
2. Reference Books
3. Quit\n'''))
            if tell==1:
                if borrowed_books[0][0]!=None:
                    novel_no=int(input("Enter Novel Number:"))
                    if novel_no in novel:
                        if borrowed_books[0][0]==novel_no:
                            a1='select datediff("{}",Novel_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            if date_difference[0][0]>30:
                                print("You have exceeded the time to return the book")
                                print("Please return the book with a fine of ",date_difference[0][0]-30," rupees")
                            a='update teacher set Novel_Date="{}" where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a)
                            mycon.commit()
                            print("The time to return the book has been extended")
                        else:
                            print("Incorrect Novel Number")
                    else:
                        print("Novel Number does not exist")
                else:
                    print("You have not borrowed Novels")
            elif tell==2:
                if borrowed_books[0][1]!=None or borrowed_books[0][2]!=None or borrowed_books[0][3]!=None:
                    reference_book_no=int(input("Enter the Reference Book Number:"))
                    if reference_book_no in reference:
                        if borrowed_books[0][1]==reference_book_no:
                            a1='select datediff("{}",Reference_Book_No_1_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            if date_difference[0][0]>30:
                                print("You have exceeded the time to return the book")
                                print("Please return the book with a fine of ",date_difference[0][0]-30," rupees")
                            a='update teacher set Reference_Book_No_1_Date="{}" where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a)
                            mycon.commit()
                            print("The time to return the book has been extended")
                        elif borrowed_books[0][2]==reference_book_no:
                            a1='select datediff("{}",Reference_Book_No_2_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            if date_difference[0][0]>30:
                                print("You have exceeded the time to return the book")
                                print("Please return the book with a fine of ",date_difference[0][0]-30," rupees")
                            a='update teacher set Reference_Book_No_2_Date="{}" where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a)
                            mycon.commit()
                            print("The time to return the book has been extended")
                        elif borrowed_books[0][3]==reference_book_no:
                            a1='select datediff("{}",Reference_Book_No_3_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            if date_difference[0][0]>30:
                                print("You have exceeded the time to return the book")
                                print("Please return the book with a fine of ",date_difference[0][0]-30," rupees")
                            a='update teacher set Reference_Book_No_3_Date="{}" where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a)
                            mycon.commit()
                            print("The time to return the book has been extended")
                        else:
                            print("Invalid Reference Book Number")
                    else:
                        print("Invalid Book Number")
                else:
                    print("You have not borrowed Reference Books")
            elif tell==3:
                break
            else:
                print("Enter valid number")
        else:
            print("You have not borrowed any books")
            break

#Function for Teachers to check the time left to return the book
def teacher_time(teacher_no,date):
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
    while True:
        if borrowed_books!=[(None,None,None,None)]:
            tell=int(input('''Which book do you wish to check time left on?
1. Novel
2. Reference Books
3. Quit\n'''))
            if tell==1:
                if borrowed_books[0][0]!=None:
                    novel_no=int(input("Enter the Novel Number"))
                    if novel_no in novel:
                        if borrowed_books[0][0]==novel_no:
                            a1='select datediff("{}",Novel_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            if date_difference[0][0]<=30:
                                print("You have ", 30-date_difference[0][0]," days to return the book")
                            else:
                                print("You have exceeded the time to return the book")
                                print("Please return the book with a fine of ",date_difference[0][0]-30," rupees")
                        else:
                            print("Incorrect Novel Number")
                    else:
                        print("Invalid Book Number")
                else:
                    print("You have not borrowed any Novels")
            elif tell==2:
                if borrowed_books[0][1]!=None or borrowed_books[0][2]!=None or borrowed_books[0][3]!=None:
                    reference_book_no=int(input("Enter the Reference Book Number:"))
                    if reference_book_no in reference:
                        if borrowed_books[0][1]==reference_book_no:
                            a1='select datediff("{}",Reference_Book_No_1_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            if date_difference[0][0]<=30:
                                print("You have ", 30-date_difference[0][0]," days to return the book")
                                break
                            else:
                                print("You have exceeded the time to return the book")
                                print("Please return the book with a fine of ",date_difference[0][0]-30," rupees")
                        elif borrowed_books[0][2]==reference_book_no:
                            a1='select datediff("{}",Reference_Book_No_2_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            if date_difference[0][0]<=30:
                                print("You have ", 30-date_difference[0][0]," days to return the book")
                                break
                            else:
                                print("You have exceeded the time to return the book")
                                print("Please return the book with a fine of ",date_difference[0][0]-30," rupees")
                        elif borrowed_books[0][3]==reference_book_no:
                            a1='select datediff("{}",Reference_Book_No_3_Date) from Teacher where teacher_ID={}'.format(date,teacher_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            if date_difference[0][0]<=30:
                                print("You have ", 30-date_difference[0][0]," days to return the book")
                                break
                            else:
                                print("You have exceeded the time to return the book")
                                print("Please return the book with a fine of ",date_difference[0][0]-30," rupees")
                        else:
                            print("Incorrect Reference Number")
                    else:
                        print("Invalid Book Number")
                else:
                    print("You have not borrowed Reference Books")
            elif tell==3:
                break
            else:
                print("Enter valid number")
        else:
            print("You have not borrowed any books")
            break

#Function for students to borrow books
def student_borrow(student_no,date):
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
    while True:
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
        if availability_reference!=[] or availability_novels!=[]:
            tell=int(input('''Do you wish to borrow
1. Novel
2. Reference Book
3. Quit\n'''))
            if tell==1:
                if availability_novels!=[]:
                    if borrowed_books[0][0]==None:
                        a="select Novel_No,Novel_name,Publication,Author_Name,Genre from novels where availability=1"
                        cursor.execute(a)
                        data=cursor.fetchall()
                        for i in data:
                            print(i)
                        novel_no=int(input("Enter the Novel Number you wish to borrow:"))
                        if novel_no in novel:
                            if novel_no in availability_novels:
                                a='update Students set Novel_No={},Novel_Date="{}" where student_ID={}'.format(novel_no,date,student_no)
                                cursor.execute(a)
                                mycon.commit()
                                a1='update Novels set Availability=False where Novel_No={}'.format(novel_no)
                                cursor.execute(a1)
                                mycon.commit()
                                print("You have borrowed the book. Please return it in proper condition. Thank You")
                            else:
                                print("The book is already taken. Please come back later.")
                        else:
                            print("Invalid Book Number")
                    else:
                        print("You have already borrowed a Novel. Please return it to borrow another one")
                else:
                    print("No Novels are currently available. Please come back later")
            elif tell==2:
                if availability_reference!=[]:
                    if borrowed_books[0][1]==None:
                        a="select Reference_Book_No, Reference_Book_Name, Publication, Author_Name, Subject from reference where Availability=1"
                        cursor.execute(a)
                        data=cursor.fetchall()
                        for i in data:
                            print(i)
                        reference_book_no=int(input("Enter the Reference Book Number of the Book you wish to borrow:"))
                        if reference_book_no in reference:
                            if reference_book_no in availability_reference:
                                a='update students set Reference_Book_No={},Reference_Book_Date="{}" where student_ID={}'.format(reference_book_no,date,student_no)
                                cursor.execute(a)
                                mycon.commit()
                                a1='update Reference set Availability=False where Reference_Book_No={}'.format(reference_book_no)
                                cursor.execute(a1)
                                mycon.commit()
                                print("You have borrowed the book. Please return it in proper condition. Thank You")
                            else:
                                print("The book is already taken. Please come back later.")
                        else:
                            print("Invalid Book Number")
                    else:
                        print("You have already borrowed a Reference Book. Please return it to borrow another one")
                else:
                    print("No Reference Books are currently available. Please come back later.")
            elif tell==3:
                break
            else:
                print("Enter valid number")
        else:
            print("Sorry. There are no books available.")
            break
        
#Function for students to return their books
def student_return(student_no,date):
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
    while True:
        cursor.execute('select Novel_no,Reference_Book_No from Students where Student_ID={}'.format(student_no))
        borrowed_books=cursor.fetchall()
        if borrowed_books!=[(None,None)]:
            t=int(input('''Do you wish to return a
1. Novel
2. Reference Book
3. Quit\n'''))
            if t==1:
                if borrowed_books[0][0]!=None:
                    novel_no=int(input("Enter the Novel Number:"))
                    if novel_no in novel:
                        if borrowed_books[0][0]==novel_no:
                            a1='select datediff("{}",Novel_Date) from Students where student_ID={}'.format(date,student_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            a='update students set Novel_No=NULL,Novel_date=NULL where student_ID={}'.format(student_no)
                            cursor.execute(a)
                            mycon.commit()
                            a2='update Novels set Availability=True where novel_no={}'.format(novel_no)
                            cursor.execute(a2)
                            mycon.commit()
                            if date_difference[0][0]>15:
                                print("Pay a fine of ",(date_difference[0][0]-15)," at the desk")
                            else:
                                print("Thank You")
                        else:
                            print("Incorrect Novel Number")
                    else:
                        print("Invalid Book Number")
                else:
                    print("You have not borrowed a novel")
            elif t==2:
                if borrowed_books[0][1]!=None:
                    reference_book_no=int(input("Enter the Reference Book Number:"))
                    if reference_book_no in reference:
                        if borrowed_books[0][1]==reference_book_no:
                            a1='select datediff("{}",Reference_Book_Date) from students where student_ID={}'.format(date,student_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            a='update students set Reference_Book_No=NULL,Reference_Book_Date=NULL where Student_ID={}'.format(student_no)
                            cursor.execute(a)
                            mycon.commit()
                            a2='update Reference set Availability=True where reference_book_no={}'.format(reference_book_no)
                            cursor.execute(a2)
                            mycon.commit()
                            if date_difference[0][0]>30:
                                print("Pay a fine of ",(date_difference[0][0]-15)," at the desk")
                            else:
                                print("Thank You")
                        else:
                            print("Incorrect Reference Book Number")
                    else:
                        print("Invalid Book Number")
                else:
                    print("You have not borrowed any Reference Books")
            elif t==3:
                break
            else:
                print("Enter valid number")
        else:
            print("You have not borrowed any books.")
            break

#Function for students to view their borrowed books
def student_view(student_no):
    cursor.execute('select Novel_no,Reference_Book_No from students where student_ID={}'.format(student_no))
    borrowed_books=cursor.fetchall()
    if borrowed_books[0][0]!=None:
        cursor.execute('select novels.novel_no,novel_name from students,novels where novels.novel_no=students.novel_no and student_ID={}'.format(student_no))
        borrowed_novel=cursor.fetchall()
        print("Novel Number:",borrowed_novel[0][0],"\tNovel Name:",borrowed_novel[0][1])
    else:
        print("You have not borrowed a novel")
    if borrowed_books[0][1]!=None:
        cursor.execute('select reference.reference_book_no,reference_book_name from students,reference where students.reference_book_no=reference.reference_book_no and student_ID={}'.format(student_no))
        borrowed_novel=cursor.fetchall()
        print("Reference Book Number:",borrowed_novel[0][0],"\tReference Book Name:",borrowed_novel[0][1])
    else:
        print("You have not borrowed a Reference Book")    

#Function for students to extend their time left to return the book
def student_extend(student_no,date):
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
    while True:
        cursor.execute('select Novel_no,Reference_Book_No from students where student_ID={}'.format(student_no))
        borrowed_books=cursor.fetchall()
        if borrowed_books!=[(None,None)]:
            tell=int(input('''Do you wish to extend time of
1. Novel
2. Reference Books
3. Quit\n'''))
            if tell==1:
                if borrowed_books[0][0]!=None:
                    novel_no=int(input("Enter Novel Number:"))
                    if novel_no in novel:
                        if borrowed_books[0][0]==novel_no:
                            a1='select datediff("{}",Novel_Date) from students where student_ID={}'.format(date,student_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            if date_difference[0][0]>15:
                                print("You have exceeded the time to return the book")
                                print("Please return the book with a fine of ",date_difference[0][0]-15," rupees")
                            a='update students set Novel_Date="{}" where student_ID={}'.format(date,student_no)
                            cursor.execute(a)
                            mycon.commit()
                            print("The time to return the book has been extended")
                        else:
                            print("Incorrect Novel Number")
                    else:
                        print("Invalid Book Number")
                else:
                    print("You have not borrowed a Novel")
            elif tell==2:
                if borrowed_books[0][1]!=None:
                    reference_book_no=int(input("Enter the Reference Book Number:"))
                    if reference_book_no in reference:
                        if borrowed_books[0][1]==reference_book_no:
                            a1='select datediff("{}",Reference_Book_Date) from students where student_ID={}'.format(date,student_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            if date_difference[0][0]>15:
                                print("You have exceeded the time to return the book")
                                print("Please return the book with a fine of ",date_difference[0][0]-15," rupees")
                            a='update students set Reference_Book_Date="{}" where student_ID={}'.format(date,student_no)
                            cursor.execute(a)
                            mycon.commit()
                            print("The time to return the book has been extended")
                        else:
                            print("Invalid Reference Book Number")
                    else:
                        print("Invalid Book Number")
                else:
                    print("You have not borrowed a Reference Book")
            elif tell==3:
                break
            else:
                print("Enter valid number")
        else:
            print("You have not borrowed any books")
            break

#Function for Students to check the time left to return the book
def student_check(student_time,date):
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
    while True:
        cursor.execute('select Novel_no,Reference_Book_No from students where student_ID={}'.format(student_no))
        borrowed_books=cursor.fetchall()
        if borrowed_books!=[(None,None)]:
            tell=int(input('''Which book do you wish to check time left on?
1. Novel
2. Reference Books
3. Quit\n'''))
            if tell==1:
                if borrowed_books[0][0]!=None:
                    novel_no=int(input("Enter the Novel Number"))
                    if novel_no in novel:
                        if borrowed_books[0][0]==novel_no:
                            a1='select datediff("{}",Novel_Date) from students where student_ID={}'.format(date,student_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            if date_difference[0][0]<=15:
                                print("You have ", 15-date_difference[0][0]," days to return the book")
                            else:
                                print("You have exceeded the time to return the book")
                                print("Please return the book with a fine of ",date_difference[0][0]-15," rupees")
                        else:
                            print("Incorrect Novel Number")
                    else:
                        print("Invalid Book Number")
                else:
                    print("You have not borrowed a Novel")
            elif tell==2:
                if borrowed_books[0][1]!=None:
                    reference_book_no=int(input("Enter the Reference Book Number:"))
                    if reference_book_no in reference:
                        if borrowed_books[0][1]==reference_book_no:
                            a1='select datediff("{}",Reference_Book_Date) from students where student_ID={}'.format(date,student_no)
                            cursor.execute(a1)
                            date_difference=cursor.fetchall()
                            if date_difference[0][0]<=15:
                                print("You have ", 15-date_difference[0][0]," days to return the book")
                            else:
                                print("You have exceeded the time to return the book")
                                print("Please return the book with a fine of ",date_difference[0][0]-15," rupees")
                        else:
                            print("Incorrect Reference Book Number")
                    else:
                        print("Invalid Number")
                else:
                    print("You have not borrowed a Reference Book")
            elif tell==3:
                break
            else:
                print("Enter valid number")
        else:
            print("You have not borrowed any books")
            break

#Function for Teachers to Sign Up
def teacher_signup():
    print("SIGN UP:")
    while True:
        teacher_no=int(input("Enter your Teacher ID:"))
        cursor.execute('select Teacher_ID from Teacher')
        data=cursor.fetchall()
        teacher=[]
        for i in data:
            teacher.append(i[0])
        if teacher_no not in teacher:
            teacher_password =input("Create a Password:")
            teacher_name=input("Enter your name:")
            a='insert into teacher(teacher_ID,teacher_password,teacher_name) values({},"{}","{}")'.format(teacher_no,teacher_password,teacher_name)
            cursor.execute(a)
            mycon.commit()
            print("You have successfully signed up")
            break
        else:
            print("Teacher ID already exists")
    teacher_login(teacher_no,teacher_password)

#Function for Students to Sign Up
def student_signup():
    global student_no
    print("SIGN UP:")
    while True:
        cursor.execute('select Student_ID from Students')
        data=cursor.fetchall()
        student=[]
        for i in data:
            student.append(i[0])
        student_no=int(input("Enter your student ID:"))
        if student_no not in student:
            student_password=input("Create a Password:")
            student_name=input("Enter your name:")
            _class=int(input("Enter your class:"))
            section=input("Enter your section:")
            a='insert into students(student_ID,student_password,student_name,class,section) values({},"{}","{}",{},"{}")'.format(student_no,student_password,student_name,_class,section)
            cursor.execute(a)
            mycon.commit()
            print("You have successfully signed up")
            break
        else:
            print("Student ID already exists")
    student_login(student_no,student_password)

#Function for Teachers to Log In 
def teacher_login(teacher_no,teacher_password):
    while  True:
        cursor.execute('select Teacher_ID from Teacher')
        data=cursor.fetchall()
        teacher=[]
        for i in data:
            teacher.append(i[0])
        cursor.execute('select Teacher_Password from teacher where teacher_ID={}'.format(teacher_no))
        password_teacher=cursor.fetchall()
        if teacher_no not in teacher:
            print("You have not signed up before")
            teacher_signup()
        else:
            while True:
                if teacher_password==password_teacher[0][0]:
                    s1=int(input('''Do you wish to
1. Borrow a book
2. Return a book
3. View all borrowed Books
4. Extend time to return book
5. Check time to return book
6. Filter books 
7. Quit\n'''))
                    if s1==1:
                        teacher_borrow(teacher_no,date)
                    elif s1==2:
                        teacher_return(teacher_no,date)
                    elif s1==3:
                        teacher_view(teacher_no)
                    elif s1==4:
                        teacher_extend(teacher_no,date)
                    elif s1==5:
                        teacher_time(teacher_no,date)
                    elif s1==6:
                        _filter()
                    elif s1==7:
                        break
                    else:
                        print("Enter valid number")
                else:
                    print("Incorrect Password")
                    return True
        break

#Function for Students to Log In
def student_login(student_no,student_password):
    while True:
        cursor.execute('select Student_ID from Students')
        data=cursor.fetchall()
        student=[]
        for i in data:
            student.append(i[0])
        cursor.execute('select student_Password from students where student_ID={}'.format(student_no))
        password_student=cursor.fetchall()
        if student_no not in student:
            print("You have not signed up before")
            student_signup()
        else:
            while True:
                if student_password==password_student[0][0]:
                    s1=int(input('''Do you wish to
1. Borrow a book
2. Return a book
3. View all borrowed Books
4. Extend time to return book
5. Check time to return book
6. Filter books 
7. Quit\n'''))
                    if s1==1:
                        student_borrow(student_no,date)
                    elif s1==2:
                        student_return(student_no,date)
                    elif s1==3:
                        student_view(student_no)
                    elif s1==4:
                        student_extend(student_no,date)
                    elif s1==5:
                        student_check(student_no,date)
                    elif s1==6:
                        _filter()
                    elif s1==7:
                        break
                    else:
                        print("Enter valid number")
                else:
                    print("Incorrect Password")
                    return True
        break

#Main Program
import mysql.connector as m
mycon=m.connect(host='localhost',user='root',password='123456',database='library')
cursor=mycon.cursor()
date=input("Enter the date as(YYYY-MM-DD):")
while True:
    s=int(input('''1. Teacher
2. Student
3. Admin
4. Quit\n'''))
    if s==1:
        while True:
            t=int(input('''Have you borrowed a book before?
1. Yes
2. No\n'''))
            if t==2:
                teacher_signup()
                break
            elif t==1:
                print("LOGIN:")
                teacher_no=int(input("Enter your Teacher ID:"))
                while True:
                    teacher_password=input("Enter your Password:")
                    if teacher_login(teacher_no,teacher_password):
                        continue
                    else:
                        break
                break
            else:
                print("Invalid input")
    elif s==2:
        while True:
            t=int(input('''Have you borrowed a book before?
1. Yes
2. No\n'''))
            if t==2:
                student_signup()
                break
            elif t==1:
                print("LOGIN:")
                student_no=int(input("Enter your Student ID:"))
                while True:
                    student_password=input("Enter your Password:")
                    if student_login(student_no,student_password):
                        continue
                    else:
                        break
                break
            else:
                print("Invalid input")
    elif s==3:
        while True:
            s1=int(input('''Do you wish to
1. Add a book
2. Remove a book
3. Edit details of a book
4. List borrowed books
5. Delete Users
6. Quit\n'''))
            if s1==1:
                admin_add()
            elif s1==2:
                admin_remove()
            elif s1==3:
                admin_edit()
            elif s1==4:
                admin_list()
            elif s1==5:
                admin_delete_user()
            elif s1==6:
                break
            else:
                print("Enter a valid number")

    elif s==4:
        break
    else:
        print("Enter valid number")
