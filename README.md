# Dynamic Website Design for a Manufacturing Company
## AIM:
To design a dynamic website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAM:

### base.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Copper Private Limited</title>
    <link rel="stylesheet" href="{% static 'css/layout.css' %}">
    <link rel = "icon" href ="{% static 'img/titleicon.png' %}" type = "image/x-icon"> 
              
</head>

<body>
    <div class="container">
    <div class="banner">
        Copper Private Limited.
    </div>
    <div class="menu">
        <div class="menuitem"><a href="/home">Home</a></div> 
        <div class="menuitem"><a href="/products">Products</a></div> 
        <div class="menuitem"><a href="/people">People</a></div>
        <div class="menuitem"><a href="/contactus">Contact-Us</a></div> 
    </div><div class="content">
    {% block content %}    
    {% endblock  %}
    </div>
    <div class="footer">
        Copyright © 2020 Copper Private Limited, Developed by Gowri.
    </div>
    </div>
</body>

</html>
``` 

### home.html
```
{% extends "websitedynamic/base.html" %}

{% block content %}
<div class="homecontent">
    <h1>About Us</h1>
    <img src="/static/img/firstpic.png" alt="Building">
    <div class="contenttext">
        Established in the year 2004, we “Copper Private Limited” have gained immense recognition in the domestic market as a
        leading trader of Ferrous & Non – Ferrous metal Products. Procured from authenticated vendors, these products
        are assured to be at par with the international quality standards.
        <h2>Our range encompasses following products:</h2>
        <ul>
            <li>Forging</li>
            <li>Structural Steels</li>
            <li>Plates </li>
            <li>Pipes & Tubes</li>
            <li>Manifold Blocks</li>
            <li>Alloy Steels</li>
            <li>Bright Bars</li>
            <li>Fittings</li>
            <li>Castings</li>
            <li>Industrial Steels</li>
        </ul>
    </div>
</div>
{% endblock  %}
```

### products.html
```
{% extends "websitedynamic/base.html" %}

{% block content %}
<div class="productcontent">
    <h1>Our Premium Products</h1>
    <div class="productitems">
        {% for product in products%}
        <div class="productitem">
            <div class="itemimage">
                <img src="{{ product.photo.url }}" alt="Product photo">
            </div>
            <div class="itemname">{{ product.productname }}</div>
            <div class="itemprice">Price: {{ product.productprice }}</div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock  %}
```

### people.html
```
{% extends "websitedynamic/base.html" %}

{% block content %}
<div>
    <h1>Our team</h1>
    <div class="productitems">
        {% for people in peoples%}
        <div class="productitem">
            <div class="itemimage">
                <img src="{{ people.photo.url }}" alt="People photo">
            </div>
            <div class="itemname">{{ people.name }}</div>
            <div class="itemprice">Price: {{ people.position }}</div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock  %}
```

### contactus.html
```
{% extends "websitedynamic/base.html" %}

{% block content %}
<div>
    <h1>Contact details</h1>
    <div>
        <h2>Contact person:</h2>
            <h4>Vijay Kharti (director)</h4>

        <h2>Address:</h2>
        <h4>Copper Private Limited</h4>
        <h4>No. 1-A, Puliambedu, Numbal,</h4>
        <h4> Off Poonamallee High Road,</h4> 
        <h4>Chennai - 600077,</h4> 
        <h4>Tamil Nadu, India</h4>
        
        <h2>Call us:</h2>
        <h4>080678 54633</h4>
    </div>
    <div>

        <h1>Other contact details</h1>
        <h4>Sales Enquiry</h4>
        <h4> Kavita</h4> 
        <h4>1A puliembedu, Numbal, Off PH Rd,</h4>
        <h4>Chennai - 600077, India</h4>

        <h3>Head Office</h3>
        <h4>Kamal Khatri,</h4>
        <h4>1A Puliembedu, Numbal,</h4> 
        <h4>Off Poonamallee High Road, India</h4>
        
        

        <h3>Branch Office</h3>
        <h4>Vijay Khatri</h4>

        <h3>Head Office</h3>
        <h4>Srinivasan</h4>
        <h4>1A puliembedu, Numbal,</h4>
        <h4> Off PH Rd, Chennai -600077, India</h4>

       </div>
</div>

{% endblock  %}
```

## OUTPUT:
![output](./static/img/out1.png)

![output](./static/img/admin2.png)

![output](./static/img/admin2.2.png)

![output](./static/img/out2.png)

![output](./static/img/out3.png)

![output](./static/img/admin1.png)

![output](./static/img/admin1.1.png)

![output](./static/img/out4.png)

![output](./static/img/out5.png)

![output](./static/img/out6.png)

![output](./static/img/out7.png)



## CODE VALIDATION REPORT:
![output](./static/img/val1.png)

![output](./static/img/val2.png)

![output](./static/img/val3.png)

![output](./static/img/val4.png)


## RESULT:
Thus a dynamic website is designed for the chip manufacturing company and is hosted in the URL http://gowri.student.saveetha.in:8000/. HTML code is validated.