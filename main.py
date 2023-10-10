import socket
print('Welcome to our project')
print('Done by Dana,Lana,Jana')
def create_response( request,client_port):
    print(f"Received request from {client_port}: {request}")
    if request == "/" or request == "/index.html" or request == "/main_en.html" or request == "/en":
        try:
            with open("main_en.html", "r", encoding="utf-8") as html_file:
                html_content = html_file.read()

            with open("styles.css", "r", encoding="utf-8") as css_file:
                css_content = css_file.read()

            response = ("HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n" + html_content + "\n<style>\n" + css_content + "\n</style>").encode()
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
           response = generate_error_response("The requested page was not found.",  client_port)

   

    elif request == "/laptops.txt":
        try:
            with open("laptops.txt", "r", encoding="utf-8") as laptops_file:
                laptops_content = laptops_file.read()
                laptops_lines = laptops_content.strip().split('\n')
                sorted_laptops = '\n'.join(laptops_lines)
            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=UTF-8\r\n\r\n{laptops_content}".encode()
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)

    elif request == "/SortByName":
        try:
            with open("laptops.txt", "r", encoding="utf-8") as laptops_file:
                laptops_content = laptops_file.read()
                laptops_lines = laptops_content.strip().split('\n')
                laptops_lines.sort(key=lambda line: line.split(',')[0].upper())  # Sort by name in uppercase
                sorted_laptops = '\n'.join(laptops_lines)

            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=UTF-8\r\n\r\n{sorted_laptops}".encode()
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)


    # Add this case to the create_response function
    elif request == "/SortByPrice":
        try:
            with open("laptops.txt", "r", encoding="utf-8") as laptops_file:
                laptops_lines = laptops_file.readlines()

            laptops_lines.sort(key=lambda line: float(line.split()[1]) if len(line.split()) > 1 else float('inf'))

            sorted_laptops_content = ""
            total_price = 0

            for line in laptops_lines:
                name, price = line.strip().split()
                sorted_laptops_content += f"{name}: ${price}\n"
                total_price += float(price)

            sorted_laptops_content += f"\nTotal Price: ${total_price}"

            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=UTF-8\r\n\r\n{sorted_laptops_content}".encode()
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)



    elif request == "/bzuLogo.png":
        try:
            with open("bzuLogo.png", "rb") as image_file:
                image_content = image_file.read()

            response = b"HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n" + image_content
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)



    elif request == "/buy.jpg":
        try:
            with open("buy.jpg", "rb") as image_file:
                image_content = image_file.read()

            response = b"HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\n\r\n" + image_content
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
           response = generate_error_response("The requested page was not found.",  client_port)



    elif request == "/main_en.html":
        try:
            with open("main_en.html", "r", encoding="utf-8") as html_file:
                html_content = html_file.read()

            response = ("HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n" + html_content).encode()
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
           response = generate_error_response("The requested page was not found.",  client_port)


    elif request == "/main_en.html":
        try:
            with open("main_en.html", "r", encoding="utf-8") as html_file:
                html_content = html_file.read()

            response = ("HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n" + html_content).encode()
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)




    elif request == "/main_ar.html" or request == "/ar":
        try:
            with open("main_ar.html", "r", encoding="utf-8") as html_file:
                html_content = html_file.read()

            with open("styles.css", "r", encoding="utf-8") as css_file:
                css_content = css_file.read()

            response = ("HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n" + html_content + "\n<style>\n" + css_content + "\n</style>").encode()
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)




    elif request == "/styles.css":
        try:
            with open("styles.css", "r", encoding="utf-8") as css_file:
                css_content = css_file.read()

            response = ("HTTP/1.1 200 OK\r\nContent-Type: text/css; charset=UTF-8\r\n\r\n" + css_content).encode()
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)

    elif request.endswith(".html"):
        try:
            with open(request[1:], "r", encoding="utf-8") as html_file:
                html_content = html_file.read()

            response = ("HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n" + html_content).encode()
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)

    elif request.endswith(".css"):
        try:
            with open(request[1:], "r", encoding="utf-8") as css_file:
                css_content = css_file.read()

            response = ("HTTP/1.1 200 OK\r\nContent-Type: text/css; charset=UTF-8\r\n\r\n" + css_content).encode()
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)

    elif request.endswith(".png"):
        try:
            with open(request[1:], "rb") as image_file:
                image_content = image_file.read()

            response = b"HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n" + image_content
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)

    elif request.endswith(".jpg"):
        try:
            with open(request[1:], "rb") as image_file:
                image_content = image_file.read()

            response = b"HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\n\r\n" + image_content
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)



    elif request == "/main_ar.html" or request == "/ar":
        try:
            with open("main_ar.html", "r", encoding="utf-8") as html_file:
                html_content = html_file.read()

            with open("styles.css", "r", encoding="utf-8") as css_file:
                css_content = css_file.read()

            response = ("HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n" + html_content + "\n<style>\n" + css_content + "\n</style>").encode()
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)

        # Add this case to the create_response function
    elif request == "/SortByName":
        try:
            with open("laptops.txt", "r", encoding="utf-8") as laptops_file:
                laptops_content = laptops_file.read()
                laptops_lines = laptops_content.strip().split('\n')
                laptops_lines.sort(key=lambda line: line.split(',')[0].upper())  # Sort by name in uppercase
                sorted_laptops = '\n'.join(laptops_lines)

            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=UTF-8\r\n\r\n{sorted_laptops}".encode()
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)
    elif request == "/SortByPrice":
        try:
            with open("laptops.txt", "r", encoding="utf-8") as laptops_file:
                laptops_lines = laptops_file.readlines()

            laptops_lines.sort(key=lambda line: float(line.split()[1]) if len(line.split()) > 1 else float('inf'))

            sorted_laptops_content = ""
            total_price = 0

            for line in laptops_lines:
                name, price = line.strip().split()
                sorted_laptops_content += f"{name}: ${price}\n"
                total_price += float(price)

            sorted_laptops_content += f"\nTotal Price: ${total_price}"

            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=UTF-8\r\n\r\n{sorted_laptops_content}".encode()
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)


    elif request.endswith(".html"):
        try:
            with open(request[1:], "r", encoding="utf-8") as html_file:
                html_content = html_file.read()

            response = ("HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n" + html_content).encode()
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
           response = generate_error_response("The requested page was not found.",  client_port)

    elif request.endswith(".css"):
        try:
            with open(request[1:], "r", encoding="utf-8") as css_file:
                css_content = css_file.read()

            response = ("HTTP/1.1 200 OK\r\nContent-Type: text/css; charset=UTF-8\r\n\r\n" + css_content).encode()
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
           response = generate_error_response("The requested page was not found.",  client_port)

    elif request.endswith(".png"):
        try:
            with open(request[1:], "rb") as image_file:
                image_content = image_file.read()

            response = b"HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n" + image_content
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)

    elif request.endswith(".jpg"):
        try:
            with open(request[1:], "rb") as image_file:
                image_content = image_file.read()

            response = b"HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\n\r\n" + image_content
            print("HTTP/1.1 200 OK")
        except FileNotFoundError:
            response = generate_error_response("The requested page was not found.",  client_port)


    else:
        response = generate_error_response("The requested page was not found.",  client_port)

        # Add redirects for specific paths using 307 Temporary Redirect status code
    if request == "/azn":
        response = "HTTP/1.1 307 Temporary Redirect\r\nLocation: https://www.amazon.com\r\n\r\n".encode()
        print("HTTP/1.1 307 Temporary Redirect")
    elif request == "/so":
        response = "HTTP/1.1 307 Temporary Redirect\r\nLocation: https://stackoverflow.com\r\n\r\n".encode()
    elif request == "/bzu":
        response = "HTTP/1.1 307 Temporary Redirect\r\nLocation: https://www.birzeit.edu\r\n\r\n".encode()

    return response


def generate_error_response(error_message, client_port):
    
    with open("error.html", "r", encoding="utf-8") as error_file:
        error_content = error_file.read()

    error_content = error_content.replace("{client_port}", str(client_port))
    response = f"HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n{error_content}".encode()
    return response



def main():
   
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", port))
    server_socket.listen(1)

    print(f"Server is listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        request = client_socket.recv(1024).decode()

        if not request:
            continue

        print(f"Received request from {client_address[0]}:{client_address[1]}:\n{request}")

        request_line = request.split('\n')[0]
        request_parts = request_line.split()
        if len(request_parts) > 1:
            requested_path = request_parts[1]
            response = create_response(requested_path, client_address[0])
        else:
            response = generate_error_response("Bad Request", client_address[0])

        client_socket.sendall(response)
        client_socket.close()



if __name__ == "__main__":
    main()
