### Programacion de Computadoras IV
## Parcial 2
# Braulio Rodriguez 8-899-1093

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

dataframe = pd.read_csv('Vacunas.csv')
dataframe = dataframe.convert_dtypes()


# Funciones
# Mostrar todos los datos
@app.route('/Vacunas', methods=['GET'])
def MostarTodo():
    Vacunas = dataframe.dropna()
    Vacunas = Vacunas.to_json(orient='index')
    return jsonify(Vacunas)


# Filtro de datos por pais
@app.route('/Vacunas/<string:Pais>', methods=['GET'])
def FiltroPaises(Pais):
    DataframeFinal = pd.DataFrame()
    DataframeFinal = dataframe[dataframe['Country Name'] == Pais]
    DataframeFinal = DataframeFinal.dropna(1)
    db = DataframeFinal.to_json(orient='index')
    return jsonify(db)


# Filtro de datos por año
@app.route('/Vacunas/<string:Pais>/<string:Year>', methods=['GET'])
def FiltroYear(Pais, Year):
    Datos_Filtrados = dataframe[dataframe['Country Name'] == Pais]
    Datos_Filtrados = Datos_Filtrados.dropna(1)
    Yearlist = Year.split(',')
    Datos_FiltradosYear = Datos_Filtrados[Yearlist]
    DatosFinales = Datos_FiltradosYear.to_json(orient='index')
    return jsonify(DatosFinales)


app.run(debug=True, port=8000)
