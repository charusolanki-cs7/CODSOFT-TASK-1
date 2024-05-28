#A To-Do List application is a useful project that helps users manage and organize their tasks efficiently.
#This project aims to create a command-line or GUI-based application using Python, allowingusers to create, update, and track their to-do lists
  
import tkinter as tk                      
from tkinter import ttk                  
from tkinter import messagebox           
import sqlite3 as sql                     
  
def add_task():
    task_string = task_field.get()   
    if len(task_string) == 0:    
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        # adding the string to the tasks list  
        tasks.append(task_string)  
        the_cursor.execute('insert into tasks values (?)', (task_string ,))  
        # calling the function to update the list  
        list_update()  
        # deleting the entry in the entry field  
        task_field.delete(0, 'end')  
  
def list_update():  
    clear_list()  
    for task in tasks:  
        task_listbox.insert('end', task)  
def delete_task():  
    # using the try-except method  
    try:  
        # getting the selected entry from the list box  
        the_value = task_listbox.get(task_listbox.curselection())  
        # checking if the stored value is present in the tasks list  
        if the_value in tasks:  
            # removing the task from the list  
            tasks.remove(the_value)  
            # calling the function to update the list  
            list_update()  
            # using the execute() method to execute a SQL statement  
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
          
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')     
def delete_all_tasks():  
     
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    # if the value turns to be True  
    if message_box == True:  
          
        while(len(tasks) != 0):  
            # using the pop() method to pop out the elements from the list  
            tasks.pop()  
          
        the_cursor.execute('delete from tasks')  
         
        list_update()  
def clear_list():  
     task_listbox.delete(0, 'end')  
def close():
    print(tasks)  
    guiWindow.destroy()
def retrieve_database():  
     
    while(len(tasks) != 0):  
        # using the pop() method to pop out the elements from the list  
        tasks.pop()  
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])  
  
# main function  
if __name__ == "__main__":  
     
    guiWindow = tk.Tk()  
    guiWindow.title("To-Do List Manager - JAVATPOINT")   
    guiWindow.geometry("500x450+750+250")  
    guiWindow.resizable(0, 0)    
    guiWindow.configure(bg = "#FAA0A0")  
  
      
    the_connection = sql.connect('listOfTasks.db')    
    the_cursor = the_connection.cursor()  
    the_cursor.execute('create table if not exists tasks (title text)')  
  
    tasks = []  
    header_frame = tk.Frame(guiWindow, bg = "#FAA0A0")  
    functions_frame = tk.Frame(guiWindow, bg = "#FAA0A0")  
    listbox_frame = tk.Frame(guiWindow, bg = "#FAA0A0")  
  
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
      
    header_label = ttk.Label(  
        header_frame,  
        text = "The To-Do List",  
        font = ("Brush Script MT", "30"),  
        background = "#FAA0A0",  
        foreground = "#8B4513"  
    )  
      
    header_label.pack(padx = 20, pady = 20)  
  
      
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Consolas", "11", "bold"),  
        background = "#FAA0A0",  
        foreground = "#000000"  
    )  
     
    task_label.place(x = 30, y = 40)  
      
    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 18,  
        background = "#FFF8DC",  
        foreground = "#A52A2A"  
    )  
    task_field.place(x = 30, y = 80)  
   # adding buttons to the application using the ttk.Button() widget  
    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",  
        width = 24,  
        command = add_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,  
        command = delete_all_tasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    )  
     
    add_button.place(x = 30, y = 120)  
    del_button.place(x = 30, y = 160)  
    del_all_button.place(x = 30, y = 200)  
    exit_button.place(x = 30, y = 240)  
  
    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 26,  
        height = 13,  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#CD853F",  
        selectforeground = "#FFFFFF"  
    )  
    task_listbox.place(x = 10, y = 20)  
    retrieve_database()  
    list_update()  
    # using the mainloop() method to run the application  
    guiWindow.mainloop()  
    # establishing the connection with database  
    the_connection.commit()  
    the_cursor.close()  
