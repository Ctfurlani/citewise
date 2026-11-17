# Transport Layer Security

Transport Layer Security (TLS) is a cryptographic protocol designed to provide secured communications over a computer network, such as the Internet. The protocol is widely used in applications such as email, instant messaging, and voice over IP, but its use in securing HTTPS remains the most publicly visible.

The TLS protocol aims primarily to provide security, including privacy (confidentiality), integrity, and authenticity through the use of cryptography, such as the use of certificates, between two or more communicating computer applications. It runs in the presentation layer and is itself composed of two layers: the TLS record and the TLS handshake protocols.

The closely-related Datagram Transport Layer Security (DTLS) is a communications protocol that provides security to datagram-based applications. In technical writing, references to "(D)TLS" are often seen when it applies to both versions.

TLS is a proposed Internet Engineering Task Force (IETF) standard, first defined in 1999, and the current version is TLS 1.3, defined in August 2018. TLS builds on the now-deprecated SSL (Secure Sockets Layer) specifications (1994, 1995, 1996) developed by Netscape Communications for adding the HTTPS protocol to their Netscape Navigator web browser.

Client–server applications use the TLS protocol to communicate across a network in a way designed to prevent eavesdropping and tampering.

Since applications can communicate either with or without TLS (or SSL), it is necessary for the client to request that the server set up a TLS connection. One of the main ways of achieving this is to use a different port number for TLS connections. Port 80 is typically used for unencrypted HTTP traffic while port 443 is the common port used for encrypted HTTPS traffic. Another mechanism is to make a protocol-specific STARTTLS request to the server to switch the connection to TLS – for example, when using some mail and news protocols.

Once the client and server have agreed to use TLS, they negotiate a stateful connection by using a handshaking procedure (see § TLS handshake). The protocols use a handshake with an asymmetric cipher to establish not only cipher settings but also a session-specific shared key with which further communication is encrypted using a symmetric cipher. During this handshake, the client and server agree on various parameters used to establish the connection's security:

The handshake begins when a client connects to a TLS-enabled server requesting a secure connection and the client presents a list of supported cipher suites (ciphers and hash functions).

From this list, the server picks a cipher and hash function that it also supports and notifies the client of the decision.

The server usually then provides identification in the form of a digital certificate. The certificate contains the server name, the trusted certificate authority (CA) that vouches for the authenticity of the certificate, and the server's public encryption key.

The client confirms the validity of the certificate before proceeding.

To generate the session keys used for the secure connection, the client either:

encrypts a random number (PreMasterSecret) with the server's public key and sends the result to the server (which only the server should be able to decrypt with its private key); both parties then use the random number to generate a unique session key for subsequent encryption and decryption of data during the session, or

uses Diffie–Hellman key exchange (or its variant elliptic-curve DH) to securely generate a random and unique session key for encryption and decryption that has the additional property of forward secrecy: if the server's private key is disclosed in the future, it cannot be used to decrypt the current session, even if the session is intercepted and recorded by a third party.

This concludes the handshake and begins the secured connection, which is encrypted and decrypted with the session key until the connection closes. If any one of the above steps fails, then the TLS handshake fails and the connection is not created.

Older versions of TLS and SSL allowed for establishing sessions via a PreMasterSecret using the server's public and private key. These algorithms were eliminated in TLS1.3 when it mandated forward secrecy.

TLS and SSL do not fit neatly into any single layer of the OSI model or the TCP/IP model. TLS runs "on top of some reliable transport protocol (e.g., TCP)", which would imply that it is above the transport layer. It serves encryption to higher layers, which is normally the function of the presentation layer. However, applications generally use TLS as if it were a transport layer, even though applications using TLS must actively control initiating TLS handshakes and handling of exchanged authentication certificates.

When secured by TLS, connections between a client (e.g., a web browser) and a server (e.g., wikipedia.org) will have all of the following properties:

The connection is private (or has confidentiality) because a symmetric-key algorithm is used to encrypt the data transmitted. The keys for this symmetric encryption are generated uniquely for each connection and are based on a shared secret that was negotiated at the start of the session. The server and client negotiate the details of which encryption algorithm and cryptographic keys to use before the first byte of data is transmitted (see below). The negotiation of a shared secret is both secure (the negotiated secret is unavailable to eavesdroppers and cannot be obtained, even by an attacker who places themselves in the middle of the connection) and reliable (no attacker can modify the communications during the negotiation without being detected).

The identity of the communicating parties can be authenticated using public-key cryptography. This authentication is required for the server and optional for the client.

The connection is reliable (or has integrity) because each message transmitted includes a message integrity check using a message authentication code to prevent undetected loss or alteration of the data during transmission.

TLS supports many different methods for exchanging keys, encrypting data, and authenticating message integrity. As a result, secure configuration of TLS involves many configurable parameters, and not all choices provide all of the privacy-related properties described in the list above (see the tables below § Key exchange, § Cipher security, and § Data integrity).

Attempts have been made to subvert aspects of the communications security that TLS seeks to provide, and the protocol has been revised several times to address these security threats. Developers of web browsers have repeatedly revised their products to defend against potential security weaknesses after these were discovered (see TLS/SSL support history of web browsers).

Source: https://en.wikipedia.org/wiki/Transport_Layer_Security (Wikipedia, CC BY-SA 4.0)
