import base64

with open("heart_desease.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    print(f"![heart_desease.png](data:image/png;base64,{encoded_string})")
