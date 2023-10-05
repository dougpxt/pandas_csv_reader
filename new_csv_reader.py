#####################
from tkinter import *
from tkinter import filedialog, ttk
#
import pandas as pd
##########
root = Tk()
root.geometry('640x480')
root.title("")
root.tk_setPalette(background='#333', foreground='white')
############################################################################
widget_frame = LabelFrame(root, text = 'PANDAS CSV READER', padx=10, pady=10)
#
image = PhotoImage(file='panda_icon.png')
image_label = Label(widget_frame, image=image)
#
treeview_frame = Frame(widget_frame, pady=10)
treeview = ttk.Treeview(treeview_frame,show='headings')
#
input_frame = Frame(widget_frame)
file_input = Entry(input_frame)
buttons_frame = Frame(widget_frame, padx=100)
browse_button = Button(buttons_frame, text="Browse", command=lambda: browse_file())
submit_button = Button(buttons_frame, text="Submit", command=lambda: submit())
#
text_variable = StringVar()
shape_label = Label(widget_frame, textvariable=text_variable)
########################################
widget_frame.pack(expand=True, fill=BOTH)
#
image_label.pack(fill=BOTH)
#
treeview_frame.pack(expand=True, fill=BOTH)
treeview.place(relheight=1, relwidth=1)
treescrollx = Scrollbar(treeview_frame, orient='horizontal', command=treeview.xview)
treescrolly = Scrollbar(treeview_frame, orient='vertical', command=treeview.yview)
treeview.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side='bottom', fill='x')
treescrolly.pack(side='right', fill='y')
#
input_frame.pack(side='left', expand=True, fill=BOTH)
file_input.pack(side='left', expand=True, fill=BOTH)
buttons_frame.pack(side='left')
browse_button.pack(side='left')
submit_button.pack(side='left')
#
shape_label.pack()
#################
def browse_file():
    global file
    file = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    file_input.delete(0, END)  # Clear any previous text in the entry
    file_input.insert(0, file)
 #   
def submit():
    selected_items = treeview.get_children()
    for item in selected_items:
        treeview.delete(item)
    #
    indexation = ['ID', 'id', 'index', 'indice', 'key', 'chave']
    found = False
    for index in indexation:
        if index in pd.read_csv(file).columns:
            df = pd.read_csv(file, index_col=index, encoding='utf-8')
            found = True
        if not found:
            df = pd.read_csv(file, encoding='utf-8')
    total_qtd = df.shape[0]
    #
    treeview['column'] = list(df.columns)
    for column in treeview['column']:
        treeview.heading(column, text=column)
    #
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        treeview.insert('', 'end', values=row)
    text_variable.set(f'TOTAL ROWS: {total_qtd}')
##############
root.mainloop() 