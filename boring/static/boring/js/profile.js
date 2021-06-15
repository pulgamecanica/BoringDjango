function newGame() {
    openWindow("New Game!")
}
function newPost() {
    openWindow("New Post!")
}
function openShop() {
    openWindow("Shop!")
}
function openSettings() {
    openWindow("Settings!")
}
function showItems() {
    openWindow("Items!")
}
function goBack(params) {
    document.querySelector('#content-selected').innerHTML = "";
    document.querySelector('#content-selected').style.display = "none";
    document.querySelector('#profile-menu').style.display = "block";
}
function openWindow(content) {
    document.querySelector('#profile-menu').style.display = "none";
    document.querySelector('#content-selected').style.display = "block";
    document.querySelector('#content-selected').innerHTML = content;
    let arrow = document.createElement('i');
    arrow.classList.add('fas');
    arrow.classList.add('fa-arrow-left');
    let back = document.createElement('span');
    back.style.position = 'absolute';
    back.style.top = '5px';
    back.style.left = '5px';
    back.addEventListener('click', goBack, false);
    back.appendChild(arrow);
    document.querySelector('#content-selected').appendChild(back);
}