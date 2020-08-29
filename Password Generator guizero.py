import pyperclip
from guizero import *
from string import *
from random import shuffle, choice


# Function for generating a password
def gen_pwd(pwd_length, lower, upper, numbers, specials, pwd_txt):

    length = pwd_length.value   # Get the value from slider for password length

    lowercase = ascii_lowercase

    uppercase = ascii_uppercase

    nums = digits

    specs = punctuation

    new_passwd = ""

    pwd_type = 0    # Set a password type to 0

    # If checkbox(es) for lowercase, uppercase, numbers and special characters are checked
    if lower.value == 1 and upper.value == 0 and numbers.value == 0 and specials.value == 0:
        pwd_type = 1
    elif lower.value == 1 and upper.value == 1 and numbers.value == 0 and specials.value == 0:
        pwd_type = 2
    elif lower.value == 1 and upper.value == 1 and numbers.value == 1 and specials.value == 0:
        pwd_type = 3
    elif lower.value == 1 and upper.value == 1 and numbers.value == 1 and specials.value == 1:
        pwd_type = 4
    elif lower.value == 1 and upper.value == 1 and numbers.value == 1 and specials.value == 0:
        pwd_type = 5
    elif lower.value == 0 and upper.value == 0 and numbers.value == 1 and specials.value == 0:
        pwd_type = 6
    else:
        print("Error")

    # Generate a password with lowercase
    if pwd_type == 1:
        for i in range(0, length):
            new_passwd += choice(lowercase)
        pass_word = list(new_passwd)
        shuffle(pass_word)
        new_pass = "".join(pass_word)

        passwd1 = new_pass

        new_passwd = passwd1

        pwd_txt.append(new_passwd)

    # Generate a password with lower and uppercase
    elif pwd_type == 2:
        for x in range(0, length):
            new_passwd += choice(lowercase + uppercase)
        pass_word = list(new_passwd)
        shuffle(pass_word)
        new_pass = "".join(pass_word)

        passwd1 = new_pass

        new_passwd = passwd1

        pwd_txt.append(new_passwd)

    # Generate a password with lowercase, uppercase and numbers
    elif pwd_type == 3:
        for y in range(0, length):
            new_passwd += choice(lowercase + uppercase + nums)
        pass_word = list(new_passwd)
        shuffle(pass_word)
        new_pass = "".join(pass_word)

        passwd1 = new_pass

        new_passwd = passwd1

        pwd_txt.append(new_passwd)

    # Generate a password with lowercase, uppercase, numbers and special characters
    elif pwd_type == 4:
        for z in range(0, length):
            new_passwd += choice(lowercase + uppercase + nums + specs)
        pass_word = list(new_passwd)
        shuffle(pass_word)
        new_pass = "".join(pass_word)

        passwd1 = new_pass

        new_passwd = passwd1

        pwd_txt.append(new_passwd)

    # Generate a password with numbers for PIN number
    elif pwd_type == 5:
        for n in range(0, length):
            new_passwd += choice(nums)
        pass_word = list(new_passwd)
        shuffle(pass_word)
        new_pass = "".join(pass_word)

        passwd1 = new_pass

        new_passwd = passwd1

        pwd_txt.append(new_passwd)

    # Generate a password with lowercase, uppercase and special characters
    elif pwd_type == 6:
        for s in range(0, length):
            new_passwd += choice(lowercase + uppercase + specs)
        pass_word = list(new_passwd)
        shuffle(pass_word)
        new_pass = "".join(pass_word)

        passwd1 = new_pass

        new_passwd = passwd1

        pwd_txt.append(new_passwd)
    else:
        print("Error")


# Function for copying a password into a clipboard
def copy_pwd(app):

    pwd_txt = TextBox(app, grid=[1, 6])
    pwd_txt.width = 30
    pwd_txt.bg = "White"

    cp_pwd = pwd_txt.value

    pyperclip.copy(cp_pwd)

    pwd_txt.clear()


def show_pwd(app, show_btn):

    if show_btn.text == "Show":
        pwd_txt = TextBox(app, grid=[1, 6])
        pwd_txt.width = 30
        pwd_txt.bg = "White"
    else:
        show_btn.text = "Hide"
        pwd_txt = TextBox(app, grid=[1, 6], hide_text=True)
        pwd_txt.width = 30
        pwd_txt.bg = "White"


# Entry point of the program and displays an app
def main():

    app = App(title="Password Generator", height=350, width=750, bg='Gray', layout="grid")

    Text(app, text="Password Generator", size=20, grid=[3, 0])

    # Set up checkbox options for lowercase, uppercase, numbers and special characters
    lower = CheckBox(app, text="Lowercase", grid=[0, 2])
    lower.text_size = 12
    lower.text_color = "Black"
    upper = CheckBox(app, text="Uppercase", grid=[1, 2])
    upper.text_size = 12
    upper.text_color = "Black"
    numbers = CheckBox(app, text="Numbers", grid=[2, 2])
    numbers.text_size = 12
    numbers.text_color = "Black"
    specials = CheckBox(app, text="Special Characters", grid=[3, 2])
    specials.text_size = 12
    specials.text_color = "Black"

    # Set up a slider for password length
    Text(app, text="Password Length", grid=[0, 4], size=14)
    pwd_length = Slider(app, start=5, end=100, grid=[1, 4])
    pwd_length.bg = "Gray"
    pwd_length.width = 150

    # Set up a textbox for display a generated password
    Text(app, text="New Password", grid=[0, 6], size=14)
    pwd_txt = TextBox(app, grid=[1, 6], hide_text=True)
    pwd_txt.width = 30
    pwd_txt.bg = "White"

    # Set up PushButtons for generate and copy a password and exiting a program
    gen_btn = PushButton(app, text="Generate", command=gen_pwd,
                         args=[pwd_length, lower, upper, numbers, specials, pwd_txt], grid=[0, 7])
    gen_btn.bg = 'White'
    gen_btn.width = 5
    gen_btn.text_size = 10
    gen_btn.text_color = 'Black'
    copy_btn = PushButton(app, text="Copy", command=copy_pwd, args=[app], grid=[0, 8])
    copy_btn.bg = 'White'
    copy_btn.width = 5
    copy_btn.text_size = 10
    copy_btn.text_color = 'Black'
    show_btn = PushButton(app, text="Show", command=show_pwd, args=[app], grid=[1, 8])
    show_btn.update_command(show_pwd, args=(app, show_btn))
    show_btn.bg = 'White'
    show_btn.width = 5
    show_btn.text_size = 10
    show_btn.text_color = 'Black'
    exit_btn = PushButton(app, text="Exit", command=exit, grid=[1, 7])
    exit_btn.bg = 'white'
    exit_btn.width = 5
    exit_btn.text_size = 10
    exit_btn.text_color = 'Black'

    app.display()


# The following if statement helps Python determine whether or not the main()
# function in this program is our entry point
if __name__ == "__main__":
    main()
