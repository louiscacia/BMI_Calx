#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 19:58:03 2024

@author: louiscacia
"""

import tkinter as tk

def calculate_bmi():
    
    try: 
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        
        if use_us.get():
            
            height *= 0.3048 # Convert meters to feet 
            weight *= 0.453592 # Convert kilograms to pounds
           
        if height <= 0 or weight <= 0:
            result_label.config(text="Height or weight below physical limit")
            
        else: 
            
            bmi = weight / (height ** 2)
            result_label.config(text=f"BMI: {bmi:.2f}")
     
    except:
        
        result_label.config(text="not a vaild entry")
        
def update_labels():
    if use_us.get():
        height_label.config(text="Height (ft):")
        weight_label.config(text="Weight (lbs):")
    else:
        height_label.config(text="Height (m):")
        weight_label.config(text="Weight (kg):")



root = tk.Tk()
root.title("BMI Calculator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

use_us = tk.BooleanVar()
use_us.set(False)

us_checkbutton = tk.Checkbutton(frame, text="Imperial System", variable=use_us, command=update_labels)
us_checkbutton.grid(row=2, columnspan=2)


height_label = tk.Label(frame, text="Height (m):")
height_label.grid(row=0, column=0, sticky="e")
    
height_entry = tk.Entry(frame)
height_entry.grid(row=0, column=1)
    
weight_label = tk.Label(frame, text="Weight (kg):")
weight_label.grid(row=1, column=0, sticky="e")
    
weight_entry = tk.Entry(frame)
weight_entry.grid(row=1, column=1)

        
    
calculate_button = tk.Button(frame, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=3, columnspan=2)

result_label = tk.Label(frame, text="")
result_label.grid(row=4, columnspan=2)

root.mainloop()
