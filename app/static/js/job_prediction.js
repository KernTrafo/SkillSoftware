// add missing user skill to user skill list
function addMissingPredictionSkill(input) {
    let x = input.parentNode.parentNode.firstChild.textContent;    

    // add skill to skill list    
    document.getElementById('skills_menu').insertAdjacentHTML('beforeend', '<button class="btn btn-primary recommendation-button selected" id="' + x + '" type="button" onclick="removeUserSkill(this.id)">' + x + '<i class="fas fa-minus"></i></button>');
    document.getElementById('skills_menu').insertAdjacentHTML('beforeend', '<input class="d-none data-input-field w-100" id="checkbox_' + x + '" name="user_skills_checkbox" onkeydown="return event.key != &quot;Enter&quot;;" type="text" value="' + x + '"></input>');
    document.getElementById('skills-save-button').click();
}

function analyzeSkill(skill) {
    // enter skill into analysis input field
    document.getElementById('analyseinput').value = skill.slice(11);
    document.getElementById('analyse-button').click();
};

function jobDetails(job) {
    document.getElementById('job_details_text').textContent = 'Haben Sie Interesse an der Position ' + job + '?';
    document.getElementById('job_details_text').value = job;
    $('#modal-prediction').modal('show');
};

function contactRecruiter() {
    let x = document.getElementById('job_details_text').value
    document.getElementById('predictioncontact_subject').value = 'Anfrage ' + x;
    $('#modal-prediction').modal('hide');
    $('#modal-message').modal('show');
};
