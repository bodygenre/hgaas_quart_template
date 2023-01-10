from quart import Quart, request, render_template, jsonify
import asyncio
import datetime


app = Quart(__name__, static_url_path='/public', static_folder='public', template_folder='public')

running = True



# Background Jobs

some_global_data = 1
async def run_background_job():
  global some_global_data
  import random
  while running:
    # sets some_global_data to a random number once per second
    some_global_data = 2*random.randint(1,10)
    print("background job: ", some_global_data)
    await asyncio.sleep(1)


# Basic Routes

@app.route("/")
async def index():
  return await render_template('index.html', cachebust=datetime.datetime.now().timestamp())


last_restart_time = str(datetime.datetime.now())
@app.route("/last_restart")
def last_restart():
  return last_restart_time


# API Endpoints

@app.route("/example_url_param/<param>")
async def example_url_param(param):
  changed_thing = param * (some_global_data%20)
  return jsonify({
    "changed": changed_thing,
  })

  
@app.route("/example_query_param")
async def example_query_param():
  param = request.args['param']
  changed_thing = param * (some_global_data%20)
  return jsonify({
    "changed": changed_thing,
  })

  
@app.route("/example_json_post", methods=["POST"])
async def example_json_post():
  j = await request.get_json()
  changed_thing = j['param'] * (some_global_data%20)
  return jsonify({
    "changed": changed_thing,
  })





@app.while_serving
async def server_wrapper():
    global running
    yield
    running = False

  
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        app.run_task(host="0.0.0.0", port=8094),
	    run_background_job(),
        # put your other infinite-loop coroutines down here
    ))

