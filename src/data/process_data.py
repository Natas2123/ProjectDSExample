import pandas as pd

# Ruta del archivo de datos en bruto
input_filepath = "./data/raw/RH_bruto.csv"

# Ruta donde se guardará el archivo de datos procesados
output_filepath = "./data/processed/RH_procesado.csv"

# Leer los datos brutos
df = pd.read_csv(input_filepath)

# Rellenar los valores faltantes
# Para 'Años_En_Empresa', 'Ingreso_Mensual', 'Evaluacion_Desempeño', y 'Nivel_Satisfaccion'
# vamos a usar la media de cada columna
for column in [
    "Años_En_Empresa",
    "Ingreso_Mensual",
    "Evaluacion_Desempeño",
    "Nivel_Satisfaccion",
]:
    df[column] = df[column].fillna(df[column].mean())

# Para 'Nombre', 'Apellido', 'Rol_Trabajo', 'Genero', y 'Desercion'
# vamos a rellenar los valores faltantes con un valor predeterminado
for column in ["Nombre", "Apellido", "Rol_Trabajo", "Genero", "Desercion"]:
    df[column] = df[column].fillna("Desconocido")

# Para 'ID_Empleado' vamos a eliminar las filas que tienen un valor faltante, ya que es un identificador único
df = df.dropna(subset=["ID_Empleado"])

# Guardar los datos procesados
df.to_csv(output_filepath, index=False)

print("Los datos se han procesado y guardado correctamente.")
