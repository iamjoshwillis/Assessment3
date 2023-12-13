### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?  

 _There are syntax differences Python uses snake case instead of the camelCase that JS uses,Python's empty value is None while JS uses null, Python has lists instead of arrays, Python has dictionaries, Python uses and, or, and not, instead of &&, ||, and !._

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  
  _You could use letter.get('c', 'Not Found') or try: print(letter['c'] except KeyError: print('Not Found')_

- What is a unit test?

  _A unit test tests pieces of code that are small and isolated. These do not test the integration of components or the framework itself._
  
- What is an integration test?

  _An integration tests combined program units as groups in multiple ways. They are written with the unittest framework, and could test things like the URL path, if the right HTML is being returned, or that the correct status code is being returned._

- What is the role of web application framework, like Flask?

  _A framework is a set of functions, classes, etc. that assist in defining which requests to respond to, and how to respond to requests._

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  
  _A URL parameter is more suited in a "subject of page" fashion, while a query parameter is more like "extra info about the page"_

- How do you collect data from a URL placeholder parameter using Flask?

  _A very nice feature and way of doing this is:_
  
  app.route('/< datatocollect >')  
  def show_collecteddata(datatocollect)  
  return datatocollect
  
- How do you collect data from the query string using Flask?

  _You can use request.args(data) to gather this information._

- How do you collect data from the body of the request using Flask?

  _You can use request.form(data) to gather this information._

- What is a cookie and what kinds of things are they commonly used for?

  _A cookie is a name/string-value pair that the browser stores. They are small bits of info that will restore/maintain the state of certain pieces of information in the browser._

- What is the session object in Flask?

  _The session object in Flask contains information for the current browser, it will preserve a type, like keeping a list a list, and they are signed so that users cannot modify the data. It's generally better to use sessions over cookies._

- What does Flask's `jsonify()` do?

  _It's a way for Flask to translate data into JSON while letting the browser know that it is incoming JSON._
