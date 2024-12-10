export function initializeFilter() {
    document.addEventListener('DOMContentLoaded', function() {
        const filterContainer = document.getElementById('filterContainer');
        const toggleButton = document.getElementById('toggleFilterButton');

        toggleButton.addEventListener('click', function() {
            if (filterContainer.style.display === 'none' || filterContainer.style.display === '') {
                filterContainer.style.display = 'block';
                toggleButton.textContent = 'Ocultar Filtro';
            } else {
                filterContainer.style.display = 'none';
                toggleButton.textContent = 'Mostrar Filtro';
            }
        });

        document.getElementById('filterForm').addEventListener('submit', function(event) {
            event.preventDefault();
            
            const formData = new FormData(event.target);
            const selectedActions = formData.getAll('action');

            console.log('Acciones seleccionadas:', selectedActions);

            // Aquí puedes añadir la lógica para filtrar los datos en función de las acciones seleccionadas
            // Por ejemplo, podrías realizar una petición AJAX para obtener los datos filtrados desde el servidor
            fetchData(selectedActions);
        });
        
        //filtro por fechas
        document.getElementById('filterForm').addEventListener('submit', function(event) {
            event.preventDefault();
            
            const formData = new FormData(event.target);
            const selectedActions = formData.getAll('action');
            const fechaEnvio = formData.get('fecha_envio');
            const fechaPagoEstimado = formData.get('fecha_pago_estimado');
            const fechaPagoReal = formData.get('fecha_pago_real');

            console.log('Acciones seleccionadas:', selectedActions);
            console.log('Fecha de envío:', fechaEnvio);
            console.log('Fecha de pago estimada:', fechaPagoEstimado);
            console.log('Fecha real del pago:', fechaPagoReal);

            // Aquí puedes añadir la lógica para filtrar los datos en función de las acciones seleccionadas y las fechas
            // Por ejemplo, podrías realizar una petición AJAX para obtener los datos filtrados desde el servidor
            fetchData(selectedActions, fechaEnvio, fechaPagoEstimado, fechaPagoReal);
        });

        function fetchData(actions, fechaEnvio, fechaPagoEstimado, fechaPagoReal) {
            // Suponiendo que la URL del API sea 'https://example.com/api/documentos'
            // y que puedas enviar las acciones seleccionadas y las fechas como parámetros de consulta (query parameters)
            let url = 'https://example.com/api/documentos';
            const params = new URLSearchParams();

            if (actions.length > 0) {
                params.append('actions', actions.join(','));
            }
            if (fechaEnvio) {
                params.append('fecha_envio', fechaEnvio);
            }
            if (fechaPagoEstimado) {
                params.append('fecha_pago_estimado', fechaPagoEstimado);
            }
            if (fechaPagoReal) {
                params.append('fecha_pago_real', fechaPagoReal);
            }

            if (params.toString()) {
                url += '?' + params.toString();
            }

            fetch(url)
                .then(response => response.json())
                .then(data => populateTable(data))
                .catch(error => console.error('Error fetching data:', error));
        }

        //filtro por acciones de cobranza
        function fetchData(actions) {
            // Suponiendo que la URL del API sea 'https://example.com/api/documentos'
            // y que puedas enviar las acciones seleccionadas como parámetros de consulta (query parameters)
            let url = 'https://example.com/api/documentos';
            if (actions.length > 0) {
                url += '?actions=' + actions.join(',');
            }

            fetch(url)
                .then(response => response.json())
                .then(data => populateTable(data))
                .catch(error => console.error('Error fetching data:', error));
        }

        function populateTable(data) {
            const tbody = document.querySelector('#documentTable tbody');
            tbody.innerHTML = ''; // Limpiar la tabla antes de añadir nuevas filas

            data.forEach(doc => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${doc.id}</td>
                    <td>${doc.nombre}</td>
                    <td>${doc.fecha}</td>
                    <td>${doc.registro_gente}</td>
                    <td>${doc.tipo_de_acción}</td>
                    <td>${doc.cantidad_gente_contactar}</td>
                    <td><a href="${doc.descargar}" download>Descargar</a></td>
                `;
                tbody.appendChild(row);
            });
        }

        // Inicializar la tabla con datos sin filtrar
        fetchData([]);
    });
}