<div style="text-align: center">
<img src="https://i.imgur.com/wWhD02P.png"/>
</div>

# F-Aprrox
An application to aprroximate functions with polynomial using Taylor's series

## Usage
Simply enter function of x, then the approximation accuracy you want to get. The bigger degree of polynomial the higher accuracy you'll get, when the degree is infinity the Taylor's polynomial is equal to function. Then enter the point on x-axis around which the function will be approximated.

### Tips for use
While using app remember of SymPy functions notation:
- Instead of a^b use a**b
- For mathematical constant instaed of using e or π use their approximated value
- Always use functions of x
- Remember not to approximate functions around the point that value of function doesn't exist

## Radius of Convergence
It's recomended to check radius of convergence on your own in [Desmos](https://www.desmos.com/calculator)

## ToDo
- Calculating radius of convergence in app with a certain accuracy 
- Integration with [webpage](https://ziobro.ml/) and [Desmos](https://www.desmos.com/calculator) API

## Requirements
- [Python 3.8](https://www.python.org/)
    - [SymPy 1.6.2](https://pypi.org/project/sympy/)
