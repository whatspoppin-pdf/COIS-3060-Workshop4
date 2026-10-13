# Add a new book to the catalog 
print('Add a New Book') 
print('-' * 20) 
title = input('Enter book title: ') 
author = input('Enter author: ') 
year = input('Enter year: ') 
 
with open('books.txt', 'a') as f: 
    f.write(f'{title}, {author}, {year}\n') 
 
print(f'Successfully added "{title}"!')
