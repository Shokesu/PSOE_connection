# PSOE_connection

1. Instrucciones de uso.

    Para empezar a recolectar tweets, ejecutar el script **model/PSOE_tweet_collector.py**
    Este script realizará consultas a la base de datos ElasticSeach para obtener los tweets que satisfagan los siguientes
    criterios:
    - En el cuerpo del mensaje, aparece uno de los siguientes términos: **@sanchezcastejon, @patxilopez, @susanadiaz**
    - En el cuerpo del mensaje se menciona una fuente de información externa (url)

    El script procesará los tweets consultados y almacenará en el fichero **data/tweets.json** la información de estos, codificada en formato
    JSON.


2. Para visualizar los datos, abrir el notebook en **view/visualize_data.ipynb** con IPython o Jupyter.
  Al ejecutarlo, se generarán una serie de gráficos:
    - Gráfico que muestra el número de tweets que mencionan a cada candidato del PSOE (Sanchez, Patxi y Susana)
    - Gráfico que visualiza las fuentes de información externas más referenciadas en estos tweets.
    - Gráfico igual que el anterior, solo que los tweets se agregan por candidato.

