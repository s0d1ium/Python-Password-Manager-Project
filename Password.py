class PasswordFunction:

    def Password():

        attempts = 0
        hash = "test"
        ACCESS = False

        Input = input("Enter Password: ")

        while ACCESS == False:

            if Input != hash:
                print("Incorrect Password")
                attempts += 1
                print(attempts)
                if attempts == 3:
                    print("Password attempt limit exceeded")
                    exit()
                Input = input("Enter Password: ")
            else:
                ACCESS = True

        print("SUCCESS")
        exit()

PasswordFunction.Password()