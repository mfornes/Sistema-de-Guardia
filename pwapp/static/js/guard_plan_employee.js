$(document).ready(function () {    

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

    $('#todos tbody').on('click', 'tr', function (event) {
        $(this).toggleClass('selected highlight');
    });

    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
    
    $("#primerTurno").click(function () {    

        let url = $("#primerTurno").attr("data-url");
        $.ajax({
            url: url,
            type: "GET",
            dataType: "json",
            crossDomain: false,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            success: (response) => {

                $("#todos tbody").html('');

                (response.context).forEach(item => {
                    $("#todos tbody").append(`<tr id="${item.id}">
                        <td>${item.name || "-"}</td>
                        <td>${item.last_name || "-"}</td>                   
                    </tr>`)
                });

                const myModal = new bootstrap.Modal(document.getElementById('exampleModal'), {})

                myModal.show()

                $('#aceptarListado').click(function () {

                    $("#todos tbody tr.selected").each(function (index, value) {                    
                        $(this).append('<td><button type="button" class="btn btn-outline-danger btnDelete">Eliminar</button></td>');
                        $(this).removeClass("selected highlight");
                        $("#listPrimerTurno tbody").append(value)
                    });

                    myModal.hide()
                });

                $("#listPrimerTurno tbody").on('click', '.btnDelete', function () {
                    $(this).closest('tr').remove();
                });
            },
            error: (error) => {
                console.log(error);
            }
        });
    });

    $('#todos1 tbody').on('click', 'tr', function () {
        $(this).toggleClass('selected highlight');
    });

    $("#segundoTurno").click(function () {
        let url = $("#segundoTurno").attr("data-url");
        const payload = {
            local: $("#id_local")[0].value,       
        }
        $.ajax({
            url: url,
            type: "GET",
            dataType: "json",
            crossDomain: false,
            data: payload,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            success: (response) => {

                $("#todos1 tbody").html('');

                (response.context).forEach(item => {
                    $("#todos1 tbody").append(`<tr id="${item.id}">
                        <td>${item.name || "-"}</td>
                        <td>${item.last_name || "-"}</td>                   
                    </tr>`)
                });

                const myModal = new bootstrap.Modal(document.getElementById('exampleModal1'), {})

                myModal.show()               

                $('#aceptarListado1').click(function () {

                    $("#todos1 tbody tr.selected").each(function (index, value) {                    
                        $(this).append('<td><button type="button" class="btn btn-outline-danger btnDelete">Eliminar</button></td>');
                        $(this).removeClass("selected highlight");
                        $("#listSegundoTurno tbody").append(value)
                    });

                    myModal.hide()
                });

                $("#listSegundoTurno tbody").on('click', '.btnDelete', function () {
                    $(this).closest('tr').remove();
                });
            },
            error: (error) => {
                console.log(error);
            }
        });
    });

    $("#createGP").click(function () {

        let url = $("#createGP").attr("data-url");
        let listPrimerTurno = [];
        let listSegundoTurno = [];

        $("#listPrimerTurno tbody tr").each(function (index, value) {                    
            listPrimerTurno.push(value.id)
        });

        $("#listSegundoTurno tbody tr").each(function (index, value) {                    
            listSegundoTurno.push(value.id)
        });

        const payload = {
            date:  $("#id_date")[0].value,
            local: $("#id_local")[0].value,
            listPrimerTurno: listPrimerTurno,
            listSegundoTurno: listSegundoTurno, 
        }
        $("#spinner-div").show();
        $.ajax({
            url: url,
            type: "POST",
            dataType: "json",
            data: JSON.stringify({payload: payload,}),
            headers: {
              "X-Requested-With": "XMLHttpRequest",
              "X-CSRFToken": getCookie("csrftoken"),
            },
            success: (data) => {
                if(data.status == 1){ 
                    window.location.pathname = "guard_plan_employee";
                 }
            },
            error: (error) => {
              console.log(error);
            },
            complete: function () {
                $("#spinner-div").hide();
              }          
          });
    });   

    $("#updateListPrimerTurno tbody").on('click', '.btnDelete', function () {
        $(this).closest('tr').remove();
    });


    $('#updateList tbody').on('click', 'tr', function () {
        $(this).toggleClass('selected highlight');
    });

    $("#updatePrimerTurno").click(function () {
        let url = $("#updatePrimerTurno").attr("data-url");
        $.ajax({
            url: url,
            type: "GET",
            dataType: "json",
            crossDomain: false,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            success: (response) => {

                $("#updateList tbody").html('');

                (response.context).forEach(item => {
                    $("#updateList tbody").append(`<tr id="${item.id}">
                        <td>${item.name || "-"}</td>
                        <td>${item.last_name || "-"}</td>                   
                    </tr>`)
                });

                const myModal = new bootstrap.Modal(document.getElementById('exampleModal'), {})

                myModal.show()

                $('#updateAceptarListado').click(function () {

                    $("#updateList tbody tr.selected").each(function (index, value) {                    
                        $(this).append('<td><button type="button" class="btn btn-outline-danger btnDelete">Eliminar</button></td>');
                        $(this).removeClass("selected highlight");
                        $("#updateListPrimerTurno tbody").append(value)
                    });

                    myModal.hide()
                });                
            },
            error: (error) => {
                console.log(error);
            }
        });       
    });
   
    $("#updateListSegundoTurno tbody").on('click', '.btnDelete', function () {
        $(this).closest('tr').remove();
    });

    $('#updateList1 tbody').on('click', 'tr', function () {
        $(this).toggleClass('selected highlight');
    });

    $("#updateSegundoTurno").click(function () {
        let url = $("#updateSegundoTurno").attr("data-url");

        const payload = {
            local: $("#updateLocal").attr("for"),    
        }
        $.ajax({
            url: url,
            type: "GET",
            dataType: "json",
            crossDomain: false,
            data: payload,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            success: (response) => {

                $("#updateList1 tbody").html('');

                (response.context).forEach(item => {
                    $("#updateList1 tbody").append(`<tr id="${item.id}">
                        <td>${item.name || "-"}</td>
                        <td>${item.last_name || "-"}</td>                   
                    </tr>`)
                });

                const myModal = new bootstrap.Modal(document.getElementById('exampleModal1'), {})

                myModal.show()              

                $('#updateAceptarListado1').click(function () {

                    $("#updateList1 tbody tr.selected").each(function (index, value) {                    
                        $(this).append('<td><button type="button" class="btn btn-outline-danger btnDelete">Eliminar</button></td>');
                        $(this).removeClass("selected highlight");
                        $("#updateListSegundoTurno tbody").append(value)
                    });

                    myModal.hide()
                });
               
            },
            error: (error) => {
                console.log(error);
            }
        });      
    });

    $("#updateGP").click(function () {

        let url = $("#updateGP").attr("data-url");
        let listPrimerTurno = [];
        let listSegundoTurno = [];

        $("#updateListPrimerTurno tbody tr").each(function (index, value) {                    
            listPrimerTurno.push(value.id)
        });

        $("#updateListSegundoTurno tbody tr").each(function (index, value) {                    
            listSegundoTurno.push(value.id)
        });

        const payload = {
            listPrimerTurno: listPrimerTurno,
            listSegundoTurno: listSegundoTurno,
        }
        $("#spinner-div").show();

        $.ajax({
            url: url,
            type: "PUT",
            dataType: "json",
            data: JSON.stringify({payload: payload,}),
            headers: {
              "X-Requested-With": "XMLHttpRequest",
              "X-CSRFToken": getCookie("csrftoken"),
            },
            success: (data) => {
              console.log(data);
              if(data.status == 1){ 
                const myToast =  new bootstrap.Toast(document.getElementById('mytoast'), {});
                myToast.show()
             }  
            },
            error: (error) => {
              console.log(error);
            },
            complete: function () {
                $("#spinner-div").hide();
              }
          });
    }); 

});