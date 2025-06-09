# Client-Server Maximum Number Tracker

This project implements a client-server application where:

## Functionality

### Server (`server.c`)
- Listens on port 8080 for incoming client connections
- Receives integer numbers from clients
- Stores all received numbers (up to 1000 numbers)
- Maintains and tracks the current maximum of all received numbers
- Responds to each client with the current maximum value
- Provides detailed logging of all operations

### Client (`client.c`)
- Connects to the server on localhost:8080
- Prompts user to enter an integer number
- Sends the number to the server
- Receives and displays the current maximum from the server
- Closes the connection

## Compilation

### Using Makefile (Recommended)
```bash
# Compile both server and client
make

# Compile only server
make server

# Compile only client
make client

# Clean compiled files
make clean
```

### Manual Compilation
```bash
# Compile server
gcc -Wall -Wextra -std=c99 -o server server.c

# Compile client
gcc -Wall -Wextra -std=c99 -o client client.c
```

## Running the Programs

### 1. Start the Server
```bash
# Using Makefile
make run-server

# Or directly
./server
```

The server will start and display:
```
Server listening on port 8080...
Ready to receive numbers and track maximum.
```

### 2. Run Client(s)
In separate terminal windows, run one or more clients:

```bash
# Using Makefile
make run-client

# Or directly
./client
```

Each client will prompt you to enter a number:
```
=== Client: Send Number and Get Maximum ===
Enter a number to send to server: 42
Connecting to server at 127.0.0.1:8080...
Connected successfully!
Sent number: 42
Current maximum on server: 42
Connection closed.
```

## Example Usage

1. Start the server
2. Run first client and send number `10` → Server responds with maximum: `10`
3. Run second client and send number `25` → Server responds with maximum: `25`
4. Run third client and send number `15` → Server responds with maximum: `25`
5. Run fourth client and send number `30` → Server responds with maximum: `30`

The server maintains the maximum across all client connections and stores all received numbers.

## Features

- **Error Handling**: Both programs include comprehensive error checking
- **Network Byte Order**: Proper handling of integer transmission over network
- **Multiple Clients**: Server can handle multiple sequential client connections
- **Storage**: Server stores all received numbers (up to 1000)
- **Logging**: Server provides detailed logging of all operations
- **Socket Reuse**: Server allows socket reuse for quick restarts

## Architecture

- **Protocol**: TCP/IP
- **Port**: 8080
- **Data Format**: 32-bit integers in network byte order
- **Connection Model**: Sequential (one client at a time)
- **Storage**: In-memory array (resets when server restarts) 