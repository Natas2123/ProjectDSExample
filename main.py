import pandas as pd
from sklearn import preprocessing
import joblib
import numpy as np

# Asumamos que tienes una Serie de pandas `data_test` que contiene tus datos de prueba.
data_test = pd.Series(
    {
        "Años_En_Empresa": 5.0,
        "Ingreso_Mensual": 5000.0,
        "Evaluacion_Desempeño": 3.0,
        "Nivel_Satisfaccion": 0.6,
        "Caracteristica_5": 1.0,
        "Caracteristica_6": 2.0,
        "Caracteristica_7": 3.0,
        "Caracteristica_8": 4.0,
        "Caracteristica_9": 5.0,
    }
)


# Cargar el modelo entrenado
clf = joblib.load("random_forest.joblib")

# Si tienes alguna columna no numérica en tu serie, necesitas convertirla a numérica.
# En este caso, todas nuestras columnas son numéricas, por lo que podemos omitir este paso.

# Asegúrate de que tus datos estén en la forma correcta.
# Los modelos de scikit-learn siempre esperan los datos de entrada en una forma bidimensional (n_samples, n_features),
# incluso si sólo tienes una muestra (en este caso, n_samples sería 1).
data_test = np.array(data_test).reshape(1, -1)

# Realizar la predicción
prediction = clf.predict(data_test)

print("La predicción es: ", prediction)
