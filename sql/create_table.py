# CrearTabla.py
import sqlite3


def create_prediction_table():
    conn = sqlite3.connect("my_database.db")  # connect to your database
    c = conn.cursor()

    # Create table
    c.execute(
        """
        CREATE TABLE Predicciones (
            ID INTEGER PRIMARY KEY,
            UsuarioID INTEGER,
            Prediccion REAL,
            FechaPrediccion TIMESTAMP
        )
    """
    )

    # Save (commit) the changes and close the connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_prediction_table()
