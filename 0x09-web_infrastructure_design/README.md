# 0x09. Web infrastructure design:web:

**Concepts**
- [DNS](./concepts/dns.md)
- [Monitoring](./concepts/monitoring.md)
- [Web Server](./concepts/web_server.md)
- [Network basics](./concepts/network_b.md)
- [Load balancer](./concepts/l_balance.md)
- [Server](./concepts/server.md)

**Background**

In the sysadmin/devops track projects, the project requirements included the ability to create a diagram illustrating the web stack that was built. Furthermore, it was essential to provide an explanation of the function and purpose of each component within the stack. Additionally, understanding system redundancy was crucial, including its importance in ensuring high availability and fault tolerance. Lastly, familiarity with various acronyms such as LAMP (Linux, Apache, MySQL, PHP), SPOF (Single Point of Failure), and QPS (Queries Per Second) was required. Overall, these projects emphasized a comprehensive understanding of the web stack, its components, system redundancy, and relevant acronyms.

## Resources:books:
- **Network basics** concept page
- **Server** concept page
- **Web server** concept page
- **DNS** concept page
- **Load balancer** concept page
- **Monitoring** concept page
- [What is a database](https://www.oracle.com/ke/database/what-is-database/)
- [What’s the difference between a web server and an app server?](https://www.infoworld.com/article/2077354/app-server-web-server-what-s-the-difference.html)
- [DNS record types](https://www.site24x7.com/learn/dns-record-types.html)
- [Single point of failure](https://avinetworks.com/glossary/single-point-of-failure/)
- [How to avoid downtime when deploying new code](https://softwareengineering.stackexchange.com/questions/35063/how-do-you-update-your-production-codebase-database-schema-without-causing-downt#answers-header)
- [High availability cluster (active-active/active-passive)](https://docs.oracle.com/cd/E17904_01/core.1111/e10106/intro.htm#ASHIA712)
- [What is a firewall](https://www.webopedia.com/definitions/firewall/)

## Tasks:page_with_curl:

### 0. Simple web stack

- [0-simple_web_stack](./0-simple_web_stack): A designed single-server web infrastructure that is capable of hosting a website accessible through the domain `www.foobar.com`. The infrastructure utilizes a shared resource model, where both the database and application server components leverage the CPU, RAM, and SSD resources provided by the server.
  It is important to note that the current configuration does not include any firewalls or SSL certificates for network protection. While the infrastructure efficiently serves the website, it is recommended to implement appropriate security measures, such as firewalls and SSL certificates, to safeguard the server's network and ensure the confidentiality and integrity of data transmission.

**Some specifics About This Infrastructure**
- What is a server?
  - A server is a computer or system that provides services or resources to other devices or ***clients*** on a network.
  
- What is the role of the domain name?
  - A domain name is a unique and human-friendly identifier used to locate and access websites or online services on the internet. It serves as a more memorable alternative to the numerical IP addresses that computers use to communicate with each other.

- What type of DNS record `www` is in `www.foobar.com`?
  - The `www.foobar.com` is an alias for the domain `foobar.com`. The former uses a **CNAME (Canonical Name) record**, indicating that it points to the latter, which uses an **A (Adress) record** type to associate the IPv4 address `173.231.209.34` with the domain `foobar.com`. This can be checked by running ``dig www.foobar.com``

- What is the role of the web server?
  - A web server is a software or hardware component that accepts requests through HTTP or secure HTTP (HTTPS) protocols and responds by providing the content of the requested resource or returning an error message when necessary. It acts as the intermediary between clients and the web content they are accessing.

- What is the role of the application server?
  - The role of an application server is to host and execute applications, responding to client requests by providing the content of the requested resource or returning error messages. It acts as a software or hardware component that handles the runtime environment and services required for applications to run and interact with clients.

- What is the role of the database?
  - The role of a database is to store, manage, and organize structured data efficiently. It provides a structured and secure environment for storing and retrieving data, allowing applications to store, update, and retrieve information as needed.

- What is the server using to communicate with the computer of the user requesting the website
  - The server communicates with the user's computer over the internet network using the HTTP (Hypertext Transfer Protocol), which is a key component of the TCP/IP (Transmission Control Protocol/Internet Protocol) protocol suite.

**the issues with this infrastructure:**
- SPOF:
  - The Single Point of Failure (SPOF) in the single-serve infrastructure design is the reliance on a single server. If this server fails or experiences issues, the entire infrastructure and website hosted on it become inaccessible. There is no redundancy or backup server to ensure continuous availability, making it vulnerable to disruptions and downtime.

- Downtime when maintenance needed (like deploying new code web server needs to be restarted):
  - During maintenance, such as deploying new code and restarting the web server, downtime occurs, rendering the server temporarily unavailable for handling client requests. Downtime refers to the period when the server is not accessible, impacting user access to the website. Measures like scheduling maintenance during low traffic times can minimize user disruptions.

- Cannot scale if too much incoming traffic.
  - The issue "Cannot scale if too much incoming traffic" means that the single-server infrastructure is unable to handle a large influx of requests effectively, resulting in performance degradation or downtime.

### 1. Distributed web infrastructure

- [1-distributed_web_infrastructure](./1-distributed_web_infrastructure): A designed three-server web infrastructure for `www.foobar.com` includes a web server (Nginx), an application server, a load balancer (HAproxy), and a MySQL database. Nginx serves static files and handles incoming requests, while HAproxy distributes traffic across the servers for optimal resource utilization. The application server hosts the code base, generating dynamic content and executing server-side logic. The MySQL database efficiently manages and stores the website's data. This infrastructure design ensures improved performance, scalability, and fault tolerance by distributing the workload, utilizing specialized components, and implementing a robust database management system. Overall, it enables a smooth and responsive website experience for users while accommodating growth and providing reliability.

**some specifics about this infrastructure:**
- For every additional element, why you are adding it?
  - A caching layer, such as Redis or Memcached, can be added between the application server and the database in order to enhance the performance and response times of the web infrastructure. By caching frequently accessed data or computed results, this layer reduces the workload on the database and accelerates the retrieval of information, resulting in faster response times for users.

- What distribution algorithm your load balancer is configured with and how it works
  - The load balancer, specifically HAProxy, is configured with the Round Robin distribution algorithm. HAProxy evenly distributes incoming requests across the available servers in a cyclic manner to achieve balanced resource utilization. This algorithm ensures that each server receives an equal share of the incoming traffic, preventing any individual server from becoming overloaded and promoting efficient request processing across the server pool.

- Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both.
  - The HAProxy load balancer is configured for an Active-Active setup instead of an Active-Passive setup.
  - Active-Active setups can provide higher capacity, improved performance, and better load distribution, as all nodes actively handle traffic. They are well-suited for scenarios where maximizing resource utilization and handling high traffic volumes are important.
  - Active-Passive setups prioritize failover and redundancy, ensuring uninterrupted service in the event of a node failure. This setup may be preferred when rapid failover and fault tolerance are crucial.

- How a database Primary-Replica (Master-Slave) cluster works
  - A Primary-Replica (Master-Slave) database cluster consists of a primary/master server that handles read and write operations, and replica/slave servers that receive replicated data changes from the primary server. Replica servers are used for read operations, improving performance. The primary server's changes are replicated asynchronously to the replicas, ensuring data consistency. In case of primary server failure, a replica can be promoted as the new primary server, ensuring high availability.

- What is the difference between the Primary node and the Replica node in regard to the application
  - The primary node handles write operations, ensuring data modifications are applied and maintained. The replica node, on the other hand, handles read operations, reducing the workload on the primary node and improving performance by distributing the read traffic across replicas.

**issues with this infrastructure:**
- Where are SPOF
  - The potential single points of failure (SPOFs) in this infrastructure are the load balancer and the database server.
    
    If the load balancer fails, it can disrupt the distribution of incoming traffic to the web and application servers, resulting in service unavailability.To mitigate this, implementing redundancy or high availability for the load balancer, such as using multiple load balancers in a failover configuration, can ensure continuous traffic distribution even if one load balancer fails.

    Similarly, If the database server experiences issues or downtime, it can lead to data unavailability and impact the functionality of the website. Implementing a replicated or clustered database setup can address this issue. With replication, data is replicated across multiple database servers, providing redundancy and allowing for failover to a replica server in case the primary database server fails.

- Security issues (no firewall, no HTTPS)
  - The security issues with this infrastructure include the absence of a firewall and lack of HTTPS encryption, leading to increased vulnerability to cyber attacks, higher risks of data breaches and privacy breaches, potential compliance and legal issues, and loss of user trust. Implementing these security measures is essential to protect the infrastructure, safeguard user data, and maintain a secure and trustworthy environment.

- No monitoring
  - The absence of monitoring in the infrastructure hinders the ability to track performance, identify issues, and ensure smooth operation. It increases the risk of undetected problems, downtime, and degraded performance, impacting user experience and hindering timely troubleshooting and optimization. Monitoring is vital for proactive issue identification and maintaining a reliable and high-performing infrastructure.

### 2. Secured and monitored web infrastructure
- [2-secured_and_monitored_web_infrastructure](./2-secured_and_monitored_web_infrastructure): A three-server web infrastructure designed for hosting the website `www.foobar.com` focuses on security, encrypted traffic, and monitoring. It consists of a load balancer server equipped with three firewalls for enhanced security, serving an SSL certificate for HTTPS access to `www.foobar.com`. This load balancer distributes incoming traffic across two application servers, ensuring redundancy and load balancing. All communication is secured with SSL/TLS encryption. The infrastructure is monitored by three monitoring clients, collecting data for monitoring services to track performance and maintain overall system health. This setup provides a secure, scalable, and closely monitored environment for hosting the website.

**some specifics about this infrastructure:**
- For every additional element, why you are adding it
  - A **database server** is added alongside the application servers and positioned behind the load balancer. Its purpose is to store and manage website data, including user information, content, and other relevant data.

- What are firewalls for
  - In the context of this infrastructure, firewalls are used to enhance security. They act as a barrier between the server and the external network, controlling incoming and outgoing network traffic based on predefined security rules. Firewalls help protect the servers and the network infrastructure from unauthorized access, malicious attacks, and potential security threats. By implementing firewalls, the infrastructure can selectively allow or block traffic, providing an additional layer of defense against unauthorized access and potential vulnerabilities.

- Why is the traffic served over HTTPS
  - Traffic is served over HTTPS in this infrastructure to ensure secure and encrypted communication, protecting user data and maintaining trust.

- What monitoring is used for
  - Monitoring in this infrastructure is used to track server performance, availability, traffic load, and security, ensuring optimal system operation and proactive management.

- How the monitoring tool is collecting data
  - The monitoring tool collects data by actively monitoring and analyzing various metrics and logs from the servers and network devices. It uses specific monitoring agents or software installed on the servers, which gather real-time information about resource utilization, performance metrics, system logs, and network traffic. The monitoring tool collects and aggregates this data, providing insights and alerts based on predefined thresholds and rules. Additionally, the monitoring tool may utilize APIs or integration with other tools and services to gather relevant data and enrich the monitoring capabilities.

- Explain what to do if you want to monitor your web server QPS
  - To monitor the QPS (Queries Per Second) of your web server:
    1. Choose a suitable monitoring tool that supports QPS monitoring.
    2. Configure the monitoring tool to collect and track the QPS metric from the web server.
    3. Set appropriate thresholds for QPS.
    4. Enable alerting to receive notifications when QPS exceeds the thresholds.
    5. Analyze the monitoring data and take necessary actions to optimize performance or scale the infrastructure based on the QPS trends.

**issues with this infrastructure:**
- Why terminating SSL at the load balancer level is an issue
  - SSL certificates play a crucial role in encrypting traffic between web servers and the external network, ensuring privacy, integrity, and identification. They prevent security risks like man-in-the-middle attacks and network sniffing. However, terminating SSL at the load balancer level in this infrastructure poses issues by compromising end-to-end encryption, increasing the attack surface for backend servers, and potentially violating compliance and privacy requirements.

- Why having only one MySQL server capable of accepting writes is an issue
  - Having only one MySQL server capable of accepting writes in this infrastructure can lead to several issues. Firstly, it becomes a single point of failure, risking data inconsistencies or loss if the server experiences downtime. Additionally, scalability and performance are limited as the single server can become a bottleneck under increased workload. High availability is compromised without redundancy, causing service interruptions during server failures or maintenance. Moreover, data integrity and disaster recovery are at risk without multiple servers for write operations. To address these concerns, implementing a solution with multiple MySQL servers capable of accepting writes, such as database replication or clustering, is essential for improved availability, scalability, performance, and data integrity.

- Why having servers with all the same components (database, web server and application server) might be a problem
  - Having servers with all the same components (database, web server, and application server) in this infrastructure can present challenges. It limits the ability to optimize each component for its specific requirements, potentially resulting in suboptimal performance and scalability. Scaling can become complex as adding resources would involve redundant components across all servers. Maintenance becomes more intricate, requiring coordination for updates and troubleshooting. Furthermore, the lack of flexibility hampers the ability to adapt to evolving needs or integrate new technologies. Adopting a specialized and modular approach allows for better resource allocation, scalability, streamlined maintenance, and adaptability to changing requirements.

### 3. Scale up
- [3-scale_up](./3-scale_up): A web infrastructure `Scale up` is designed to meet the requirements of security, encrypted traffic, and monitoring. It consists of a single server that serves as the central component, along with a load balancer (HAproxy) configured as a cluster with another load balancer. The components of the infrastructure, including the web server, application server, and database, are split across dedicated servers. This separation allows for efficient resource utilization and easier management. Security measures are implemented, including SSL/TLS encryption, to protect the communication between clients and servers. Additionally, monitoring capabilities are incorporated to track the system's performance, availability, and overall health, ensuring prompt identification and resolution of any issues that may arise.

***readme:***
- [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)

**some specifics about this infrastructure:**
- For every additional element, why you are adding it
  - Adding an Intrusion Detection System (IDS) between the load balancer and the web server enhances security by detecting potential intrusions or malicious activities in the network.
