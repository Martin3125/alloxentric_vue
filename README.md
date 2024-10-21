# Proyecto: Optimizador de Cobraza (Alloxentric)

![Logo del proyecto](https://alloxentric.com/wp-content/uploads/2020/11/alloxentric_logo-3x.png) ![alt text](https://www.duoc.cl/wp-content/uploads/2022/09/logo-0.png)

Integrantes: 
* Víctor Silva
* Martín Soto 

## Resumen del Proyecto
El proyecto tiene como objetivo desarrollar un modelo de machine learning para segmentar a los clientes morosos en diferentes grupos, según su comportamiento de pago, y luego predecir la mejor acción de cobranza para cada grupo. Se implementará en dos etapas:

1. Segmentación de Clientes con K-Means:
Se usará el algoritmo K-Means para agrupar a los clientes en clústeres, basándose en características como el historial de pagos, monto de la deuda, tiempo de morosidad, entre otras variables relevantes. Esto permitirá identificar patrones comunes en los comportamientos de los clientes, facilitando el diseño de estrategias de cobranza personalizadas para cada grupo.

2. Predicción de Acciones con LSTM:
En la segunda etapa, se implementará un modelo LSTM (Long Short-Term Memory) para predecir la probabilidad de éxito de diferentes acciones de cobranza (por ejemplo, llamadas, mensajes de texto, llamadas automáticas) para cada grupo de clientes. LSTM es adecuado para este propósito debido a su capacidad para manejar datos secuenciales y capturar relaciones a largo plazo en el comportamiento de los clientes.

## Despliegue del ambiente de desarrollo (Alloxentric)
Para poder ejecutar el ambiente de desarrollo se debe tomar en cuenta los siguientes pasos:

1. Instalar Node.js
2. Intalar Mongo DB Compass
3. Ejecutar el npm install
4. Ejecutar pip install fastapi uvicorn pymongo pydantic
5. Ejecutar uvicorn data_base:app --reload
6. Ejecutar npm run dev

## Configuración Recomendada del IDE 

[Node.js](https://nodejs.org/en)

[MongoDB](https://www.mongodb.com/products/tools/compass)

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Personalizar la Configuración

See [Vite Configuration Reference](https://vitejs.dev/config/).


## Configuración del Proyecto
Instala todas las dependencias necesarias 
```sh
npm install
```
### Servidor local
Se debe instalar en caso de no tener uvicorn
```sh
pip install fastapi uvicorn pymongo pydantic
```
Ejecuta el servidor local
```sh
uvicorn data_base:app --reload
```

### Compilación y Recarga Automática para Desarrollo

```sh
npm run dev
```

### Compilación y Minificación para Producción

```sh
npm run build
```

### Lint con [ESLint](https://eslint.org/)

```sh
npm run lint
```

## Fases del Capstone 2024 

El proyecto de Capstone se divide en las siguientes fases:

* FASE 1: Definición proyecto APT (Semana 1 a 4)
* FASE 2: Desarrollo proyecto APT (Semana 5 a 15)
* FASE 3: Presentación Proyecto APT (Semana 16 a 18)

El proyecto tiene una duración de 18 semanas donde se debe tener termniando el proyecto en la semana 15.