# Configuration des notifications

Pour ajouter une notification, il faut :
1. Créer un bucket
   - Le bucket est le "réservoir" de données d'un projet
2. Créer un topic
   - Un topic est un "sujet" à lequel on configure une action lors de
     l'arrivé d'une notification. Par exemple, c'est ici où l'on
     configure comment la notification sera envoyée et à quel addresse, soit par
     - HTTP
     - AMQP (message, ex. RabbitMQ)
     - Kafka
3. Créer une (configuration de) notification
   - On associe un évènement à un topic. Par exemple, on pourrait configurer une
     liaison entre un Topic et un évènement (cération d'un nouvel objet).
     Donc à chaque nouvel objet, une notification est envoyé selon le topic (par HTTP, AMQP ou kafka)
     
4. Finalement stocker un objet pour déclencher la notification
   - Stockage un objet binaire quelconque (ex. une image)