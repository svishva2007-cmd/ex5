# Ex.05 Design a Website for Server Side Processing
## Date:12.12.2025
## Reference no:25006451

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :

~~~
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
/* ==== PAGE BACKGROUND ==== */
body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #0088ffd4, #00ff40b0);
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

/* ==== OUTER CARD BOX ==== */
.box {
    width: 380px;
    padding: 20px;
    background: rgba(255, 255, 255, 0.15);
    border-radius: 15px;
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.3);
}

/* ==== HEADER ==== */
h1 {
    color: #fff;
    text-align: center;
    padding-bottom: 10px;
    font-size: 28px;
}

/* ==== FORM ELEMENT WRAPPER ==== */
.formelt {
    color: #fff;
    font-size: 18px;
    margin-top: 12px;
    margin-bottom: 10px;
    text-align: center;
}

/* ==== INPUT BOX STYLE ==== */
input[type="text"] {
    width: 70%;
    padding: 8px;
    margin-top: 5px;
    border-radius: 8px;
    border: none;
    outline: none;
    font-size: 16px;
    text-align: center;
}

/* ==== GRADIENT BUTTON ==== */
input[type="submit"] {
    background: linear-gradient(45deg, #00ff95, #00d4ff);
    padding: 10px 20px;
    border: none;
    color: black;
    font-weight: bold;
    border-radius: 10px;
    cursor: pointer;
    font-size: 18px;
    transition: 0.3s;
}

input[type="submit"]:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 12px #00ffd5;
}

/* error text */
.error {
    color: #ffdddd;
    font-size: 14px;
    margin-top: 6px;
    text-align: center;
}
</style>
</head>

<body>
<div class="box">
<h1>Power Calculator</h1>

<form method="POST">
    {% csrf_token %}

    <div class="formelt">
        Resistance (R) :<br>
        <input type="text" name="resistance" value="{{R}}"> Ω
    </div>

    <div class="formelt">
        Current (I) :<br>
        <input type="text" name="current" value="{{I}}"> A
    </div>

    <div class="formelt">
        <input type="submit" value="Calculate">
    </div>

    <div class="formelt">
        Power (P = I²·R) :<br>
        <input type="text" name="power" value="{{power}}"> W
    </div>

    {% if error %}
    <div class="error">{{ error }}</div>
    {% endif %}

</form>
</div>

</body>
</html>
~~~

## SERVER SIDE PROCESSING:

![alt text](<Screenshot 2025-12-12 134456.png>)

## HOMEPAGE:

<img width="1919" height="928" alt="image" src="https://github.com/user-attachments/assets/83886435-4011-40e1-9322-9539cb1a4e68" />


The program for performing server side processing is completed successfully.
