#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <limits.h>

#define PORT 8080
#define MAX_CLIENTS 5
#define MAX_NUMBERS 1000

int main() {
    int server_sock, new_socket, valread;
    struct sockaddr_in server_addr, client_addr;
    int addrlen = sizeof(client_addr);
    int connection_count = 0;
    
    // Storage for all received numbers
    int received_numbers[MAX_NUMBERS];
    int numbers_count = 0;
    int current_max = INT_MIN;  // Initialize to minimum possible integer
    
    // Create socket
    server_sock = socket(AF_INET, SOCK_STREAM, 0);
    if (server_sock < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }
    
    // Allow socket reuse
    int opt = 1;
    setsockopt(server_sock, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
    
    // Configure server address
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);
    
    if (bind(server_sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }
    
    if (listen(server_sock, MAX_CLIENTS) < 0) {
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }
    
    printf("Server listening on port %d...\n", PORT);
    printf("Ready to receive numbers and track maximum.\n");
    
    while (1) {
        // Accept new connection
        new_socket = accept(server_sock, (struct sockaddr *)&client_addr, (socklen_t*)&addrlen);
        if (new_socket < 0) {
            perror("Accept failed");
            continue;
        }
        
        connection_count++;
        printf("\nNew connection #%d from %s\n", connection_count, inet_ntoa(client_addr.sin_addr));
        
        // Read integer from client
        int client_num;
        valread = recv(new_socket, &client_num, sizeof(client_num), 0);
        if (valread <= 0) {
            printf("Client disconnected or error\n");
            close(new_socket);
            continue;
        }
        
        // Convert from network byte order
        client_num = ntohl(client_num);
        printf("Received number: %d\n", client_num);
        
        // Store the number if we have space
        if (numbers_count < MAX_NUMBERS) {
            received_numbers[numbers_count] = client_num;
            numbers_count++;
        } else {
            printf("Warning: Maximum number storage reached!\n");
        }
        
        // Update maximum if this number is larger
        if (numbers_count == 1 || client_num > current_max) {
            current_max = client_num;
        }
        
        printf("Current maximum: %d\n", current_max);
        printf("Total numbers received: %d\n", numbers_count);
        
        // Send current maximum back to client
        int response = htonl(current_max);
        if (send(new_socket, &response, sizeof(response), 0) < 0) {
            perror("Send failed");
        } else {
            printf("Sent maximum %d back to client\n", current_max);
        }
        
        // Close the client socket
        close(new_socket);
        printf("Connection closed.\n");
    }
    
    close(server_sock);
    return 0;
}