import streamlit as st
import functions15

todos = functions15.read_todo()

def add_todo():
    todo1 = st.session_state["new_todo"] + "\n"
    todos.append(todo1)
    functions15.write_todo(todos)


st.title("MY TODO APP")
st.subheader("This is my to-do app.")
st.write("This app is to increase my productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions15.write_todo(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a to do:",
              placeholder="Add a to-do",
              on_change=add_todo,
              key="new_todo")

