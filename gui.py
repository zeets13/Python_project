import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import customtkinter as ctk
from customtkinter import * 
from PIL import Image, ImageTk 

model = joblib.load("heart_disease_model.pkl")

def predict():
    try:
        inputs = [
            int(age_entry.get()),
            sex_var.get(),
            cp_var.get(),
            int(bp_entry.get()),
            int(chol_entry.get()),
            fbs_var.get(),
            restecg_var.get(),
            int(hr_entry.get()),
            exang_var.get(),
            float(oldpeak_entry.get()),
            slope_var.get(),
            ca_var.get(),
            thal_var.get()
        ]

        prediction = model.predict([inputs])[0]

        if prediction == 1:
            messagebox.showerror("Prediction Result", "⚠️ High Risk of Heart Disease! Consult a doctor.")
        else:
            messagebox.showinfo("Prediction Result", "✅ Low Risk of Heart Disease. Stay healthy!")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values!")

root = tk.Tk()
root.title("Heart Disease Predictor")
root.geometry("800x800")

bg_image = Image.open("final.jpg")  
bg_image = bg_image.resize((1600, 800))  
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TEntry", font=("Arial", 12))


title_label = CTkLabel(root, text="Predict & Prevent Disease!", 
                       font=("Verdana", 32), 
                       text_color="#331D2C", 
                       fg_color="transparent")
title_label.pack(pady=(50))

frame = ttk.Frame(root,width=700, height=900, padding=10, )
frame.pack_propagate(False)
frame.place(relx=0.5, rely=0.5, anchor="center")  

labels = ["Age", "Resting BP", "Cholesterol", "Max Heart Rate", "ST Depression"]
entries = []
for i, label in enumerate(labels):
    tk.Label(frame, text=label, font=("Verdana", 12), bg="#f0f0f0").grid(row=i, column=0, sticky='w',padx=15, pady=5)
    entry = ttk.Entry(frame)
    entry.grid(row=i, column=1, pady=5)
    entries.append(entry)

age_entry, bp_entry, chol_entry, hr_entry, oldpeak_entry = entries

sex_var = tk.IntVar()
tk.Label(frame, text="Sex", font=("Verdana", 12), bg="#f0f0f0").grid(row=5, column=0, sticky='w', padx=15,pady=5)
ttk.Radiobutton(frame, text="Male", variable=sex_var, value=1).grid(row=5, column=1)
ttk.Radiobutton(frame, text="Female", variable=sex_var, value=0).grid(row=5, column=2)

cp_var = tk.IntVar()
tk.Label(frame, text="Chest Pain Type", font=("Verdana", 12), bg="#f0f0f0").grid(row=6, column=0, sticky='w',padx=15, pady=5)
ttk.Combobox(frame, textvariable=cp_var, values=[0, 1, 2, 3], width=5).grid(row=6, column=1)

fbs_var = tk.IntVar()
tk.Label(frame, text="Fasting Blood Sugar > 120", font=("Verdana", 12), bg="#f0f0f0").grid(row=7, column=0, sticky='w', padx=15,pady=5)
ttk.Combobox(frame, textvariable=fbs_var, values=[0, 1], width=5).grid(row=7, column=1)

restecg_var = tk.IntVar()
tk.Label(frame, text="Resting ECG", font=("Verdana", 12), bg="#f0f0f0").grid(row=8, column=0, sticky='w', padx=15,pady=5)
ttk.Combobox(frame, textvariable=restecg_var, values=[0, 1, 2], width=5).grid(row=8, column=1)

exang_var = tk.IntVar()
tk.Label(frame, text="Exercise Angina", font=("Verdana", 12), bg="#f0f0f0").grid(row=9, column=0, sticky='w', padx=15,pady=5)
ttk.Combobox(frame, textvariable=exang_var, values=[0, 1], width=5).grid(row=9, column=1)

slope_var = tk.IntVar()
tk.Label(frame, text="Slope", font=("Verdana", 12), bg="#f0f0f0").grid(row=10, column=0, sticky='w', padx=15,pady=5)
ttk.Combobox(frame, textvariable=slope_var, values=[0, 1, 2], width=5).grid(row=10, column=1)

ca_var = tk.IntVar()
tk.Label(frame, text="Major Vessels", font=("Verdana", 12), bg="#f0f0f0").grid(row=11, column=0, sticky='w',padx=15, pady=5)
ttk.Combobox(frame, textvariable=ca_var, values=[0, 1, 2, 3], width=5).grid(row=11, column=1)

thal_var = tk.IntVar()
tk.Label(frame, text="Thalassemia", font=("Verdana", 12), bg="#f0f0f0").grid(row=12, column=0, sticky='w',padx=15, pady=5)
ttk.Combobox(frame, textvariable=thal_var, values=[0, 1, 2, 3], width=5).grid(row=12, column=1)

btn= CTkButton(frame, text="Predict", command=predict, corner_radius=30,fg_color="#432E54",hover_color="black",text_color="white").grid(row=13, columnspan=2, padx=15, pady=20)


root.mainloop()
