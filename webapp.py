import streamlit as st
import functions

todos = functions.get_todos()



def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''  # Clear the input box after pressing Enter
    print(todo)




st.title('My todo app,this is title')
st.subheader('this is my todo app, this is subheader')
st.write('this is the write method')
st.write('This page is hosted locally')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
print(todos)

st.text_input(label='enter todo... todo is making me puke', placeholder='i\'m placeholder', on_change=add_todo,\
               key='new_todo')


st.session_state