"""
Pattern Printing Programs
Convert various patterns using loops
"""

def pattern1_square():
    """Pattern 1: Square of stars (5x5)"""
    print("Pattern 1: Square")
    n = 5
    
    for i in range(n):
        bag = ""
        for j in range(n):
            bag += "* "
        print(bag.strip())
    print()


def pattern2_descending_triangle():
    """Pattern 2: Descending right triangle"""
    print("Pattern 2: Descending Triangle")
    n = 4
    
    for i in range(n, 0, -1):
        bag = ""
        for j in range(1, i + 1):
            bag += "* "
        print(bag.strip())
    print()


def pattern3_ascending_right_triangle():
    """Pattern 3: Ascending right-aligned triangle"""
    print("Pattern 3: Ascending Right-Aligned Triangle")
    n = 5
    
    for i in range(1, n + 1):
        bag = ""
        
        # leading spaces (to push stars to the right)
        for s in range(1, n - i + 1):
            bag += "  "  # two spaces to match "* "
        
        # stars
        for j in range(1, i + 1):
            bag += "* "
        
        print(bag.rstrip())
    print()


def pattern4_ascending_triangle_compact():
    """Pattern 4: Ascending right-aligned triangle (compact)"""
    print("Pattern 4: Ascending Triangle (Compact)")
    n = 5
    
    for i in range(1, n + 1):
        bag = ""
        
        # leading spaces
        for s in range(1, n - i + 1):
            bag += "  "  # two spaces per missing star
        
        # stars
        for j in range(1, i + 1):
            bag += "*"  # add star
            if j < i:
                bag += " "  # add space only between stars
        
        print(bag)
    print()


def pattern5_number_ascending():
    """Pattern 5: Number ascending triangle"""
    print("Pattern 5: Number Ascending Triangle")
    n = 5
    
    for i in range(1, n + 1):
        bag = ""
        
        for j in range(1, i + 1):
            bag += str(j)  # add the number
            if j < i:
                bag += " "  # space between numbers
        
        print(bag)
    print()


def pattern6_number_descending():
    """Pattern 6: Number descending triangle"""
    print("Pattern 6: Number Descending Triangle")
    n = 5
    
    for i in range(n, 0, -1):
        bag = ""
        
        for j in range(1, i + 1):
            bag += str(j)  # add the number
            if j < i:
                bag += " "  # space between numbers
        
        print(bag)
    print()


def pattern7_binary_alternate_column():
    """Pattern 7: Binary pattern (alternating by column)"""
    print("Pattern 7: Binary Pattern (Alternate by Column)")
    n = 5
    
    for i in range(1, n + 1):
        bag = ""
        
        for j in range(1, i + 1):
            # start every row with 1, then alternate 1,0,1,0,...
            value = 1 if (j % 2 == 1) else 0
            bag += str(value)
            if j < i:
                bag += " "
        
        print(bag)
    print()


def pattern8_binary_alternate_diagonal():
    """Pattern 8: Binary pattern (alternating by diagonal)"""
    print("Pattern 8: Binary Pattern (Alternate by Diagonal)")
    n = 5
    
    for i in range(1, n + 1):
        bag = ""
        
        for j in range(1, i + 1):
            # value depends on (i + j): this matches the second pattern
            value = 1 if ((i + j) % 2 == 0) else 0
            bag += str(value)
            if j < i:
                bag += " "
        
        print(bag)
    print()


def main():
    print("=" * 50)
    print("         PATTERN PRINTING PROGRAMS")
    print("=" * 50)
    print()
    
    pattern1_square()
    pattern2_descending_triangle()
    pattern3_ascending_right_triangle()
    pattern4_ascending_triangle_compact()
    pattern5_number_ascending()
    pattern6_number_descending()
    pattern7_binary_alternate_column()
    pattern8_binary_alternate_diagonal()
    
    print("=" * 50)


if __name__ == "__main__":
    main()
