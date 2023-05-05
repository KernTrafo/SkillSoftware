function addUserSkill() {
    let x = document.getElementById('skills_input').value.toLowerCase();
    if (x == '') {
    }
    else {
        // add skill to skill list
        document.getElementById('skills_menu').insertAdjacentHTML('beforeend', '<button class="btn btn-primary recommendation-button selected" id="' + x + '" type="button" onclick="removeUserSkill(this.id)">' + x + '<i class="fas fa-minus"></i></button>');
        document.getElementById('skills_menu').insertAdjacentHTML('beforeend', '<input class="d-none data-input-field w-100" id="checkbox_' + x + '" name="user_skills_checkbox" onkeydown="return event.key != &quot;Enter&quot;;" type="text" value="' + x + '"></input>');
    }
    // clean input
    document.getElementById('skills_input').value = ''
}


// add recommended user skills
function addUserSkillRecommendation(skill) {
    // get text of recommended item
    let x = document.getElementById(skill).textContent;
    // remove from recommendations
    document.getElementById(skill).remove(); 
    // add skill to selected list
    document.getElementById('skills_menu').insertAdjacentHTML('beforeend', '<button class="btn btn-primary recommendation-button selected" id="' + x + '" type="button" onclick="removeUserSkill(this.id)">' + x + '<i class="fas fa-minus"></i></button>');
    document.getElementById('skills_menu').insertAdjacentHTML('beforeend', '<input class="d-none data-input-field w-100" id="checkbox_' + x + '" name="user_skills_checkbox" onkeydown="return event.key != &quot;Enter&quot;;" type="text" value="' + x + '"></input>');
}


// remove skill from user skill list
function removeUserSkill(skill) {
    // get skill name
    let x = document.getElementById(skill).textContent;
    // remove from selected items
    document.getElementById(skill).remove(); 
    document.getElementById('checkbox_' + skill).remove(); 
    // add back to recommendations
    document.getElementById('vorgeschlageneuserskills').insertAdjacentHTML('beforeend', '<button class="btn btn-primary recommendation-button" id="' + skill + '" type="button" onclick="addUserSkillRecommendation(this.id)">' + x + '<i class="fas fa-plus"></i></button>');
}
