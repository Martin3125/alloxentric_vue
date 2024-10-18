import pandas as pd
import re
import pandas as pd


def prepare_data(data):

    df_copy = data.copy()
    df_copy.head()

    # Función para eliminar números y caracteres especiales del nombre de la acción
    def limpiar_accion(homologada):
        if isinstance(homologada, str):  # Verificar si el valor es una cadena
            # Usamos una expresión regular para quitar números, puntos y guiones
            return re.sub(r'\d+[\.-]*', '', homologada).strip()
        return homologada  # Si no es una cadena, devolver el valor tal como está

    # Aplicar la función a la columna 'homologada'
    df_copy['homologada'] = df_copy['homologada'].apply(limpiar_accion)

    #ImputaciÃ³n por 0 de la variable 'Pago'
    df_copy['Pago'] = df_copy['Pago'].fillna(0)

    df_copy2 = df_copy.copy()
    df_copy2.head()

    # Agrupar por la columna 'deudor' y aplicar funciones específicas para cada columna
    df_agrupado = df_copy2.groupby('deudor').agg({
    'Pago': 'sum',  # Sumar los montos de Pago
    'fecha': lambda x: ', '.join(map(str, x.unique())),
    'fecha_pago': lambda x: ', '.join(map(str, x.unique())),
    'id_cliente': lambda x: ', '.join(map(str, x.unique())),  # Concatenar los id_cliente únicos separados por coma
    'homologada': lambda x: ', '.join(map(str, x.unique())),  # Tomar el primer valor de homologada (puedes cambiar esto si lo necesitas) # Tomar el primer valor de AccionCobranza
    'TipoGestion': lambda x: ', '.join(map(str, x.unique())),  # Tomar el primer valor de TipoGestion
    'Descripcion': lambda x: ', '.join(map(str, x.unique()))  # Tomar el primer valor de Descripcion
    }).reset_index()
    # Crear una nueva columna binaria 'PagoBinario' en df_copy
    df_agrupado['PagoBinario'] = df_agrupado['Pago'].apply(lambda x: 1 if x > 0 else 0)

    # Aplicar One-Hot Encoding a las columnas 'homologada', 'TipoGestion' y 'Descripcion'
    df_encoded = pd.get_dummies(df_copy2, columns=['homologada', 'TipoGestion'], prefix=['homologada', 'TipoGestion'])

    # Agrupar por 'deudor' de nuevo, sumando los valores binarios para cada categorÃa
    df_final = df_encoded.groupby('deudor').max().reset_index()

    # Crear una nueva columna binaria 'PagoBinario' en df_copy
    df_final['PagoBinario'] = df_final['Pago'].apply(lambda x: 1 if x > 0 else 0)
    
    # Diccionario para mapear descripciones a acciones
    accion_dict = {
        'Sin acciones': [
            'CORTAN LLAMADO',
            'SIN TELEFONOS',
            'TELEFONO VACANTE/MALO/FUERA DE SERVICIO',
            'NO CORRESPONDE TELEFONO/NO TRABAJA ALLI/NO LO CONOCEN',
            'NO CORRESPONDE TELEFONO/NO VIVE ALLI/NO LO CONOCEN',
            'NO RECIBEN RECADOS',
            'NO QUIERE PAGA/DESCONOCE LA DEUDA',
            'DEUDOR NO INFORMADO',
            'DICE QUE PAGO/ABONO/RENEGOCIO',
            'NO PUEDE PAGAR',
            'OCUPADO/CONGESTION'
        ],
        'Correo electrónico': [
            'EMAIL - DICE QUE PAGO/ABONO/RENEGOCIO',
            'ENVIO EMAIL COMERCIAL',
            'EMAIL - CONTACTO DEUDOR',
            'EMAIL - COMPROMISO DE PAGO',
            'EMAIL - SE CONFIRMA PAGO'
        ],
        'SMS': [
            'COMENTARIO',  # Ejemplo de un comentario que se incluirá en SMS
            'COMENTARIO - COMPROMISO PAGO',
            'COMENTARIO - CONTACTO DEUDOR',
            'COMENTARIO - NO QUIERE PAGAR'
            # Agrega más descripciones relacionadas a SMS aquí si es necesario
        ],
        'Whatsapp': [
            'WHATSAPP - CONTACTO DEUDOR',
            'WHATSAPP - COMPROMISO DE PAGO'
        ],
        'Llamada por bot': [
            'BUZON DE VOZ',
            'NO CONTESTA'
        ],
        'Llamada directa': [
            'CONTACTO DEUDOR',
            'COMPROMISO DE PAGO',
            'RECADO EN CASA',
            'RECADO EN OFICINA',
            'PIDE VOLVER A LLAMAR',
            'VOLVER A LLAMAR',
            'SE CONFIRMA PAGO',
            'CLIENTE REALIZARA PLAN DE PAGOS',
            'COMPROMISO PAGO - TRANSFERENCIA DE FONDOS',
            'TERCERO ENTREGA NUEVO TELEFONO',
            'CLIENTE IRA A LA SUCURSAL',
            'RESPUESTA COBRADOR EN TERRENO',
            'COMPROMISO PAGO - COORDINACION'
        ],
        'Acciones judiciales': [
            'DEUDOR FALLECIDO ( PRESENTA CERTIFICADO )',
            'POSIBLE RECLAMO'
        ]
    }

    # Crear columnas binarias para cada acción
    for accion in accion_dict.keys():
        df_final[accion] = df_final['Descripcion'].apply(
            lambda x: 1 if any(desc in x for desc in accion_dict[accion]) else 0
        )


    # Sumar las columnas binarias para crear una nueva columna 'Cantidad_Gestiones'
    df_final['Cantidad_AccionesCobranza'] = df_final[['Sin acciones', 'Correo electrónico', 'SMS', 'Whatsapp', 'Llamada por bot', 'Llamada directa', 'Acciones judiciales']].sum(axis=1)

    # Sumar todas las columnas de tipo de gestiÃ³n para crear una nueva columna de cantidad de gestiones
    df_final['Cantidad_Gestiones'] = df_final[['TipoGestion_Administrativa',
                                                'TipoGestion_Compromiso',
                                                'TipoGestion_Compromiso-Com',
                                                'TipoGestion_EMAIL',
                                                'TipoGestion_Negativa',
                                                'TipoGestion_Negativa-Com',
                                                'TipoGestion_Positiva',
                                                'TipoGestion_Positiva-Adm',
                                                'TipoGestion_Positiva-Com',
                                                'TipoGestion_Positiva-Indi',
                                                'TipoGestion_Positiva-Wsp',
                                                'TipoGestion_Sistema',
                                                'TipoGestion_Terreno']].sum(axis=1)
    
    # Creamos la columna 'gestion_positiva' basada en la columna 'Pago'
    df_final['gestion_positiva'] = df_final['Pago'].apply(lambda x: 1 if x == 1 else 0)

    # Definir las columnas booleanas a convertir en enteros
    boolean_columns = [
        'homologada_Administrativa', 'homologada_Contacto Directo', 'homologada_Contacto Indirecto',
        'homologada_Herramientas Masivas', 'homologada_Sin Contacto', 'homologada_Sin Gestion',
        'TipoGestion_Administrativa', 'TipoGestion_Compromiso', 'TipoGestion_Compromiso-Com',
        'TipoGestion_EMAIL', 'TipoGestion_Negativa', 'TipoGestion_Negativa-Com',
        'TipoGestion_Positiva', 'TipoGestion_Positiva-Adm', 'TipoGestion_Positiva-Com',
        'TipoGestion_Positiva-Indi', 'TipoGestion_Positiva-Wsp', 'TipoGestion_Sistema',
        'TipoGestion_Terreno'
    ]

    # Convertir las columnas booleanas a enteros
    df_final[boolean_columns] = df_final[boolean_columns].astype(int)
    return df_final

