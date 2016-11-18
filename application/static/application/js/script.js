$(document).ready(function(){
	$('.modify').addClass('hide');
	$('#allevent').removeClass('hide');
	$('#all').addClass('active');

	$('.common').click(function(e) {
		e.preventDefault();
		var active = '#' + $(this).attr("id");
		$('.common').removeClass('active');
		$(active).addClass('active');
		var elementId = '#' + $(this).attr("id") + 'event'; 
		$('.modify').addClass('hide');
		$(elementId).removeClass('hide');
	});
});