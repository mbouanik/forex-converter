### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  - JS can be used  on the front-end  and back-end
  - python has indentations 
  - python use snake_case  Js use camelCase
  - 
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  - try: except:
  - variable.get(‘c’, default_value)

- What is a unit test?
  - allow you to test one functionality  of an app or program 

- What is an integration test?
  - allows you to test the synergy of  two of more functionality of an app that suppose to work together

- What is the role of web application framework, like Flask?
  - allow you to use basic or complex build-in functionality that you don’t need to build from scratch 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  - the first one is the information of a route
  - second one is value pass to the back-end 

- How do you collect data from a URL placeholder parameter using Flask?
  - variable = value

- How do you collect data from the query string using Flask?
  - request.args[‘variable’]

- How do you collect data from the body of the request using Flask?
  - request.form.get(‘variable’)

- What is a cookie and what kinds of things are they commonly used for?
  - store information about users …  lives inside the browser, the information is persistent 

- What is the session object in Flask?
  - store information inside the browser  but disappear as soon as the window is close or new tab is used 

- What does Flask's `jsonify()` do?
  - convert data into JSON 
