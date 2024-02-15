def main():
    num1=float(input("enter the 1st floating value:"))
    num2=float(input("enter the 2nd floating value:"))
    result = num1/num2
    print("Result in scientific notation (2 decimal): {:.2e}".format(result))
if __name__=="__main__":
    main()