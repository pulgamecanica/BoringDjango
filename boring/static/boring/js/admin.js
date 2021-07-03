document.addEventListener("DOMContentLoaded", function(event) {
    document.querySelectorAll('input').forEach(input => input.classList.add('form-control'));
});
function showAdminPannel(section_name) {
    let sections = document.querySelector('#admin-sections-container').children;
    for (let index = 0; index < sections.length; index++) {
        sections[index].style.display = "none";
    }
    document.querySelector('#'+section_name).style.display = "block";
};