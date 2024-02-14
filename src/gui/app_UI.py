import customtkinter
from gui.widgets.login_widget import LoginWidget
from gui.widgets.password_widget import PasswordWidget
from gui.widgets.edit_pass_widget import EditPasswordWidget
from gui.widgets.view_pass_widget import ViewPasswordWidget
from gui.widgets.add_pass_widget import AddPasswordWidget
from gui.widgets.register_widget import RegisterWidget
from code.controller import Controller

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self, controller: Controller):
        super().__init__()

        # Backend comunication
        self.controller = controller

        self.title("SafeLock")
        self.geometry(f"{1280}x{720}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Main widget (root)
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20)

        self.main_frame.grid_rowconfigure((0, 1), weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Current widget displayed on the main widget
        self.welcome_screen()

    def login(self, email: str, password: str):
        confirm = self.controller.login(email, password)
        if confirm is False:
            ''' Show ui error name or pasasword incorrect'''
            pass
        else:
            self.home()

    def register(self, email: str, password: str, rep_password: str):
        confirm = self.controller.register(email, password, rep_password)
        if confirm is False:
            ''' Show ui error '''
            pass
        else:
            ''' Show ui feedback and proceed to login '''

    def welcome_screen(self):
        self.clear_ui()
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Safe Lock", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        self.current_frame = LoginWidget(self.main_frame, app=self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)
    
    def home(self):
        self.clear_ui()
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Contraseñas", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        self.current_frame = PasswordWidget(self.main_frame, app=self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)


    def edit_pass(self):
        self.clear_ui()
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Editar contraseña", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        self.current_frame = EditPasswordWidget(self.main_frame, app=self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)
        # Get data from backend and change to new widget UI

    def view_register(self):
        self.clear_ui()
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Registro", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        self.current_frame = RegisterWidget(self.main_frame, app=self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)

    def view_pass(self):
        self.clear_ui()
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Ver Contraseña", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        self.current_frame = ViewPasswordWidget(self.main_frame, app=self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)
        # Get data from backend and change to new widget UI
        pass

    def delete_pass(self):
        print("Contraseña borrada")
        # Delete password from backend and refresh UI
        pass

    def add_pass(self):
        self.clear_ui()
        self.current_title = customtkinter.CTkLabel(self.main_frame, text="Añadir Contraseña", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_title.grid(row=0, column=0, padx=20, pady=20)

        self.current_frame = AddPasswordWidget(self.main_frame, app=self)
        self.current_frame.grid(row=1, column=0, padx=20, pady=20)
        # Add password to backend and refresh UI
        pass

    def clear_ui(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
