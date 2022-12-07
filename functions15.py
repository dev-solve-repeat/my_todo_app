"""The variables having some constant values are written in the top of the module,
and they are written in caps"""
FILEPATH = "todoList.txt"
def read_todo(filepath=FILEPATH):
    """This function reads the text file and returns it to a variable. In this case a list."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_arg, filepath = FILEPATH): #gives syntax error, non default parameter following default parameter
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello from functions")
