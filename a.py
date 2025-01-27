def outer_function():
    count = 0  # Local variable in the enclosing scope (outer_function)

    def inner_function():
        nonlocal count

        count += 1  # Trying to modify 'count' from the enclosing scope
        print(count)

    inner_function()
    inner_function()
    inner_function()  # Call the inner function

outer_function()
outer_function()
