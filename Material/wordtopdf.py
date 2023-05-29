import os
from docx2pdf import convert

def convert_to_pdf():
    # Nombre constante del archivo de entrada
    input_file = "ApuntsDS.docx"
    
    # Definir la ruta del archivo de salida
    output_file = os.path.join(os.path.dirname(__file__), "ApuntsDS.pdf")
    
    try:
        convert(input_file, output_file)
        print("La conversión se ha completado con éxito.")
    except Exception as e:
        print(f"Error al convertir el archivo: {str(e)}")