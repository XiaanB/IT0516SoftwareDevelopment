def show_hello(param):
    print("Hello there, the number of times this"
          " function is called is {0}!!.".format(param))


counter = 0
print("testing my second user defined function.")

counter += 1
show_hello(counter)

counter += 1
show_hello(counter)

