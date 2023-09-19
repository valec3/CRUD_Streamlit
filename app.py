import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False



class App:
    def __init__(self):
        self.titulo = "Aplicación CRUD con Streamlit"
        self.menu = {
            "Inicio": self.mostrar_inicio,
            "Crear usuarios": self.crear_usuario,
            "Borrar usuarios": self.borrar_usuarios,
            "Ver usuarios": self.ver_usuarios,
            "Actualizar usuarios": self.actualizar_usuarios,
            
        }
        self.pagina_actual = "Inicio"

    def run(self):
        st.set_page_config(page_title=self.titulo)
        st.title(self.titulo)

        # Menú lateral
        self.pagina_actual = st.sidebar.selectbox("Selecciona una página", list(self.menu.keys()))

        # Contenido de la aplicación
        self.menu[self.pagina_actual]()

    def mostrar_inicio(self):
        st.subheader("Bienvenido a la página de inicio. Esta es la página principal de la aplicación.")

    def crear_usuario(self):
        
        st.subheader("Crear usuario.")
        user = st.form("persona_info")
        col1, col2 = st.columns(2)
        with col1:
            nombre_input = user.text_input(
                "Nombre",
                label_visibility=st.session_state.visibility,
                disabled=st.session_state.disabled,
            )
            apellido_input = user.text_input(
                "Apellido",
                label_visibility=st.session_state.visibility,
            )
            correo_input = user.text_input(
                "Correo electrónico",
                "example@gmail.com",
                key="placeholder",
            )
            
            
        with col2:
            telefono_input = user.text_input(
                "Número de teléfono",
                label_visibility=st.session_state.visibility,
            )
            contrasena_input = user.text_input(
                "Contraseña",
                label_visibility=st.session_state.visibility,
            )
        btn_crear = user.form_submit_button("Crear")


    def ver_usuarios(self):
        st.subheader("Lista de usuarios")
        
    def borrar_usuarios(self):
        st.subheader("Borrar usuarios")
    def actualizar_usuarios(self):
        st.subheader("Actualizar usuarios")
        
if __name__ == "__main__":
    app = App()
    app.run()
