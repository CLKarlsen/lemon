$(document).ready(function(){

	$(".add-likes-link").click(function(event) {
		event.preventDefault();
		var message_id = $(this).data("messageid");
		var likes_element_id = "#id-likes-for-message-" + message_id;
		$.ajax({
			url: "/lemon_messages/" + message_id + "/add_likes"
		})
		.done(function(data) {
			var likes_updated = data['likes_updated'];
			$(likes_element_id).html(likes_updated);
		});
	});
});