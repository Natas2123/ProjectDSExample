
---

# Informe: Proyecto de Predicción de Deserción Laboral 

## Procesamiento de Datos

Primero, importamos nuestros datos a partir de un archivo CSV y examinamos el marco de datos para tener una visión general:

```python
df = pd.read_csv("./data/processed/RH_procesado.csv")
print(df.head())
```

Dado que algunos de nuestros datos son no numéricos, estos necesitan ser transformados a valores numéricos para que puedan ser procesados por nuestro modelo. Utilizamos un codificador de etiquetas para lograr esto:

```python
for column in df.columns:
    if df[column].dtype == type(object):
        le = preprocessing.LabelEncoder()
        df[column] = le.fit_transform(df[column])
```

A continuación, mostramos nuestro dataframe procesado:

```python
print(df.head())
```

## Preparación de Datos

Nuestro objetivo es predecir la deserción, por lo que ajustamos nuestros datos para reflejar esto. En nuestro caso, los valores de 'Desercion' son 0, 1, y 2, y decidimos tratar tanto el 0 como el 2 como indicadores de no-deserción:

```python
mapeo_desercion = {1: 1, 0: 0, 2: 0}
df["Desercion"] = df["Desercion"].replace(mapeo_desercion)
```

## Modelo de Entrenamiento

Usamos un 80% de los datos para entrenar nuestro modelo y dejamos el 20% restante para probarlo. Elegimos un modelo de Random Forest por su robustez y capacidad para manejar una gran cantidad de características:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
```

## Predicciones

Finalmente, hacemos algunas predicciones usando nuestro modelo y las mostramos para tener una idea de su rendimiento:

```python
predictions = clf.predict(X_test)
print(predictions[:5])
```

---

Este informe proporciona un resumen de alto nivel de tu trabajo en el proyecto, explicando qué estás haciendo en cada paso y por qué. Puedes agregar más detalles y análisis en cada sección según sea necesario para tu audiencia y propósitos.