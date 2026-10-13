# Search for books in the catalog 
print('Search Books') 
print('-' * 20) 
search_term = input('Enter search term: ') 
 
print(f'\nSearching for "{search_term}"...') 
found = False 
 
with open('books.txt', 'r') as f: 
    for line in f: 
        if search_term.lower() in line.lower(): 
            print(line.strip()) 
            found = True 
 
if not found: 
    print('No books found.') 
