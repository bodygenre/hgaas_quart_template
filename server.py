from quart import Quart, request, render_template, jsonify
import asyncio
import datetime




app = Quart(__name__, static_url_path='/public', static_folder='public', template_folder='public')


@app.route("/")
async def index():
  return await render_template('index.html', cachebust=datetime.datetime.now().timestamp())


@app.route("/example_url_param/<param>")
async def example_url_param(param):
  changed_thing = param * 20
  return jsonify({
    "changed": changed_thing,
  })

  
@app.route("/example_query_param")
async def example_query_param():
  param = request.args['param']
  changed_thing = param * 20
  return jsonify({
    "changed": changed_thing,
  })

  
@app.route("/example_json_post", methods=["POST"])
async def example_json_post():
  j = await request.get_json()
  print(j)
  changed_thing = j['param'] * 20
  return jsonify({
    "changed": changed_thing,
  })

  
last_restart_time = str(datetime.datetime.now())
@app.route("/last_restart")
def last_restart():
  return last_restart_time



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        app.run_task(host="0.0.0.0", port=8094),
        # put your other infinite-loop coroutines down here
    ))

