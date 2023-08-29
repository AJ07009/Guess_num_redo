from random import randint; 

def rando(): 
    x = 4
    y = []

    while x > 0:
        rand = randint(0,9)
        y.append(rand)
        x = x - 1

    return y

# result = rando()
# print(result)


def run_game():
    num = "".join(map(str, rando()))

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    
    life_counter = 12
    
    while life_counter > 0:
        try:
            user_input = input("Input 4-digit code: ").strip()

            if len(user_input) != 4 or not user_input.isdigit() or not all(1 <= int(digit) <= 9 
                                                                           for digit in user_input):
                print("Please enter exactly 4 digits within the range of 1 to 8.")
                continue

            counter1 = sum(1 for a, b in zip(num, user_input) 
                           if a == b)
            
            counter2 = sum(min(user_input.count(digit), num.count(digit)) 
                           for digit in set(user_input)) - counter1

            if user_input == num:
                print("Congratulations! You are a codebreaker!")
                print("The code was:", num)
                break
            else:
                print("Number of correct digits in correct place:", counter1)
                print("Number of correct digits not in correct place:", counter2)
                life_counter -= 1
                print(f"Turns left: {life_counter}")
        
        except Exception as e:
            print("Invalid input:", e)

    if life_counter == 0:
        print("The code was:", num)

if __name__ == "__main__":
    run_game()
    
