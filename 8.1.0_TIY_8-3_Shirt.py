def make_shirt(size, print_front='nothing', print_back='nothing'):
    print(f"\nSize of shirt is {size}.\nPrint {print_front.upper()} frontside.\nPrint {print_back.upper()} backside.\n")

make_shirt(size='32',print_front='man')
make_shirt(32, 'hola', 'bag')