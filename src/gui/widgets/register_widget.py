import customtkinter as ctk

class RegisterWidget(ctk.CTkFrame):    
    def __init__(self, master, app):
        super().__init__(master)
        self.parent_app = app

        # Widget split into 2 frames. Top and Bottom
        self.grid_rowconfigure((0, 1, 2), weight=1)

        title_label = ctk.CTkLabel(self, text="Registro", font=ctk.CTkFont(size=40, weight="bold", family="Verdana"))
        title_label.grid(row=0, column=0, padx=20, pady=20)

        # Top frame. 2 columns and 5 rows
        form_frame = ctk.CTkFrame(self)
        form_frame.grid(row=1, column=0, padx=20, pady=20)
        form_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        form_frame.grid_columnconfigure((0, 1), weight=1)

        self.error_label = ctk.CTkLabel(form_frame, text=None, text_color="red", font=ctk.CTkFont(size=10))
        self.error_label.grid(row=0, column=0, padx=20, pady=20)

        user_label = ctk.CTkLabel(form_frame, text="Usuario")
        user_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.user_entry = ctk.CTkEntry(form_frame, placeholder_text="Nombre de usuario *", width=250)
        self.user_entry.grid(row=1, column=1, padx=20, pady=20)

        email_label = ctk.CTkLabel(form_frame, text="Email")
        email_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.email_entry = ctk.CTkEntry(form_frame, placeholder_text="ejemplo@gmail.com *", width=250)
        self.email_entry.grid(row=2, column=1, padx=20, pady=20)

        password_label = ctk.CTkLabel(form_frame, text="Contraseña")
        password_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        self.password_entry = ctk.CTkEntry(form_frame, placeholder_text="******", show="*", width=250)
        self.password_entry.grid(row=3, column=1, padx=20, pady=20)

        rep_password_label = ctk.CTkLabel(form_frame, text="Repetir contraseña")
        rep_password_label.grid(row=4, column=0, padx=20, pady=20, sticky="w")
        self.rep_password_entry = ctk.CTkEntry(form_frame, placeholder_text="******", show="*", width=250)
        self.rep_password_entry.grid(row=4, column=1, padx=20, pady=20)


        # Bottom frame. 2 columns and 1 row
        button_frame = ctk.CTkFrame(self)
        button_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        button_frame.grid_columnconfigure((0, 1), weight=1)

        cancel_button = ctk.CTkButton(button_frame, text="Cancelar", command=app.welcome_screen, width=75)
        cancel_button.grid(row=0, column=0, padx=20, pady=20, sticky="e")

        register_button = ctk.CTkButton(button_frame, text="Registrarse", command=self.register, width=75)
        register_button.grid(row=0, column=1, padx=20, pady=20, sticky="w")


    def register(self):
        self.reset_ui()
        user_input_validation = self.check_user_input()

        if user_input_validation:
            error, status, data = self.parent_app.register(self.user_entry.get(), self.email_entry.get(), self.password_entry.get())
            if error:
                print("Error a la hora de realizar el registro: " + data)
            elif not status:
                self.error_label.configure(text="El usuario ya existe")
            else:
                self.parent_app.welcome_screen()


    def check_user_input(self) -> bool:
        user = len(self.user_entry.get()) > 0
        email = len(self.email_entry.get()) > 0
        password = len(self.password_entry.get()) > 0
        rep_password = len(self.rep_password_entry.get()) > 0

        if not user:
            self.user_entry.configure(border_color="darkred")

        if not email:
            self.email_entry.configure(border_color="darkred")

        if not password:
            self.password_entry.configure(border_color="darkred")

        if not rep_password:
            self.rep_password_entry.configure(border_color="darkred")

        if not self.password_entry.get() == self.rep_password_entry.get():
            self.error_label.configure(text="Las contraseñas no coinciden")
            self.password_entry.configure(border_color="darkred")
            self.rep_password_entry.configure(border_color="darkred")
            return False
        
        elif not (user and email and password and rep_password):
            self.error_label.configure(text="Verifica los campos marcados")

        return user and email and password and rep_password


    def reset_ui(self):
        self.error_label.configure(text=None)
        self.user_entry.configure(border_color="gray50")
        self.email_entry.configure(border_color="gray50")
        self.password_entry.configure(border_color="gray50")
        self.rep_password_entry.configure(border_color="gray50")
