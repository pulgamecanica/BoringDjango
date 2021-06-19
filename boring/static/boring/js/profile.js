document.addEventListener("DOMContentLoaded", function(event) {
    if (!(document.querySelector('#content-selected') === null)) {
        let arrow = document.createElement('i');
        arrow.id = "arrow-back"
        arrow.classList.add('fas');
        arrow.classList.add('fa-arrow-left');
        let back = document.createElement('span');
        back.style.position = 'absolute';
        back.style.top = '5px';
        back.style.left = '5px';
        back.addEventListener('click', goBack, false);
        back.appendChild(arrow);
        arrow.style.display = 'none'
        document.querySelector('#content-selected').appendChild(back);   
    }
    document.querySelectorAll('input').forEach(input => {
        input.classList.add('form-control');
        input.style.marginBottom = "1rem";
    });
    document.querySelectorAll('label').forEach(label => {
        label.classList.add('form-control');
        label.style.marginBottom = 0;
    });
    document.querySelectorAll('select').forEach(select => {
        select.classList.add('form-control');
        select.style.marginBottom = "1rem";
    });
    document.querySelectorAll('textarea').forEach(textarea => {
        textarea.classList.add('form-control');
        textarea.style.marginBottom = "1rem";
        textarea.style.height = "100px";
    });
});
function newGame() {
    openWindow("New Game!");
    showElement('game-form');
}
function newPost() {
    openWindow("New Post!");
    showElement('post-form');
}
function openShop() {
    openWindow("Shop!");
}
function openSettings() {
    openWindow("Settings");
    showElement('settings-form');

}
function showItems() {
    openWindow("Your Items!");
    showElement("items-collection");
}
function goBack(params) {
    document.querySelector('#content-selected-header').innerHTML = "";
    document.querySelector('#content-selected').style.display = "none";
    document.querySelector('#profile-menu').style.display = "block";
}
function openWindow(content) {
    document.querySelector('#profile-menu').style.display = "none";
    document.querySelector('#content-selected').style.display = "block";
    document.querySelector('#content-selected-header').innerHTML = content;
    document.querySelector('#arrow-back').style.display = 'block';
}
function showElement(name) {
    document.querySelectorAll('.form').forEach(form => form.style.display = 'none');
    document.querySelector('#'+name).style.display = 'block';
}