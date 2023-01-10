# hgaas_quart_template

template for a quart app if you want to develop with hgaas


## Features

This project shows how to do several things. Each thing is present in server.py, index.js, and index.html in some way.

1. An API "GET" call with a URL parameter (`/example_url_param/foo`)
2. An API "GET" call with a query parameter (`/example_query_param?param=bar`)
3. An API "POST" call with a JSON payload (`/example_json_post` `{"param": "baz"}`)
4. Updating the DOM with javascript based on response data from API call
5. Creating button events
6. Concurrent background jobs / scheduled tasks, run on the server


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

### Concurrent Background Jobs on Server

```python
some_global_data = 1
async def run_background_job():
  global some_global_data
  import random
  while running:
    # sets some_global_data to a random number once per second
    some_global_data = 2*random.randint(1,10)
    print("background job: ", some_global_data)
    await asyncio.sleep(1)

# ...

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        app.run_task(host="0.0.0.0", port=8094),
        run_background_job(),
        # put your other infinite-loop coroutines down here
    ))
```

A background job is defined as an `async function`. The function must have a while or for loop in it. For most purposes, you'll use `await asyncio.sleep(duration)`. If your background job reads from an async source, like an async blocking queue or something, you can use that. I recommend an `asyncio.sleep(0.1)` at least. If this function winds up not returning the thread to asyncio, it will lock up your application. 



# Single HTML file version

It's my personal preference to keep html, javascript, and css in one simple short HTML file, so I've provided an additional version.

`public/singlepage_index.html`

It's accessible at <http://localhost:8094/public/singlepage_index.html>
