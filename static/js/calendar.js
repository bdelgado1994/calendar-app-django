
const modal = document.getElementById("eventModal")
const eventForm = document.getElementById('eventForm');
// Función para limpiar los inputs del formulario
function clearForm() {
    eventForm.reset();  // Limpia todos los campos del formulario
    document.getElementById('btnDelete').style.display = 'none';  // Oculta el botón de eliminar
}
modal.addEventListener('hidden.bs.modal', function () {
    clearForm();
});
function formatDateForInput(dateString) {
    // Parsear la fecha en formato ISO 8601
    let date = new Date(dateString);

    // Extraer el año, mes, día, hora y minutos
    let year = date.getFullYear();
    let month = String(date.getMonth() + 1).padStart(2, '0'); // Meses de 0-11
    let day = String(date.getDate()).padStart(2, '0');
    let hours = String(date.getHours()).padStart(2, '0');
    let minutes = String(date.getMinutes()).padStart(2, '0');

    // Formatear la fecha en el formato que espera el input
    return `${year}-${month}-${day}T${hours}:${minutes}`;
}
document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    let calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale:"es",
        timeZone: 'UTC',
        themeSystem: 'bootstrap5',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
          }, // Esto aplicará el tema de Bootstrap 5 si se usa el CSS de Bootstrap 5
        editable: true,
        droppable: true,
        dateClick: function (info) {
            let myModal = new bootstrap.Modal(modal);
            myModal.show();
        },
        eventClick: function (info) {
            const eventId = info.event.id
            fetch(`/edit-event/${eventId}/`).then(response => response.json())
            .then(data => {
                eventForm.action = `${edit_url}`.replace('0', eventId);
                document.getElementById('id_title').value = data.title;
                document.getElementById('id_description').value = data.description;
                document.getElementById('id_initial_date').value = formatDateForInput(data.initial_date);
                document.getElementById('id_final_date').value = formatDateForInput(data.final_date);
                const deleteBtn = document.getElementById('btnDelete');
                deleteBtn.style.display = 'block';
                deleteBtn.href=`${delete_url}`.replace("0",eventId);
                let myModal = new bootstrap.Modal(modal);
                myModal.show();
            })
            
        }
    });

    calendar.render();
    fetch(url_get)
    .then(response => response.json())
    .then(data => {
        data.forEach(evento => {
            calendar.addEvent({
                id:evento.id,
                title: evento.title,
                start: evento.initial_date,
                end: evento.final_date,
                description: evento.description
            });
        });
    })
    .catch(error => console.error('Error al cargar los eventos:', error));
});