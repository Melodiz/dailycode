#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define PORT 8080
#define SERVER_IP "127.0.0.1"

int main() {
    int sock = 0;
    struct sockaddr_in serv_addr;
    int number_to_send;
    int received_max;
    
    printf("Enter a number to send to server: ");
    if (scanf("%d", &number_to_send) != 1) {
        printf("Invalid input!\n");
        return -1;
    }
    
    // Create socket
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        printf("Socket creation failed\n");
        return -1;
    }
    
    // Configure server address
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);
    
    // Convert IPv4 address from text to binary form
    if (inet_pton(AF_INET, SERVER_IP, &serv_addr.sin_addr) <= 0) {
        printf("Invalid address/ Address not supported\n");
        return -1;
    }
    
    // Connect to server
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        printf("Connection failed\n");
        return -1;
    }
    
    printf("Connected successfully!\n");
    
    // Send number to server (convert to network byte order)
    int network_number = htonl(number_to_send);
    if (send(sock, &network_number, sizeof(network_number), 0) < 0) {
        printf("Send failed\n");
        close(sock);
        return -1;
    }
    printf("Sent number: %d\n", number_to_send);
    
    // Receive maximum from server
    int valread = recv(sock, &received_max, sizeof(received_max), 0);
    if (valread <= 0) {
        printf("Failed to receive response\n");
        close(sock);
        return -1;
    }
    
    // Convert from network byte order
    received_max = ntohl(received_max);
    printf("Current maximum on server: %d\n", received_max);
    
    // Close socket
    close(sock);
    return 0;
}