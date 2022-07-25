'''in'''
def main():
    '''out'''
    gpa = float(input())
    if gpa < 1.00:
        print("I'm so sad.")
    elif gpa < 2.00:
        gpa = 4 - gpa
        print("%.2f" %gpa)
    else:
        print("I'm so happy.")
main()
