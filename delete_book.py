# Delete a book from the catalog 
print('Delete a Book') 
print('-' * 20) 
 
# Read all books 
books = [] 
with open('books.txt', 'r') as f: 
    books = f.readlines() 
 
if not books: 
    print('No books in catalog.') 
else: 
    # Display books with numbers 
    print('\nCurrent books:') 
    for i, book in enumerate(books, 1): 
        print(f'{i}. {book.strip()}') 
     
    # Get book number to delete 
    try: 
        num = int(input('\nEnter book number to delete: ')) 
        if 1 <= num <= len(books): 
            deleted_book = books[num - 1].strip() 
            books.pop(num - 1) 
             
            # Write back to file 
            with open('books.txt', 'w') as f: 
                f.writelines(books) 
             
            print(f'Successfully deleted: {deleted_book}') 
        else: 
            print('Invalid book number.') 
    except ValueError: 
        print('Please enter a valid number.')
