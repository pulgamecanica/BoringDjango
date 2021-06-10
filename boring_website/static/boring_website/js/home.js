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