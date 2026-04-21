import tkinter as tk
from tkinter import ttk, messagebox
from geometry_lib import solids, physics, exporter

def run():
    try:
        shape = cb_shape.get()
        material = cb_mat.get()
        a = float(ent_a.get())
        
        if shape == "Параллелепипед":
            b = float(ent_b.get()) if ent_b.get() else a
            c = float(ent_c.get()) if ent_c.get() else a
            vol, area = solids.calc_geom(shape, a, b, c)
        else:
            vol, area = solids.calc_geom(shape, a)
        
        mass = physics.get_mass(vol, material)
        
        res = f"Фигура: {shape}\nОбъём: {vol:.2f} м³\nПлощадь: {area:.2f} м²\nМасса: {mass:.2f} кг"
        lbl_res.config(text=res)
        
        global last_data
        last_data = res
        
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа!")

def show_parallelipiped_fields():
    """Показывает поля для длины, ширины, высоты"""
    lbl_b.pack()
    ent_b.pack()
    lbl_c.pack()
    ent_c.pack()

def hide_parallelipiped_fields():
    """Скрывает поля для ширины и высоты"""
    lbl_b.pack_forget()
    ent_b.pack_forget()
    lbl_c.pack_forget()
    ent_c.pack_forget()

def on_shape_change(*args):
    shape = cb_shape.get()
    if shape == "Параллелепипед":
        lbl_a.config(text="Длина (м):")
        show_parallelipiped_fields()
    elif shape == "Шар":
        lbl_a.config(text="Радиус (м):")
        hide_parallelipiped_fields()
    else:  # Тетраэдр
        lbl_a.config(text="Ребро (м):")
        hide_parallelipiped_fields()

# GUI
root = tk.Tk()
root.title("Калькулятор геометрических тел")
root.geometry("350x450")

last_data = None

tk.Label(root, text="ГЕОМЕТРИЧЕСКИЙ КАЛЬКУЛЯТОР", font=("Arial", 12, "bold")).pack(pady=10)

# Выбор фигуры (теперь Combobox, а не Entry)
tk.Label(root, text="Выберите фигуру:").pack()
cb_shape = ttk.Combobox(root, values=["Шар", "Тетраэдр", "Параллелепипед"], state="readonly")
cb_shape.pack()
cb_shape.bind("<<ComboboxSelected>>", on_shape_change)
cb_shape.set("Шар")

# Параметры
tk.Label(root, text="Параметры фигуры:").pack(pady=(10, 0))
lbl_a = tk.Label(root, text="Радиус (м):")
lbl_a.pack()
ent_a = tk.Entry(root)
ent_a.pack()

# Поля для параллелепипеда (скрыты по умолчанию)
lbl_b = tk.Label(root, text="Ширина (м):")
ent_b = tk.Entry(root)
lbl_c = tk.Label(root, text="Высота (м):")
ent_c = tk.Entry(root)

# Выбор материала
tk.Label(root, text="Выберите материал:").pack(pady=(10, 0))
cb_mat = ttk.Combobox(root, values=["Сталь", "Алюминий", "Медь", "Дерево", "Бетон", "Пластик"], state="readonly")
cb_mat.pack()
cb_mat.set("Сталь")

# Кнопка расчёта
tk.Button(root, text="РАССЧИТАТЬ", command=run, bg="green", fg="white").pack(pady=15)

# Результат
lbl_res = tk.Label(root, text="Результат", font=("Arial", 10), justify="left", bg="lightgray", relief="sunken")
lbl_res.pack(fill="both", padx=20, pady=10, ipady=10)

# Кнопки сохранения
tk.Button(root, text="Сохранить в DOC", command=lambda: exporter.save_data(last_data, "doc")).pack(pady=5)
tk.Button(root, text="Сохранить в XLS", command=lambda: exporter.save_data(last_data, "xls")).pack()

root.mainloop()