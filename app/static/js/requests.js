function requestDetails(input) {
    // close all other tables
    requestDenied(input);
    
    // add active box shadow
    document.getElementById(input).style.boxShadow = '0 0 0 .25rem rgba(49,132,253,.5)';
    
    // show table and change arrow direction
    document.getElementById('persoenlichedatentablebodyoverview').classList.remove('collapse');
    document.getElementById('persoenlichedatenoverviewarrow').classList.remove('fa-chevron-down');
    document.getElementById('persoenlichedatenoverviewarrow').classList.add('fa-chevron-up'); 
}


function requestDenied(input) {
    // remove active box shadow
    document.getElementById(input).style.boxShadow = '';
    
    // collapse all tables
    document.getElementById('persoenlichedatentablebodyoverview').classList.add('collapse');
    document.getElementById('fachlichequalifikationtablebodyoverview').classList.add('collapse');
    document.getElementById('berufserfahrungtablebodyoverview').classList.add('collapse');
    document.getElementById('projekterfahrungtablebodyoverview').classList.add('collapse');
    document.getElementById('weiterbildungentablebodyoverview').classList.add('collapse');
    document.getElementById('geplanteweiterbildungentablebodyoverview').classList.add('collapse');
    document.getElementById('gesundheitsdatentablebodyoverview').classList.add('collapse');
    document.getElementById('interessentablebodyoverview').classList.add('collapse');
    
    // change arrow direction
    document.getElementById('persoenlichedatenoverviewarrow').classList.remove('fa-chevron-up');
    document.getElementById('persoenlichedatenoverviewarrow').classList.remove('fa-chevron-down');
    document.getElementById('persoenlichedatenoverviewarrow').classList.add('fa-chevron-down');
    document.getElementById('fachlichequalifikationoverviewarrow').classList.remove('fa-chevron-up');
    document.getElementById('fachlichequalifikationoverviewarrow').classList.remove('fa-chevron-down');
    document.getElementById('fachlichequalifikationoverviewarrow').classList.add('fa-chevron-down');
    document.getElementById('berufserfahrungoverviewarrow').classList.remove('fa-chevron-up');
    document.getElementById('berufserfahrungoverviewarrow').classList.remove('fa-chevron-down');
    document.getElementById('berufserfahrungoverviewarrow').classList.add('fa-chevron-down');
    document.getElementById('projekterfahrungoverviewarrow').classList.remove('fa-chevron-up');
    document.getElementById('projekterfahrungoverviewarrow').classList.remove('fa-chevron-down');
    document.getElementById('projekterfahrungoverviewarrow').classList.add('fa-chevron-down');
    document.getElementById('weiterbildungoverviewarrow').classList.remove('fa-chevron-up');
    document.getElementById('weiterbildungoverviewarrow').classList.remove('fa-chevron-down');
    document.getElementById('weiterbildungoverviewarrow').classList.add('fa-chevron-down');
    document.getElementById('geplanteweiterbildungoverviewarrow').classList.remove('fa-chevron-up');
    document.getElementById('geplanteweiterbildungoverviewarrow').classList.remove('fa-chevron-down');
    document.getElementById('geplanteweiterbildungoverviewarrow').classList.add('fa-chevron-down');
    document.getElementById('gesundheitsdatenoverviewarrow').classList.remove('fa-chevron-up');
    document.getElementById('gesundheitsdatenoverviewarrow').classList.remove('fa-chevron-down');
    document.getElementById('gesundheitsdatenoverviewarrow').classList.add('fa-chevron-down');
    document.getElementById('interessenoverviewarrow').classList.remove('fa-chevron-up');
    document.getElementById('interessenoverviewarrow').classList.remove('fa-chevron-down');
    document.getElementById('interessenoverviewarrow').classList.add('fa-chevron-down');
}


// add collapse to all requests
$('.myrequests_hide').addClass('collapse');

// on change hide all divs linked to select and show only linked to selected option
$('#myselector').change(function(){
    // saves in a variable the wanted div
    var selector = '.select_opt_' + $(this).val();
    
    // hide all elements
    $('.myrequests_hide').collapse('hide');

    // show only element connected to selected option
    $(selector).collapse('show');
});

function userMessage(user_id) {
    document.getElementById('hidden_user_id').value = document.getElementById(user_id).value
    $("#modal-message").modal("show");
};

function userMessageReply(current_field) {
    let id = current_field.parentNode.parentNode.id.slice(12);
    let category = current_field.children[0].children[0].textContent;
    let date = current_field.children[0].children[1].textContent;
    let body = current_field.children[1].textContent;
    let recruiter_id = current_field.children[2].value;
    // fill data
    document.getElementById('hidden_user_id').value = id
    document.getElementById('message_category').textContent = category
    document.getElementById('message_time').textContent = date
    document.getElementById('message_body').textContent = body
    document.getElementById('hidden_recruiter_id').value = recruiter_id
    // show modal
    $("#modal-message").modal("show");
};
