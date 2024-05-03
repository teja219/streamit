import streamlit as st
import requests

def make_http_request(method, url, headers, body):
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=body)
        elif method == 'PUT':
            response = requests.put(url, headers=headers, json=body)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            return None, "Invalid HTTP method"

        return response, None
    except Exception as e:
        return None, str(e)

def main():
    st.title("Simple HTTP Request Tester")

    method = st.selectbox("Select HTTP Method", ['GET', 'POST', 'PUT', 'DELETE'])
    url = st.text_input("Enter URL")
    headers = st.text_area("Headers (JSON format)", "{}")
    body = st.text_area("Body (JSON format)", "{}")
    submit_button = st.button("Send Request")

    if submit_button:
        try:
            headers_dict = {}
            if headers:
                headers_dict = eval(headers)  # Parse JSON headers string into dictionary

            body_dict = {}
            if body:
                body_dict = eval(body)  # Parse JSON body string into dictionary

            response, error = make_http_request(method, url, headers=headers_dict, body=body_dict)

            if error:
                st.error(f"Error: {error}")
            else:
                st.success("Request sent successfully!")
                st.subheader("Response:")
                st.json(response.json())  # Display response JSON
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
