def rgb_hex():
    invalid_msg = "Uneta vrednost je invalidna."

    red = int(raw_input("Unesite vrednost za crvenu(R): "))
    if red < 0 or red > 255:
        print invalid_msg
        return
    green = int(raw_input("Unesite vrednost za zelenu(G): "))
    if green < 0 or green > 255:
        print invalid_msg
        return
    
    blue = int(raw_input("Unesite vrednost za plavu(B): "))
    if blue < 0 or blue > 255:
        print invalid_msg
        return

    val = red << 16 + green << 8 + blue
    print "%s" % (hex(val)[2:]).upper()

def hex_rgb():
    hex_val = raw_input("Unesite boju(6 heksadecimalnih cifara): ")
    invalid_msg = "Invalidna heksadecimalna vrednost."
    if len(hex_val) != 6:
        print invalid_msg
        return
    else:
        hex_val = int(hex_val, 16)
    two_hex_digits = 2 ** 8
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    red = hex_val % two_hex_digits
    print "Crvena: %s Zelena: %s Plava: %s" % red, gree, blue

def convert():
    while True:
        option = raw_input("Unesite 1 za konverziju iz RGB u HEX. Unesite 2 za konverziju HEX u RGB. Unesite X za izlazak:")
        if option == "1":
            print "RGB u HEX..."
            rgb_hex()
        elif option == "2":
            print "HEX u RGB..."
            hex_rgb()
        elif option == "X" or option == "x":
            break
        else:
            print "Pogresna komanda."
convert()
