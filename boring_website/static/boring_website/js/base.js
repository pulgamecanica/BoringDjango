document.addEventListener("DOMContentLoaded", function(event) {
	for(let a of document.querySelector('#navBar').firstElementChild.children){
		a.classList.remove('active')
	}
	if (document.querySelector('#home-active')) {
		document.querySelector('#navBar').firstElementChild.children[1].classList.add('active')
	}else if (document.querySelector('#about-active')) {
		document.querySelector('#navBar').firstElementChild.children[2].classList.add('active')
	}else if (document.querySelector('#games-active')) {
		document.querySelector('#navBar').firstElementChild.children[3].classList.add('active')
	}else if (document.querySelector('#posts-active')) {
		document.querySelector('#navBar').firstElementChild.children[4].classList.add('active')
	}else if (document.querySelector('#faq-active')) {
		document.querySelector('#navBar').firstElementChild.children[5].classList.add('active')
	}
});