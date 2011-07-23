function buttonDropdownCombo(button, dialog, width) {
	var dropDown = $("#" + dialog);
	button = "#" + button;
	dropDown.dialog({
		autoOpen: false,
		dialogClass: "ui-no-header",
		draggable: false,
		resizable: false,
	});
	if(width) dropDown.dialog("option", "width", width);
	$(button + " a").button({
		icons: {
			secondary: "ui-icon-triangle-1-s"
		}
	}).click(function() {
		dropDown.dialog("isOpen") ? dropDown.dialog("close") : dropDown.dialog("open");
		dropDown.dialog("widget").position({
			my: "left top",
			at: "left bottom",
			of: $(button)
		});
	});
	$(".ui-no-header .closeButton span").click(function() {
		dropDown.dialog("close");
	});
}
