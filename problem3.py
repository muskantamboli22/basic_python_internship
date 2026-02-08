import numpy as np

def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements of {name} row-wise:")

    elements = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            raise ValueError("Number of columns does not match!")
        elements.append(row)

    return np.array(elements)


def display_matrix(title, matrix):
    print(f"\n{title}")
    print("-" * len(title))
    print(matrix)


def main():
    print("\n===== MATRIX OPERATIONS TOOL =====")

    try:
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")

        while True:
            print("\nChoose Operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Transpose")
            print("5. Determinant")
            print("6. Exit")

            choice = input("Enter choice (1-6): ")

            if choice == "1":
                display_matrix("A + B", A + B)

            elif choice == "2":
                display_matrix("A - B", A - B)

            elif choice == "3":
                display_matrix("A x B", np.dot(A, B))

            elif choice == "4":
                display_matrix("Transpose of A", A.T)
                display_matrix("Transpose of B", B.T)

            elif choice == "5":
                if A.shape[0] == A.shape[1]:
                    print(f"\nDeterminant of A: {np.linalg.det(A)}")
                else:
                    print("Determinant not possible for non-square matrix A")

                if B.shape[0] == B.shape[1]:
                    print(f"Determinant of B: {np.linalg.det(B)}")
                else:
                    print("Determinant not possible for non-square matrix B")

            elif choice == "6":
                print("\nExiting Matrix Tool. Thank you!")
                break

            else:
                print("Invalid choice. Try again!")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
