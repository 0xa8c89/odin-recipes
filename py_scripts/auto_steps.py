steps = """
Preheat the oven to 375 degrees F (190 degrees C). Lightly butter a 9x13-inch casserole dish.

Melt 3 tablespoons butter in a medium saucepan over medium heat. Saute onion with 1/2 teaspoon kosher salt until it starts to soften up and turn translucent, 3 to 4 minutes. Add the flour, and cook, stirring, for 3 minutes, reducing heat if needed.

Pour in cold milk and whisk for 1 minute. Raise heat to medium-high and cook, stirring often, until the sauce thickens and comes to a simmer. Remove from heat, whisk in Cheddar cheese, and reserve until needed.

Fill a large pot with water and remaining salt and bring to a rapid boil. Cook egg noodles for 5 minutes. Drain well and add to a large mixing bowl. Stir in the reserved sauce, followed by tuna, peas, cayenne, black pepper, and Worcestershire sauce. Mix with a spatula until evenly combined.

Pour the mixture into the prepared dish. Mix bread crumbs, Parmigiano-Reggiano cheese, and olive oil together in a small bowl until combined and resembling wet sand. Sprinkle evenly over the casserole.

Bake in the center of the preheated oven until browned and bubbly, about 30 minutes. Let sit for 10 minutes before cutting and serving.
"""

for i in steps.split("\n"):
    if i:
        print("<li>" + i + "</li>")