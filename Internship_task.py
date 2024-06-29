def print_honeycomb(rows, cols):
    hex_top = " ___ "
    hex_mid1 = "/   \\"
    hex_bot = "\\___/"

    for r in range(rows):
       
        if r % 2 == 0:
            print("" + (hex_top * cols))
        else:
            print("" + (hex_top * (cols)))

       
        if r % 2 == 0:
            print("" + (hex_mid1 * cols))
        else:
            print("" + (hex_mid1 * (cols)))

    
        if r % 2 == 0:
            print("" + (hex_bot * cols))
        else:
            print("" + (hex_bot * (cols)))


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))


print_honeycomb(rows, cols)