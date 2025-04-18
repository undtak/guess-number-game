#猜數字遊戲

secret_num = 45
guess = None
guess_count = 0
guess_limit = 5
out_of_limit = False

while secret_num != guess and not(out_of_limit):
    guess_count+=1
    if guess_count<=guess_limit:
        guess = int(input("guess num:"))
        if guess>secret_num:
            print("smaller")
        elif guess<secret_num:
            print("bigger")
    else:
        out_of_limit=True
if out_of_limit:
    print("you lose")
else:
    print("you win")