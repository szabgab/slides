import random


def main():
    hidden = [str(x) for x in random.sample(range(1, 7), 4)]
    #print(hidden)
    
    while(True):
        print("Please enter 4 digits")
        guess = list(input())
        if len(guess)!=4:
            continue    
        res = ""
        for h, g in zip(hidden, guess):
           #print(h, g)
           if h == g:
              res += "b"
           elif g in hidden:
              res += "w"
           #print(res)
        if res=='bbbb':
           print("Congrats!") 
           break   
        print(''.join(sorted(res)))


if __name__ == "__main__":
    main() 
