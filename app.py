from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store tasks in memory
tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect(url_for("index"))


@app.route("/delete/<int:id>")
def delete(id):
    if 0 <= id < len(tasks):
        tasks.pop(id)
    return redirect(url_for("index"))


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    new_task = request.form.get("task")
    if 0 <= id < len(tasks) and new_task:
        tasks[id] = new_task
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)