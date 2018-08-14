$(document).ready(function(){
	$("#d1").on("input",function(){
		var para1 = $("#d1").val();

		$.ajax({
			url: '/d1/',
			method: 'POST',
			data: {
				  'd1': para1
				},
					
			success: function (data) {
				$('#doc1').contents().find('#target1').html(data);
				  
					}
				});		
			});
		
	$("#d2").on("input",function(){
		
		var para2 = $("#d2").val();
		$.ajax({
			url: '/d2/',
			method: 'POST',
			data: {
				  'd2': para2
				},
					
			success: function (data) {
				
				$('#doc2').contents().find('#target2').html(data);
				  
					}
				});		
			});	
		
		});
