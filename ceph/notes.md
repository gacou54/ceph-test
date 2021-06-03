# Prérequis pour rouler les scripts
Faire un fichier `secrets.py` (`ceph-test/secrets.py`) avec 

```python
# secrets.py
access_key = 'votre-access-key'
secret_keys = 'votre-secret-key'
```

# Stocker un objet (ex. image)
1. Créer un bucket (s'il n'est pas déjà créé)
    - Le bucket est le "réservoir" de données d'un projet
    - voir `create_bucket.py`
1. Stockage d'un objet
    - voir `store_object.py`

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