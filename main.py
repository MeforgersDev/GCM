import tkinter as tk
from tkinter import ttk
import math
import re

class ModernCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GHM - MeforgersDev")
        self.geometry("600x410")
        self.configure(bg="#2d2d2d")

        self.style = ttk.Style(self)
        self.style.configure("TButton",
                             font=("Helvetica", 14),
                             padding=10,
                             foreground="#000000", 
                             background="#333333")
        self.style.map("TButton",
                       background=[("active", "#555555")])

        self.expression = ""
        self.input_text = tk.StringVar()

        # Input field
        input_frame = tk.Frame(self, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2, bg="#2d2d2d")
        input_frame.pack(side=tk.TOP)

        input_field = ttk.Entry(input_frame, font=('Helvetica', 18, 'bold'), textvariable=self.input_text, width=50, foreground="#000000", background="#ffffff", justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        # Button frame
        btns_frame = tk.Frame(self, width=200, height=250, bg="#2d2d2d")
        btns_frame.pack()

        # First row
        ttk.Button(btns_frame, text="C", command=self.clear).grid(row=0, column=0, columnspan=1, sticky="nsew")
        ttk.Button(btns_frame, text="/", command=lambda: self.click("/")).grid(row=0, column=3, sticky="nsew")

        # Second row
        ttk.Button(btns_frame, text="7", command=lambda: self.click("7")).grid(row=1, column=0, sticky="nsew")
        ttk.Button(btns_frame, text="8", command=lambda: self.click("8")).grid(row=1, column=1, sticky="nsew")
        ttk.Button(btns_frame, text="9", command=lambda: self.click("9")).grid(row=1, column=2, sticky="nsew")
        ttk.Button(btns_frame, text="*", command=lambda: self.click("*")).grid(row=1, column=3, sticky="nsew")

        # Third row
        ttk.Button(btns_frame, text="4", command=lambda: self.click("4")).grid(row=2, column=0, sticky="nsew")
        ttk.Button(btns_frame, text="5", command=lambda: self.click("5")).grid(row=2, column=1, sticky="nsew")
        ttk.Button(btns_frame, text="6", command=lambda: self.click("6")).grid(row=2, column=2, sticky="nsew")
        ttk.Button(btns_frame, text="-", command=lambda: self.click("-")).grid(row=2, column=3, sticky="nsew")

        # Fourth row
        ttk.Button(btns_frame, text="1", command=lambda: self.click("1")).grid(row=3, column=0, sticky="nsew")
        ttk.Button(btns_frame, text="2", command=lambda: self.click("2")).grid(row=3, column=1, sticky="nsew")
        ttk.Button(btns_frame, text="3", command=lambda: self.click("3")).grid(row=3, column=2, sticky="nsew")
        ttk.Button(btns_frame, text="+", command=lambda: self.click("+")).grid(row=3, column=3, sticky="nsew")

        # Fifth row
        ttk.Button(btns_frame, text="(", command=lambda: self.click("(")).grid(row=0, column=1, sticky="nsew")
        ttk.Button(btns_frame, text=")", command=lambda: self.click(")")).grid(row=0, column=2, sticky="nsew")
        ttk.Button(btns_frame, text=".", command=lambda: self.click(".")).grid(row=4, column=2, sticky="nsew")
        ttk.Button(btns_frame, text="0", command=lambda: self.click("0")).grid(row=4, column=1, sticky="nsew")
        ttk.Button(btns_frame, text="00", command=lambda: self.click("00")).grid(row=4, column=0, sticky="nsew")
        ttk.Button(btns_frame, text="=", command=self.evaluate).grid(row=4, column=3, sticky="nsew")

        # Additional functions
        ttk.Button(btns_frame, text="√", command=self.sqrt).grid(row=5, column=0, sticky="nsew")
        ttk.Button(btns_frame, text="x²", command=self.pow2).grid(row=5, column=1, sticky="nsew")
        ttk.Button(btns_frame, text="log", command=self.log).grid(row=5, column=2, sticky="nsew")
        ttk.Button(btns_frame, text="sin", command=self.sin).grid(row=5, column=3, sticky="nsew")
        ttk.Button(btns_frame, text="cos", command=self.cos).grid(row=6, column=0, sticky="nsew")
        ttk.Button(btns_frame, text="tan", command=self.tan).grid(row=6, column=1, sticky="nsew")

        # Futuristic functions button
        ttk.Button(btns_frame, text="Fütüristik Hesaplamalar", command=self.toggle_futuristic_panel).grid(row=6, column=2, columnspan=2, sticky="nsew")

        self.futuristic_panel = None

    def toggle_futuristic_panel(self):
        if self.futuristic_panel is None:
            self.futuristic_panel = tk.Toplevel(self)
            self.futuristic_panel.title("Fütüristik Hesaplamalar")
            self.futuristic_panel.geometry("400x640")
            self.futuristic_panel.configure(bg="#2d2d2d")

            ttk.Button(self.futuristic_panel, text="Gezegenler arası mesafeler", command=self.show_planet_distance_window).pack(pady=10)
            ttk.Button(self.futuristic_panel, text="Gezegenlere göre kg?", command=self.show_weight_on_planet_window).pack(pady=10)
            ttk.Button(self.futuristic_panel, text="Yörünge Hızı", command=self.show_orbital_speed_window).pack(pady=10)
            ttk.Button(self.futuristic_panel, text="Seyahat Süresi", command=self.show_travel_time_window).pack(pady=10)
            ttk.Button(self.futuristic_panel, text="Işık yılı", command=self.show_light_year_window).pack(pady=10)
            ttk.Button(self.futuristic_panel, text="Devir Hızı (RPM) - CNC", command=self.rpm).pack(pady=10)
            ttk.Button(self.futuristic_panel, text="İlerleme Hızı (IPM) - CNC", command=self.ipm).pack(pady=10)
            ttk.Button(self.futuristic_panel, text="Yüzde Hesaplama", command=self.percentage_calculator).pack(pady=10)
            ttk.Button(self.futuristic_panel, text="Motor Gücü Hesaplama", command=self.motorgucuhesap).pack(pady=10)
        else:
            self.futuristic_panel.destroy()
            self.futuristic_panel = None
    def motorgucuhesap(self):
        power_window = tk.Toplevel(self)
        power_window.title("Motor Gücü Hesaplama")
        power_window.geometry("400x300")
        power_window.configure(bg="#2d2d2d")

        def calculate_power():
            voltage = float(voltage_entry.get())
            current = float(current_entry.get())
            power_factor = float(power_factor_entry.get())
            power = voltage * current * power_factor
            result_label.config(text=f"Motor gücü: {power:.2f} watt")

        tk.Label(power_window, text="Voltajı girin (V):", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        voltage_entry = tk.Entry(power_window)
        voltage_entry.pack(pady=5)

        tk.Label(power_window, text="Akımı girin (A):", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        current_entry = tk.Entry(power_window)
        current_entry.pack(pady=5)

        tk.Label(power_window, text="Güç faktörünü girin:", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        power_factor_entry = tk.Entry(power_window)
        power_factor_entry.pack(pady=5)

        calculate_button = ttk.Button(power_window, text="Hesapla", command=calculate_power)
        calculate_button.pack(pady=10)

        result_label = tk.Label(power_window, text="", bg="#2d2d2d", fg="#ffffff")
        result_label.pack(pady=10)
          
    def percentage_calculator(self):
        percentage_window = tk.Toplevel(self)
        percentage_window.title("Yüzde Hesaplama")
        percentage_window.geometry("400x250")
        percentage_window.configure(bg="#2d2d2d")

        def calculate_percentage():
            number = float(entry_number.get())
            percentage = float(entry_percentage.get())
            result = number * (percentage / 100)
            result_label.config(text=f"Sonuç: {result:.2f}")

        tk.Label(percentage_window, text="Sayiyi girin:", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        entry_number = tk.Entry(percentage_window)
        entry_number.pack(pady=5)

        tk.Label(percentage_window, text="Yüzdeyi girin:", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        entry_percentage = tk.Entry(percentage_window)
        entry_percentage.pack(pady=5)

        calculate_button = ttk.Button(percentage_window, text="Hesapla", command=calculate_percentage)
        calculate_button.pack(pady=10)

        result_label = tk.Label(percentage_window, text="", bg="#2d2d2d", fg="#ffffff")
        result_label.pack(pady=10)

                
    def rpm(self):
        rpm_window = tk.Toplevel(self)
        rpm_window.title("Devir Hızı (RPM) Hesaplama")
        rpm_window.geometry("400x250")
        rpm_window.configure(bg="#2d2d2d")

        def calculate_rpm():
            cutting_speed = float(entry.get())
            diameter = float(diameter_entry.get())
            rpm = 12 * cutting_speed / (math.pi * diameter)
            result_label.config(text=f"Devir hızı: {rpm:.2f} RPM")

        tk.Label(rpm_window, text="Kesme hızını girin (metre/dakika):", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        entry = tk.Entry(rpm_window)
        entry.pack(pady=5)

        tk.Label(rpm_window, text="Matkap çapını girin (milimetre):", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        diameter_entry = tk.Entry(rpm_window)
        diameter_entry.pack(pady=5)

        calculate_button = ttk.Button(rpm_window, text="Hesapla", command=calculate_rpm)
        calculate_button.pack(pady=10)

        result_label = tk.Label(rpm_window, text="", bg="#2d2d2d", fg="#ffffff")
        result_label.pack(pady=10)

    def ipm(self):
        ipm_window = tk.Toplevel(self)
        ipm_window.title("İlerleme Hızı (IPM) Hesaplama")
        ipm_window.geometry("400x250")
        ipm_window.configure(bg="#2d2d2d")

        def calculate_ipm():
            feed_per_tooth = float(entry.get())
            teeth_number = float(teeth_entry.get())
            rpm = float(rpm_entry.get())
            ipm = feed_per_tooth * teeth_number * rpm
            result_label.config(text=f"İlerleme hızı: {ipm:.2f} IPM")

        tk.Label(ipm_window, text="Diş başına besleme (milimetre):", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        entry = tk.Entry(ipm_window)
        entry.pack(pady=5)

        tk.Label(ipm_window, text="Diş sayısını girin:", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        teeth_entry = tk.Entry(ipm_window)
        teeth_entry.pack(pady=5)

        tk.Label(ipm_window, text="Devir hızını girin (RPM):", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        rpm_entry = tk.Entry(ipm_window)
        rpm_entry.pack(pady=5)

        calculate_button = ttk.Button(ipm_window, text="Hesapla", command=calculate_ipm)
        calculate_button.pack(pady=10)

        result_label = tk.Label(ipm_window, text="", bg="#2d2d2d", fg="#ffffff")
        result_label.pack(pady=10)
        
    def show_planet_distance_window(self):
        distance_window = tk.Toplevel(self)
        distance_window.title("Gezegenler Arası Mesafeler")
        distance_window.geometry("400x400")
        distance_window.configure(bg="#2d2d2d")

        distances = {
            "Merkür": "57.91 milyon km",
            "Venüs": "108.2 milyon km",
            "Dünya": "149.6 milyon km",
            "Mars": "227.9 milyon km",
            "Jüpiter": "778.5 milyon km",
            "Satürn": "1.434 milyar km",
            "Uranüs": "2.871 milyar km",
            "Neptün": "4.495 milyar km"
        }

        for i, (planet, distance) in enumerate(distances.items()):
            ttk.Label(distance_window, text=f"{planet}: {distance}", font=("Helvetica", 14), background="#2d2d2d", foreground="#ffffff").pack(pady=10)

    def show_weight_on_planet_window(self):
        weight_window = tk.Toplevel(self)
        weight_window.title("Gezegenlere Göre Ağırlık Hesaplama")
        weight_window.geometry("400x250")
        weight_window.configure(bg="#2d2d2d")

        def calculate_weight():
            weight_on_earth = float(entry.get())
            planet = planet_var.get()
            gravity = {
                "Merkür": 3.7,
                "Venüs": 8.87,
                "Dünya": 9.81,
                "Mars": 3.71,
                "Jüpiter": 24.79,
                "Satürn": 10.44,
                "Uranüs": 8.69,
                "Neptün": 11.15
            }
            weight_on_planet = weight_on_earth * gravity[planet] / 9.81
            result_label.config(text=f"{planet} üzerinde ağırlık: {weight_on_planet:.2f} kg")

        tk.Label(weight_window, text="Dünya üzerindeki ağırlığınızı girin (kg):", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        entry = tk.Entry(weight_window)
        entry.pack(pady=5)

        tk.Label(weight_window, text="Gezegen seçin:", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        planet_var = tk.StringVar()
        planet_menu = ttk.OptionMenu(weight_window, planet_var, "Dünya", "Merkür", "Venüs", "Dünya", "Mars", "Jüpiter", "Satürn", "Uranüs", "Neptün")
        planet_menu.pack(pady=5)

        calculate_button = ttk.Button(weight_window, text="Hesapla", command=calculate_weight)
        calculate_button.pack(pady=10)

        result_label = tk.Label(weight_window, text="", bg="#2d2d2d", fg="#ffffff")
        result_label.pack(pady=10)

    def show_orbital_speed_window(self):
        speed_window = tk.Toplevel(self)
        speed_window.title("Yörünge Hızı Hesaplama")
        speed_window.geometry("400x200")
        speed_window.configure(bg="#2d2d2d")

        def calculate_speed():
            planet = planet_var.get()
            orbital_speeds = {
                "Merkür": 47.87,
                "Venüs": 35.02,
                "Dünya": 29.78,
                "Mars": 24.07,
                "Jüpiter": 13.07,
                "Satürn": 9.69,
                "Uranüs": 6.81,
                "Neptün": 5.43
            }
            speed = orbital_speeds[planet]
            result_label.config(text=f"{planet} yörünge hızı: {speed} km/s")

        tk.Label(speed_window, text="Gezegen seçin:", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        planet_var = tk.StringVar()
        planet_menu = ttk.OptionMenu(speed_window, planet_var, "Dünya", "Merkür", "Venüs", "Dünya", "Mars", "Jüpiter", "Satürn", "Uranüs", "Neptün")
        planet_menu.pack(pady=5)

        calculate_button = ttk.Button(speed_window, text="Hesapla", command=calculate_speed)
        calculate_button.pack(pady=10)

        result_label = tk.Label(speed_window, text="", bg="#2d2d2d", fg="#ffffff")
        result_label.pack(pady=10)
    
    def show_travel_time_window(self):
        time_window = tk.Toplevel(self)
        time_window.title("Sürtünmesiz Ortamda Seyahat Süresi Hesaplama")
        time_window.geometry("400x250")
        time_window.configure(bg="#2d2d2d")

        def calculate_travel_time():
            distance = float(entry.get())
            speed = float(speed_entry.get())
            time = distance / speed
            result_label.config(text=f"Seyahat süresi: {time:.2f} saat")

        tk.Label(time_window, text="Mesafeyi girin (km):", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        entry = tk.Entry(time_window)
        entry.pack(pady=5)

        tk.Label(time_window, text="Hızı girin (km/s):", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        speed_entry = tk.Entry(time_window)
        speed_entry.pack(pady=5)

        calculate_button = ttk.Button(time_window, text="Hesapla", command=calculate_travel_time)
        calculate_button.pack(pady=10)

        result_label = tk.Label(time_window, text="", bg="#2d2d2d", fg="#ffffff")
        result_label.pack(pady=10)

    def show_light_year_window(self):
        light_year_window = tk.Toplevel(self)
        light_year_window.title("Işık Yılını Kilometreye Çevirme")
        light_year_window.geometry("400x500")
        light_year_window.configure(bg="#2d2d2d")

        def convert_light_year_to_km():
            light_years = float(entry.get())
            kilometers = light_years * 9.461e12
            result_label.config(text=f"{light_years} ışık yılı: {kilometers:.2e} km")

        tk.Label(light_year_window, text="Işık yılı miktarını girin:", bg="#2d2d2d", fg="#ffffff").pack(pady=10)
        entry = tk.Entry(light_year_window)
        entry.pack(pady=5)

        convert_button = ttk.Button(light_year_window, text="Çevir", command=convert_light_year_to_km)
        convert_button.pack(pady=10)

        result_label = tk.Label(light_year_window, text="", bg="#2d2d2d", fg="#ffffff")
        result_label.pack(pady=10)

    def click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def equal(self):
        try:
            # Sayı ve parantez arasına çarpma işareti ekleniyor
            expression = re.sub(r'(\d)(\()', r'\1*\2', self.expression)
            result = str(eval(expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Hata")
            self.expression = ""

    def evaluate(self):
        try:
            # "*" işareti eksik olan ifadeleri otomatik olarak çarpmaya dönüştür
            modified_expression = re.sub(r'(\d+)\s*\(', r'\1*(', self.expression)
            result = str(eval(modified_expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Hata")
            self.expression = ""

    def sqrt(self):
        try:
            result = str(eval(f"math.sqrt({self.expression})"))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Hata")
            self.expression = ""

    def pow2(self):
        try:
            result = str(eval(f"({self.expression})**2"))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Hata")
            self.expression = ""

    def log(self):
        try:
            result = str(eval(f"math.log10({self.expression})"))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Hata")
            self.expression = ""

    def sin(self):
        try:
            result = str(eval(f"math.sin(math.radians({self.expression}))"))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Hata")
            self.expression = ""

    def cos(self):
        try:
            result = str(eval(f"math.cos(math.radians({self.expression}))"))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Hata")
            self.expression = ""

    def tan(self):
        try:
            result = str(eval(f"math.tan(math.radians({self.expression}))"))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Hata")
            self.expression = ""

if __name__ == "__main__":
    app = ModernCalculator()
    app.mainloop()
