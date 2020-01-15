def main():
    print("Hello")

    a = 10
    b = 20
    sum = a + b
    print("sum is:", sum);

    # whatever we write in our program is by default part of main
    print(__name__)  # main

# you have to execute main yourself now
if __name__ == "__main__":
    main()