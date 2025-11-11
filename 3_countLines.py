fname = input("enter filename:")
try:
    with open(fname, 'r') as f1:
        lines = f1.readlines()
        print(len(lines))

except FileNotFoundError:
    print("file not found")
except Exception as e:
    print("error:",e)
