"""In this program, two numbers will be given in string format. You 
have to multiply them using school methods"""
def stringMultiply(num1, num2):
    if ((num1[0] == "-" and num2[0] == "-") or (num1[0] != "-" and num2[0] != "-")):
        sign = "-"
    else:
        sign = ""
    num1.strip("_")
    num2.strip("-")
    