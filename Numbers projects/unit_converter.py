import tkinter as tk
from tkinter import ttk, messagebox

# Conversion factors
conversion_factors = {
    "Length": {
        "Meter": 1.0,
        "Kilometer": 0.001,
        "Centimeter": 100.0,
        "Millimeter": 1000.0,
        "Inch": 39.3701,
        "Foot": 3.28084,
        "Yard": 1.09361,
        "Mile": 0.000621371
    },
    "Weight": {
        "Kilogram": 1.0,
        "Gram": 1000.0,
        "Milligram": 1e6,
        "Pound": 2.20462,
        "Ounce": 35.274
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K"
    }
}


# Conversion functions
def convert_units():
    try:
        category = category_combo.get()
        from_unit = from_combo.get()
        to_unit = to_combo.get()
        value = float(entry_value.get())

        if category == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        else:
            base_value = value / conversion_factors[category][from_unit]
            result = base_value * conversion_factors[category][to_unit]

        label_result.config(text=f"Result: {result:.4f} {to_unit}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert from input unit to Celsius
    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:
        celsius = value

    # Convert from Celsius to target unit
    if to_unit == "Fahrenheit":
        return (celsius * 9 / 5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    else:
        return celsius


def update_units(event):
    selected_category = category_combo.get()
    units = list(conversion_factors[selected_category].keys())
    from_combo['values'] = units
    to_combo['values'] = units
    from_combo.current(0)
    to_combo.current(1)


# Tkinter UI setup
root = tk.Tk()
root.title("Unit Converter Tool")
root.geometry("800x700")
root.resizable(True, True)

tk.Label(root, text="Unit Converter", font=("Arial", 16, "bold")).pack(pady=10)

frame = ttk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Select Category:").grid(row=0, column=0, padx=5, pady=5)
category_combo = ttk.Combobox(frame, values=list(conversion_factors.keys()), state="readonly")
category_combo.grid(row=0, column=1, padx=5, pady=5)
category_combo.bind("<<ComboboxSelected>>", update_units)

tk.Label(frame, text="From Unit:").grid(row=1, column=0, padx=5, pady=5)
from_combo = ttk.Combobox(frame, state="readonly")
from_combo.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="To Unit:").grid(row=2, column=0, padx=5, pady=5)
to_combo = ttk.Combobox(frame, state="readonly")
to_combo.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Enter Value:").grid(row=3, column=0, padx=5, pady=5)
entry_value = ttk.Entry(frame)
entry_value.grid(row=3, column=1, padx=5, pady=5)

convert_button = ttk.Button(root, text="Convert", command=convert_units)
convert_button.pack(pady=10)

label_result = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

root.mainloop()
