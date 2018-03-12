window.onload=function(){
	 setImgHeight();//set the height according to the width, the rate is 4:3[noData.jpg]
}
//be activated when browser's size is changed
window.onresize=function(){
	 setImgHeight();//set the height according to the width, the rate is 4:3[noData.jpg]
}
//set the selectchange event of category selectpicker
function selectOnChange1(obj){
	var value = obj.options[obj.selectedIndex].value;
	showMaps("tmi1","hottest",value);
}
function selectOnChange2(obj){
	var value = obj.options[obj.selectedIndex].value;
	showMaps("tmi2","latest", value);
}
function showCategorys(language){
	var url = "/getCategory/";
	var data = null;
	var csrftoken = getCookie('csrftoken');
	$.ajax({
		url: url,
		async: false,
		cache: false,
		type: "POST",
        data: {
            language: language
        },
		success: function (res) {
			data = $.parseJSON(res);
		},
		beforeSend: function(xhr, settings) {
		  xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	});
	var selectHTML = "";
	for(category in data){
		var categoryid = parseInt(category);
		var categorydescription = data[category][0];
		selectHTML += "<option value="+categoryid+">"+categorydescription+"</option>"
	}
	$("#category1").append(selectHTML);
	$("#category2").append(selectHTML);
    $("#category1").selectpicker('refresh');
    $("#category2").selectpicker('refresh');
}
function showMaps(divIdPrefix, type, category){
	var result = null;
	var url = "/getMostMaps/";
	var csrftoken = getCookie('csrftoken');
	$.ajax({
		url: url,
		async: false,
		type: "POST",
		data: {
			category: category,
			type: type
		},
		success: function (res) {
			result = $.parseJSON(res);
		},
		beforeSend: function(xhr, settings) {
		  xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	});
	for(var i = 0; i< 6; i++)
	{
		var mapname, curdiv, imgurl, mapurl, img;
		if(result[i] != null)
		{
			mapname = result[i][0];
			curdiv = divIdPrefix + (i+1);
			imgurl = result[i][1];
			mapurl = result[i][2];
			img = $("#"+curdiv).find("img");
			$("#"+curdiv).attr("onclick","location='"+mapurl+"'");
			$("#"+curdiv).children("p").text(mapname);
			
            if(type=="admin"){
                if (mapname=="李白行迹图") {
                    imgurl =window.location.href+"uploaded/admingif/libai.gif"
                }else if (mapname=="杜甫行迹图") {
                    imgurl =window.location.href+"uploaded/admingif/dufu.gif"
                }else if (mapname=="汤显祖行迹图") {
                    imgurl =window.location.href+"uploaded/admingif/tangxianzu.gif"                  
                }else if (mapname=="全宋文专题") {
                    imgurl =window.location.href+"uploaded/admingif/quansongwen.gif"                 
                }else if (mapname=="清代妇女作家专题图") {
                    imgurl =window.location.href+"uploaded/admingif/qingdaifunv.gif"                   
                }
            }

            img.attr("src",imgurl);
		}
		else
		{
			curdiv = divIdPrefix + (i+1);
			img = $("#"+curdiv).find("img");
			if(typeof($("#"+curdiv).attr("onclick"))!="undefined")
			{
				$("#"+curdiv).removeAttr("onclick");
				$("#"+curdiv).children("p").text("");
				img.attr("src","{{ STATIC_URL }}img/noData.jpg");
			}
		}
	}
}
// get cookie value from cookies
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
function setImgHeight() {
	var imgs = $(".picItem");
	imgs.each(function (i) {
		var img = $(this);
		var width = img.width();
		var height = width* 0.75;
		img.height(height);
	});
    var imgs = $(".item");
    imgs.each(function (i) {
        var img = $(this);
        var width = img.width();
        var height = width* 0.75;
        img.height(height);
    });
}
    