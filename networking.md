# Physical Layer 

## Means of Communication

- Wired:
  - Copper
  - Fiber Optic
- Wireless:
  - Radiowaves

## Bandwidth vs. Throughput

- Bandwidth = Capacity aka "Theoretical Transfer Rate"
- Throughput = Actual aka "Observed Transfer Rate"

## Powered vs Unpowered

USB-3.0 vs USB-2.0

## Powered vs Unpowered

# Digital Layer 

## Understanding IP Addresses

### CIDR Blocks

- Examples:
  ```bash
  # example 1
  174.51.67.130/32
  # example 2
  192.168.68.0/24
  ```
- There are 2 different types of "shorthand" syntax in these types of IP addresses:
  - 1. The `X.X.X.X` is the decimal format of the 32 bit (IPv4) binary IP address.
    - In example 1, `174.51.67.130` written out would be:
      `174.51.67.130 == 10101110.00110011.01000011.10000010 == 10101110001100110100001110000010`
    - In example 2, `192.168.68.0` written out would be:
      `192.168.68.0 == 11000000.10101000.00100010.00000000 == 11000000.10101000.00100010.00000000`
  - 2. The `/X` is the shorhand syntax for the subnet mask ( the long form of which is also a 32 bit (IPv4) decimal format number), indicating the number of bits that identify the network address.
    - In example 1, `/32` written out would be:
      - "32 bits are used to identify the network address"
        - `/32 == 255.255.255.255 == 11111111.11111111.11111111.11111111 == 11111111111111111111111111111111`
    - In example 2, `/24` written out would be:
      - "24 bits are used to identify the network address"
        - `/24 == 255.255.255.0 == 11111111.11111111.11111111.00000000 == 11111111111111111111111100000000`
- When an IP address and subnet mask are combined, you are specifying a *network address* and a *range/block of host addresses* (**even if that range is 1**):
  - The subnet mask identifies which bits in the IP address point to the network address, and which bits point to the block of host addresses:
    - In example 1, `174.51.67.130/32` written out would be:
      - "`174.51.67.130` is the IP address, and `32` bits of that IP address are used to identify the network address."
      - Written out *completely*, this would be:
        ```bash
        10101110001100110100001110000010 # IP address
        11111111111111111111111111111111 # subnet mask
        ```
    - In example 2, `192.168.68.0/24` written out would be:
      - "`192.168.68.0` is the IP address, and `24` bits of that IP address are used to identify the network address."
      - Written out *completely*, this would be:
        ```bash
        11000000101010000010010000000000 # IP address
        11111111111111111111111100000000 # subnet mask
        ```
      - When you line up the IP address and the subnet mask like I have above, you can clearly see which bits point to the network address (the
        `1's`), and which bits point towards the host address (the `0's`).
- When IP addresses are specified in this format, it is referred to as **Class-less Inter-Domain Routing** (or CIDR).
  - This allows the both network portion of the IP address and the host portion to be *variable length*, and thus gets the name *Variable Length
    Subnet Masking*.
- *Some history:*
  - To fully understand CIDR, it is best to understand it's predecessor, *Classful* IP addresses:
    - Up until the 1990's, IP addresses had a *fixed* overall length, as well has having a *fixed* length for the network portion of the address and a
      *fixed* length for the host portion of the address.
    - Networks were divided into 3 "classes" of network:
      - A) Class A networks had/have a network prefix of 8 bits.
      - B) Class B networks had/have a network prefix of 16 bits.
      - C) Class C networks had/have a network prefix of 24 bits.
    - The problem with this system is it's lack of flexibility, which results in wasted/unused IP addresses:
      - For example, if you are/were a larger company with 350 internal hosts, the problem is:
        - You can't use a Class C network, because there aren't enough IP addresses for all your hosts:
          - Class C networks having a 24 bit prefix means there are 8 bits remaining for the host portion of the address.
          - 8 available bits for all host addresses means you can have `2 ** 8 = 256` unique hosts on a Class C network.
        - This forces you to use a Class B network since all your hosts won't fit in a Class C network: 
          - Class B networks having 16 bits as the network prefix, leaving the remaining 16 bits for the host addresses.
          - 16 bits for all host addresses means you have `2 ** 16 = 65,536` available addresses for hosts
            - *technically `65,534`; 2 host addresses are subtracted from the total available addresses, and they are reserved for the network address
              and the broadcast address - beyond the scope of this explanation.*
          - This creates wasted IP addresses; you're company only needs 350 of the 65,534 addresses, leaving `65,534 - 350 = 65,184` addresses unused
