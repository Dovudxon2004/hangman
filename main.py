import random
with open('sowpods.txt') as text:
    wait=list(text)
    word=random.choice(wait).strip()
    word=list(word)
    a='_'*len(word)
    lst=list(a)
    print(' '.join(lst))
empty=set()



    
def play():
    global lst 
    k=0
    while '_' in lst:
        ans=input('Guess the letter ')
        
        
        if k==6:
            print('The word was '+''.join(word))
            print('You lost')
            break
        while ans.upper() in empty:
            ans=input("it's already picked, try another letter ")
        while ans.upper() in word:
        #didn't fully understand
            empty.add(ans.upper())           
            indices=[index for index, element in enumerate(word) if element == ans.upper()]
            for elem in indices:
                lst[elem]=ans.upper()
            empty.add(ans.upper())
            if lst==word:
                print(' '.join(lst))
                print('you won')    
                break
                
            
            print(' '.join(lst))
            ans=input('Guess the letter again ')
            while ans.upper() in empty:
                print(' '.join(lst))
                ans=input("it's already picked, try another letter ")
        while ans.upper() in empty:
            print(' '.join(lst))
            ans=input("it's already picked, try another letter ")
            while ans.upper() in word:
                empty.add(ans.upper())
                indices=[index for index, element in enumerate(word) if element == ans.upper()]
                for elem in indices:
                    lst[elem]=ans.upper()
                if lst==word:
                    print(' '.join(lst))
                    print('you won')    
                    break
                print(' '.join(lst))
                ans=input('Guess the letter')
            
        while ans.upper() not in word:
            k+=1
            empty.add(ans.upper())
            
            if k==6:
                print('The word was '+''.join(word))
                print('You lost')
                break
            print('you have '+str(6-k)+' chances to guess incorrectly')
            print(' '.join(lst))
            ans=input("it's not in the word, try again ")
            
                 
            while ans.upper() in empty:
                print(' '.join(lst))
                ans=input("it's already picked, try another letter ")
            while ans.upper() in word:
                empty.add(ans.upper())
                indices=[index for index, element in enumerate(word) if element == ans.upper()]
                for elem in indices:
                    lst[elem]=ans.upper()
                if lst==word:
                    print(' '.join(lst))
                    print('you won')  
                    break  
                print(' '.join(lst))
                ans=input('Guess the letter again ')
        if k==6:
           break
        if lst==word:
            print(' '.join(lst))
            print('you won') 
            break      
    
if __name__ == "__main__":
    play()
    
        
