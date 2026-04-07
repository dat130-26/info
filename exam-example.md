# Here are some example questions how they might appear in the web-programming part of the exam

*It is difficult to come up with solvable, but non-trivial multiple choice questions. In some cases, I therefore safe the multiple choice questions for the exam and put open questions here.*

### CSS Width

How much horizontal space does a `div` element take with the following CSS properties:
- `width: 100px`
- `padding: 10px`
- `border: 1px solid black`

### CSS

Replace ... in the code below with a line, giving all `div` elements red color.
```css 
div {
    border: 1px solid black;
    ...
}
```

### CSS Selectors

Which of the following are correct css selectors?
- `div.foo`
- `#header nav a`
- `.card~.title`
- `input[type="email"]`
- `ul li:first-child`
- `div..foo`
- `main#`
- `[href="/home"`
- `section + + p`

### CSS Flexbox

Which of the following CSS properties control how elements in a flexbox are displayed:
- `flex-wrap`
- `flex-shrink`
- `align-items`
- `justify-content`
- `flex-grow`
- `float`
- `grid-template-columns`
- `text-transform`
- `z-index`


### HTML

Where is the `<legend>` HTML tag used? Together with what other tags?

### Forms

Write the URL that results in submitting the following form with values `Leander` and `Stavanger`.

```html
<form action="/search" method="get">
    <label for="name">Name:</label>
    <input type="text" id="name" name="thename">

    <label for="city">City:</label>
    <input type="text" id="city" name="thecity">

    <button type="submit">Submit</button>
</form>
```

### Flask forms

The following flask route processes a form.

```python
@app.route("/search", methods=["GET"])
def search():
    name = request.args.get("thename", "")
    city = request.args.get("thecity", "")
    return f"Name: {name}, City: {city}"
```

Rewrite the function to process the same form, if it is submitted with a POST request.

### Jinja templates

Complete the Jinja template so it shows a heading with the user's name and a list of courses. If the list is empty, show `No courses yet`.

```python
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", name="Leander", courses=["DAT100", "DAT130"])
```

```html
<h2>...</h2>

...
    <ul>
    ...
        <li>...</li>
    ...
    </ul>
...
    <p>No courses yet</p>
...
```

### Flask static

Here is an example of a file structure in a flask project.
``` 
project/
|- static/
|  |- images/
|  |  |- picture.png
|  |- index.html
|- app.py
```

Write below, how the image `picture.png` can be displayed in the index.html.

### Flask redirect

Consider this Flask route:

```python
from flask import redirect, url_for

@app.route("/go-image")
def go_image():
    return redirect(url_for("static", filename="images/picture.png"))
```

What does an HTTP request to `/go-image` return?

- A) `200 OK` with the binary image data in the same response.
- B) `302 Found` with a `Location` header that points to `/static/images/picture.png`.
- C) `404 Not Found` because `url_for` only works for templates.
- D) `500 Internal Server Error` because `redirect` can only be used with `HTML` files.

### Rest route naming

Which of the following route definitions follow common REST naming conventions? (Select all that apply.)

1. `GET /users`
2. `GET /users/{id}`
3. `POST /users`
4. `PUT /users/{id}`
5. `DELETE /users/{id}`
6. `GET /getUsers`
7. `POST /createUser`
8. `DELETE /deleteUser/{id}`
9. `GET /userProfile/{id}`
10. `POST /user/{id}`

### JS Read 

```JS
function myFunc(element,color){
    element.style.backgroundColor=color;
}
```

```html
<div onclick=...>Some content </div>
```

Replace the ... above, so that when clicked, the background color of the `div` becomes blue.

### DOM Tree

Consider the following HTML snippet:

```html
<ul id="list">
    <li id="start">Start</li>
    <li id="middle">Middle</li>
</ul>
<p id="info">Info</p><p id="end">End</p>
```

And the following JavaScript snippet:

```javascript
const base = document.getElementById("start");
const selected = base.parentElement.nextSibling;
```

Which element is selected by `selected`?

- A) `<li id="middle">Middle</li>`
- B) `<ul id="list">...</ul>`
- C) `<p id="info">Info</p>`
- D) `<p id="end">End</p>`

### AJAX

Which of the following is true about AJAX requests

- A) Always return JSON data.
- B) Multiple requests can return in reverse order.
- C) AJAX only works with the `POST` method.
- D) AJAX request always update the page.
- E) AJAX requests cannot be made to the same server that served the page.
- F) Javascript cannot handle other events, while waiting for a reply from AJAX.
- G) AJAX responses must always have status code `200`.

### JavaScript async/await

Which of the following statements about `async`/`await` is correct?

- A) `await` can be used in any function, even if the function is not marked `async`.
- B) If a function returns a Promise, you can use `await` to wait for it to resolve.
- C) `await` makes JavaScript run synchronously and blocks the whole browser tab.
- D) `async`/`await` only works for `fetch`, not for other Promises.
