from tkinter import *
def miles_to_km():
    miles = float(miles_input.get())
    km = miles*1.609
    km_result_lable.config(text=f"{km}")

window =Tk()
window.title("miles to km converter")

miles_input=Entry(width=8)
miles_input.grid(column= 1,row=0 )



miles_lable=Label(text="miles")
miles_lable.grid(column= 2,row= 0)


is_equal_lable=Label(text="is equal to")
is_equal_lable.grid(column= 0,row= 1)

km_result_lable=Label(text="0")
km_result_lable.grid(column=1,row=1 )

km_lable =Label(text="km")
km_lable.grid(column= 2,row=1)

calculate_button = Button(text="calculate" , command=miles_to_km)
calculate_button.grid(column= 1,row=2)













window.mainloop()