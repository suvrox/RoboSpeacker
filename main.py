import os

if __name__ == '__main__':
    print("Welcome to robo specker created by Suvradip")
    while True:
        x = input("Enter what you want to speak: ")
        if x == "q":
            os.system("say 'bye bye friend'")
            break
        command = f"say {x}"
        os.system(command)

