# hgaas_quart_template

template for a quart app if you want to develop with hgaas


## Features

This project shows how to do several things. Each thing is present in server.py, index.js, and index.html in some way.

1. An API "GET" call with a URL parameter (`/example_url_param/foo`)
2. An API "GET" call with a query parameter (`/example_query_param?param=bar`)
3. An AP "POST" call with a JSON payload (`/example_json_post` `{"param": "baz"}`)
4. Concurrent background jobs / scheduled tasks, run on the server
5. Updating the DOM with javascript based on response data from API call
6. Creating button events


### API GET with URL param

```html
  <span>api call with url param: </span><span class="value" id="url_param_value"></span>
```
```js
  jQuery.get("/example_url_param/foo", function(d) {
    jQuery('#url_param_value').text(d.changed)
  })
```
```python
@app.route("/example_url_param/<param>")
async def example_url_param(param):
  changed_thing = param * (some_global_data%20)
  return jsonify({
    "changed": changed_thing,
  })
```

### API GET with query param
```html
  <span>api call with query param: </span><span class="value" id="query_param_value"></span>
```
```js
  jQuery.get("/example_query_param?param=bar", function(d) {
    jQuery('#query_param_value').text(d.changed)
  })
```
```python
@app.route("/example_query_param")
async def example_query_param():
  param = request.args['param']
  changed_thing = param * (some_global_data%20)
  return jsonify({
    "changed": changed_thing,
  })
```

### API POST with JSON payload
```html
  <span>api post call with json data: </span><span class="value" id="post_param_value"></span>
```
```js
  post("/example_json_post", { param: "baz"}, function(d) {
    jQuery('#post_param_value').text(d.changed)
  })
```
```python
@app.route("/example_json_post", methods=["POST"])
async def example_json_post():
  j = await request.get_json()
  changed_thing = j['param'] * (some_global_data%20)
  return jsonify({
    "changed": changed_thing,
  })
```

### DOM manipulation with API response data
```html
  <span>api call with url param: </span><span class="value" id="url_param_value"></span>
```
```js
  jQuery.get("/example_url_param/foo", function(d) {
    jQuery('#url_param_value').text(d.changed)
  })
```
```python
@app.route("/example_url_param/<param>")
async def example_url_param(param):
  changed_thing = param * (some_global_data%20)
  return jsonify({
    "changed": changed_thing,
  })
```

### Button click event
```html
<button class="do_update">get new values</button>
```
```javascript
jQuery('button.do_update').click(function() { 
  update_values()
})
```

