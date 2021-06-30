Ce répertoire contient différents scripts Python qui ont
servi à effectuer des tests.
Ces scripts Python pourraient vous venir en aide/vous inspirer si
vous souhaitez tester ou apprendre à utiliser Ceph.


# Prérequis pour rouler les scripts
## Informations confidentielles
Faire un fichier `secrets.py` (`ceph-test/secrets.py`) avec 

```python
# secrets.py
access_key = 'votre-access-key'
secret_keys = 'votre-secret-key'
```

## Configurations
Les configurations sont écrites dans le fichier `config.py` sous la forme
de variables Python (ex. `MY_IP = '107.01.19.12`).
Assurez-vous d'y avoir entré les bonnes informations pour
votre projet puisque celles-ci __devraient__ être différentes
que celles déjà présentes. Notez que 

Quelques informations à savoir :
- `HOST` est l'adresse où se trouve le service CEPH.
  Celle configurée est celle de VALERIA.
- `MY_IP` est la destination où les notifications sont envoyées.
  Par exemple, dans le cas de notifications AMQP avec RabbitMQ,
  `MY_IP = '<adresse-ip-ou-se-trouve-rabbitmq>'`
- Les noms, clés et ID ne sont que des exemples utilisés
  à des fins de tests, vous pouvez utiliser les valeurs
  que vous souhaitez


# Stocker un objet (ex. image)
1. Créer un bucket (s'il n'est pas déjà créé)
    - Le bucket est le "réservoir" de données d'un projet
    - voir `ceph/create_bucket.py`
1. Stockage d'un objet
    - voir `ceph/store_object.py`
1. Il devient ensuite possible de récupérer cet objet
    - Voir `ceph/get_object.py`
    - L'objet devrait se trouver dans `data/`

# Configuration des notifications
Pour ajouter une notification, il faut :
1. Créer un bucket 
   - Le bucket est le "réservoir" de données d'un projet
   - Voir `ceph/create_bucket.py`
2. Créer un topic
   - Un topic est un "sujet" à lequel on configure une action lors de
     l'arrivée d'une notification. Par exemple, c'est ici où l'on
     configure comment la notification sera envoyée et à quel addresse, soit par
     - HTTP
     - AMQP (message, ex. RabbitMQ)
     - Kafka
    - Voir `ceph/create_topic.py`
3. Créer une (configuration de) notification
   - On associe un évènement à un topic. Par exemple, on pourrait configurer une
     liaison entre un Topic et un évènement (création d'un nouvel objet).
     Donc à chaque nouvel objet, une notification est envoyée selon le topic (par HTTP, AMQP ou kafka)
   - Voir `ceph/create_notification.py`
     
4. Finalement stocker un objet pour déclencher la notification
   - Stockage un objet binaire quelconque (ex. une image)
   - Voir `ceph/put_object.py`
    
5. Les données des la notification reçue devraient ressembler aux données
    dans le fichier `data/example-response-from-ceph.json`

# RabbitMQ
Afin de tester les notifications avec RabbitMQ, il est nécessaire
de lancer une instance de ce dernier et d'écouter avec un autre service.

## Lancer RabbitMQ
La méthode la plus simple pour lancer RabbitMQ est avec docker :
```shell
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

Pour des méthodes alternatives, consultez https://www.rabbitmq.com/download.html

__N'oubliez__ pas de changer la configuration `RABBITMQ_IP` au besoin dans `config.py`.

## Écouter
RabbitMQ capture les messages qu'on lui envoie et les stocke dans une queue. 
Pour récupérer ces messages, il est nécessaire de "dépiler" la queue avec un service.
Un script Python a été développé à cette fin. 
Ce dernier se trouve à `/rabbitmq/listen.py`.
Il s'agit de le démarrer afin qu'il consome les messages qui se trouve dans
la queue de RabbitMQ.
Notez qu'il écoute sur le même "exchange" que celui configuré dans la notification AMQP de Ceph.

### Tester la réception de message
Il est pertinent de tester si votre instance de RabbitMQ peut bel et bien
recevoir des messages. Pour ce faire, exécuter le script `/rabbitmq/send.py`
alors que RabbitMQ et le script `/rabbitmq/listen.py` roule.
Vous devriez recevoir un message.