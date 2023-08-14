# DVC Demo

This project is meant for testing various DVC behaviour.

The project doesn't actually `do` anything, it is just a collection of Python files that pretend to train and deploy a model and strictly for exercising DVC.

# Pipeline

The three simulated stages are manifest, train, and deploy.  They are meant to simulate a typical workflow where manifest might log things like Docker container hashes, train would train a model, and deploy would convert the trained models to a format for deployment.
