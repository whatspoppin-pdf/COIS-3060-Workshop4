# List all books in the catalog 
print('Library Catalog') 
print('=' * 50) 
 
count = 0 
with open('books.txt', 'r') as f: 
    for line in f: 
        count += 1 
        print(f'{count}. {line.strip()}') 
 
print(f'\nTotal books: {count}')
