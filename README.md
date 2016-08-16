Serial Set Inventory
====================

About
-----

This is a complete rewrite of the existing [Serial Set Inventory](http://digital.library.unt.edu/govdocs/ssi/) site hosted by the University of North Texas.
 
A work in progress.

Requirements
------------

* Python ~= 2.7.0
* Django ~= 1.8.0

Developing
----------

1. [Install Docker](http://docs.docker.com/installation/).

2. Install Docker Compose.
    ```sh
        $ pip install docker-compose
    ```
    
3. Clone the repository.
    ```sh
        $ git clone https://github.com/unt-libraries/serial-set-inventory
    ```

4. Start the container as a daemon.
    ```sh
        $ docker-compose up -d
        # Use 'docker-compose stop' to stop the container.
    ```
    At this point you should be able to access your local instance of the admin site by visiting `<dockerhost>:8000/admin`.

5. Create a superuser for access to the admin sites.
    ```sh
        $ docker-compose run manage createsuperuser
    ```
    

        
License
-------

See LICENSE.txt.

Contributors
------------

* [Jason Ellis](https://github.com/jason-ellis)