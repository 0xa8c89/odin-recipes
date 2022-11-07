steps = """
You can use melted butter instead of olive oil for the topping.

Cook egg noodles for 1 minute less than their individual package instructions call for.

If you have them around, crushed up potato chips might be the best topping for this instead of bread crumbs.
"""

for i in steps.split("\n"):
    if i:
        print("<li>" + i + "</li>")