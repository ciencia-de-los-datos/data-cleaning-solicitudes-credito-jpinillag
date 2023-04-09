"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def corregir_fecha(cadena):
    formatos_fecha = ['%Y/%m/%d', '%d/%m/%Y', '%Y-%m-%d', '%d-%m-%Y', '%m/%d/%Y', '%Y/%d/%m']
    for formato in formatos_fecha:
        try:
            return pd.to_datetime(cadena, format=formato)
        except:
            pass
    return np.nan

def clean_data():


    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col='Unnamed: 0')
    df=df.dropna()
    
    #Pasar todo a minusculas
    df["sexo"]=df["sexo"].apply(lambda x:str(x).lower())

    df["tipo_de_emprendimiento"]=df["tipo_de_emprendimiento"].apply(lambda y:str(y).lower())
    
    df["idea_negocio"]=df["idea_negocio"].apply(lambda y:str(y).lower())
    df["idea_negocio"]=df["idea_negocio"].apply(lambda y:y.replace("_"," "))
    df["idea_negocio"]=df["idea_negocio"].apply(lambda y:y.replace("-"," "))
    df["idea_negocio"]=df["idea_negocio"].apply(lambda y: y[:-1] if (y[-1]==" ") else y)

    df["barrio"]=df["barrio"].apply(lambda y:str(y).lower())
    
    df["barrio"]=df["barrio"].apply(lambda y:y.replace("_"," "))
    df["barrio"]=df["barrio"].apply(lambda y:y.replace("-"," "))

    df["comuna_ciudadano"]=df["comuna_ciudadano"].apply(lambda y: int(y))

    df["monto_del_credito"]=df["monto_del_credito"].apply(lambda y:y.replace(".00",""))
    df["monto_del_credito"]=df["monto_del_credito"].apply(lambda y:y.replace(" ",""))
    df["monto_del_credito"]=df["monto_del_credito"].apply(lambda y:y.replace(",",""))
    df["monto_del_credito"]=df["monto_del_credito"].apply(lambda y:y.replace("$",""))
    df["monto_del_credito"]=df["monto_del_credito"].apply(lambda y:int(y))

    df["línea_credito"]=df["línea_credito"].apply(lambda y:str(y).lower())
    df["línea_credito"]=df["línea_credito"].apply(lambda y:y.replace("empresarial-ed.-","empresarial ed."))
    df["línea_credito"]=df["línea_credito"].apply(lambda y:y.replace("empresarial_ed._","empresarial ed."))
    df["línea_credito"]=df["línea_credito"].apply(lambda y:y.replace("empresarial ed. ","empresarial ed."))

    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(corregir_fecha)

    df=df.drop_duplicates()
   
    return df

