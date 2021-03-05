

def word_format(word):
    new_word=word[len(word)//2:]+word[:len(word)//2] 
    for i in range(1,len(word)+1):
        print_string =""
        for x in range(0,len(word)-i):               
            print_string = print_string + " "
        print_string = print_string + new_word[:i]    
        print(print_string)
    

word_format("water")
