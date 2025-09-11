
def print_lyrics():
    print('Boots')
    print('Cats')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    print_lyrics()

# repeat_lyrics()

def print_twice(input):
    print(input)
    print(input)
    
# print_twice('spam'*4)

def is_it_even(input):
    if input % 2 == 0:
        print('4 is even')
    else:
     print('5 is odd')

is_it_even(4)
is_it_even(5)