from flask import Flask, render_template, render_template_string, request, make_response
import re
import db

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "POST":

        customer_name = request.form["customer_name"]
        pizza_name = request.form["pizza_name"]
        pizza_size = request.form["pizza_size"]
        topping = request.form["topping"]
        sauce = request.form["sauce"]

        for item in [customer_name, pizza_name, pizza_size, topping, sauce]:
            m = re.match(
                r'.*[\!@#$%^&*()_+\-=[\]{};\'\\:"|,.<>/?`~].*', item, re.IGNORECASE
            )

            if m is not None:
                return """<p>Invalid characters detected!</p>"""

        error, final_price = db.add_order(
            customer_name, pizza_name, pizza_size, topping, sauce
        )

        if error is None:

            return render_template_string(
                """ 
            <p>Thank you, {}! Your order has been placed. Final price is ${} </p>
            """.format(
                    customer_name.split(" ")[0], str(final_price)
                )
            )

        else:
            return render_template_string(
                """ 
            <p>Sorry, there was an error when placing the order: {}</p>
            """.format(
                    error
                )
            )

    else:
        return render_template("order.html")


@app.route("/menu")
def get_pizza():
    return render_template(
        "menu.html",
        pizzas=db.get_pizzas(),
        toppings=db.get_toppings(),
        sauces=db.get_sauces(),
    )


if __name__ == "__main__":
    db.create_db()
    app.run(debug=False, host="0.0.0.0", port=1337)
