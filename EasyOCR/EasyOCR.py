import requests
import json
import cv2
import re
import easyocr

# Global variable to store the image path
global_image_path = None


def trim_spaces(text):
    # Trim spaces within a word but retain spaces between separate words
    # using regular expressions to remove spaces between letters
    return re.sub(r'\s(?!\s)', '', text)


def perform_ocr(global_image_path):
    if not global_image_path:
        print("Image path not provided. OCR cannot be performed.")
        return []

    # Load the image
    img = cv2.imread(global_image_path)

    # Perform OCR on the image
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(img)

    texts = []
    for detection in result:
        bbox = detection[0]
        text = detection[1]

        # Convert bounding box coordinates to integers
        top_left = tuple(map(int, bbox[0]))
        bottom_right = tuple(map(int, bbox[2]))

        # Trim spaces within the text
        text = trim_spaces(text)
        texts.append(text)

        # Print the extracted text in the console
        print(f"Extracted text: {text}")

        # Draw bounding box and text on the image (optional)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        font_thickness = 1
        box_color = (0, 255, 0)  # Green
        text_color = (0, 0, 0)  # Black
        img = cv2.rectangle(img, top_left, bottom_right, box_color, 3)
        img = cv2.putText(img, f"{text}", (top_left[0], top_left[1] - 5), font,
                          font_scale, text_color, font_thickness, cv2.LINE_AA)

    # Save the extracted texts to a JSON file
    with open('extracted_texts.json', 'w') as json_file:
        json.dump(texts, json_file)

    # # Display the image with bounding boxes and extracted texts using matplotlib
    # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.imshow(img_rgb)
    # plt.title("Processed Image")
    # plt.axis('off')
    # plt.switch_backend('agg')
    # #plt.ioff()

    # Show the plot
    #plt.show()
    send_extracted_texts_to_spring_boot(texts)


def send_extracted_texts_to_spring_boot(extracted_texts):
    # api_url = 'http://10.175.5.146:8080'
    api_url = 'http://:8080'
    request_headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(f"{api_url}/response/receiveJSON", data=json.dumps(extracted_texts), headers=request_headers)
        response.raise_for_status()
        # print("Data successfully sent to website.")
        # print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Failed to send data:", e)



if __name__ == "__main__":
    extracted_texts = perform_ocr(global_image_path)
