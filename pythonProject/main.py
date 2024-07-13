import streamlit as st
from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

def calculate(num1, num2, operator):
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        result = "Invalid operator"
    return result

def main():
    st.title('Saawan Ashraf Calculator')  # Setting custom title

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    operator = st.selectbox("Select operator", ['+', '-', '*', '/'])

    if st.button("Calculate"):
        result = calculate(num1, num2, operator)
        st.success(f"Result: {result}")

    quit_choice = st.radio("Do you want to quit the calculator?", ('No', 'Yes'))
    if quit_choice == 'Yes':
        st.write("Goodbye!")
    else:
        st.write("Continue using the calculator.")

if __name__ == "__main__":
    main()
