$(document).ready(function(){
	$('.modify').addClass('hide');
	$('#allevent').removeClass('hide');

	$('.common').click(function(e) {
		e.preventDefault();
		var elementId = '#' + $(this).attr("id") + 'event'; 
		$('.modify').addClass('hide');
		$(elementId).removeClass('hide');
	});
});