import streamlit as st
import pandas as pd
from connect import add_user, read_usuarios,init_db,get_user
from usuario import Usuario
import plotly.express as px


COLS_FORM = [
                "ID", 
                "Nombre", 
                "Apellido", 
                "Correo electrónico", 
                "Contraseña",
                "Fecha de registro",
                "Número de teléfono" 
        ]
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
        init_db()

    def run(self):
        st.set_page_config(page_title=self.titulo, page_icon=":shark:", layout="wide")
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

        with user:
            col1, col2 = st.columns(2)

            with col1:
                nombre_input = st.text_input(COLS_FORM[1])
                apellido_input = st.text_input(COLS_FORM[2])
                correo_input = st.text_input(COLS_FORM[3], "example@gmail.com", key="placeholder")

            with col2:
                telefono_input = st.text_input(COLS_FORM[6])
                contrasena_input = st.text_input(COLS_FORM[4], type="password")

            btn_crear = st.form_submit_button("Crear")
        
        if btn_crear:
            user =(nombre_input, apellido_input, correo_input, telefono_input, contrasena_input)
            if add_user(user):
                st.success("Usuario creado exitosamente.")
                st.balloons()
            else:
                st.error("Error al crear usuario.", icon="🚨")
                
            
    def ver_usuarios(self):
        st.subheader("Lista de usuarios")
        lista_usuarios = read_usuarios()
        df = pd.DataFrame(lista_usuarios, columns=[
                "ID", 
                "Nombre", 
                "Apellido", 
                "Correo electrónico", 
                "Contraseña",
                "Fecha de registro",
                "Número de teléfono" 
        ])
        st.dataframe(df,width=2000,hide_index=True)
        
        with st.expander("Cantidad usuarios"):
            st.title(df.shape[0])
        with st.expander("Ver JSON"):
            st.json(lista_usuarios)
            
    def borrar_usuarios(self):
        st.subheader("Borrar usuarios")
    def actualizar_usuarios(self):
        st.subheader("Actualizar usuarios")
        lista_usuarios = read_usuarios()
        df = pd.DataFrame(lista_usuarios, columns=COLS_FORM)
        with st.expander("Lista de usuarios"):
            st.dataframe(df,width=2000,hide_index=True)
        selected_user = st.selectbox("Selecciona un usuario",df["ID"])
        result_user = get_user(selected_user)
        if result_user:
            user = st.form("persona_info")
            with user:
                col1, col2 = st.columns(2)

                with col1:
                    upd_nombre_input = st.text_input(COLS_FORM[1],value=result_user[0][1])
                    upd_apellido_input = st.text_input(COLS_FORM[2],value=result_user[0][2])
                    upd_correo_input = st.text_input(COLS_FORM[3],value=result_user[0][3], key="placeholder")

                with col2:
                    upd_telefono_input = st.text_input(COLS_FORM[6],value=result_user[0][6])
                    upd_contrasena_input = st.text_input(COLS_FORM[4], type="password",value=result_user[0][4])

                btn_update = st.form_submit_button("Actualizar")
        
if __name__ == "__main__":
    init_db()
    app = App()
    app.run()
