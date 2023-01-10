// jQuery.post doesn't set the right contentType for Quart, so we gotta do this
function post(url, data, fn) {
  jQuery.ajax({
    type: "POST",
    contentType: "application/json; charset=utf-8",
    url: url, 
    data: JSON.stringify(data), 
    success: fn
  })
}


function update_values() {
  jQuery.get("/example_url_param/foo", function(d) {
    jQuery('#url_param_value').text(d.changed)
  })


  jQuery.get("/example_query_param?param=bar", function(d) {
    jQuery('#query_param_value').text(d.changed)
  })


  post("/example_json_post", { param: "baz"}, function(d) {
    jQuery('#post_param_value').text(d.changed)
  })
}

update_values() // set initial values

jQuery('button.do_update').click(function() { 
  update_values()
})
