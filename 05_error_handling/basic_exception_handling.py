try:
    print(12/1)
except ZeroDivisionError as e:
    print(f"Error Occur Occurred: {e}")
else:
    print('All is well here')
finally:
    print("No Matter what, I'wll Execute!!")