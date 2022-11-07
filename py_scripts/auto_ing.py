ingredients = """
3 tablespoons unsalted butter

½ cup finely diced yellow onion

1 ½ teaspoons kosher salt, divided

3 tablespoons all-purpose flour

4 cups cold milk

1 cup shredded white Cheddar cheese

1 (12 ounce) package dry egg noodles

2 (5.5 ounce) cans tuna packed in olive oil, drained and crumbled, or to taste

¾ cup frozen peas, thawed and drained

1 pinch cayenne pepper

¼ teaspoon freshly ground black pepper

¼ teaspoon Worcestershire sauce

½ cup plain bread crumbs

½ cup grated Parmigiano-Reggiano cheese

2 tablespoons olive oil
"""
ingredients = ingredients.split('\n')
for i in ingredients:
    if i:
        print(f"<li>{i}</li>")
