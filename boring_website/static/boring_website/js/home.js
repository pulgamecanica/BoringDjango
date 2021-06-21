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
function collapse(colName) {
	let coll = document.getElementsByClassName("collapsible-"+colName);
	let i;
	for (i = 0; i < coll.length; i++) {
	    coll[i].classList.toggle("active-collapsible");
	    let content = coll[i].nextElementSibling;
	    if (content.style.display === "block") {
	      content.style.display = "none";
	    } else {
	      content.style.display = "block";
	    }
	}
}