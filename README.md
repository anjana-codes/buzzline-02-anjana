# buzzline-02-anjana
Streaming data is often too big for any one machine. Apache Kafka is a popular streaming platform that uses publish-subscribe patterns:

Producers publish streaming data to topics
Consumers subscribe to topics to process data in real-time
We'll write Python producers and consumers to work with Kafka topics.

Kafka needs space - it's big.

It also comes from the Linux world. We'll use WSL on Windows machines.

## Introduction 

This project set up the example project and see how streaming analytics works using the Kafka streaming platform and the provided producer and consumer scripts. I have a 5 year old son. So I updated the producer to send questions for 5-year-old boys, including topics like food, dinosaurs, superheroes, favorite games, and snacks. Each message streams every 3 seconds. Also I enhanced the consumer to detect keywords like “dinosaur 🦕”, “superhero 🦸”, “food/snack 🍕”, and “game ⚽” and log them with special icons for easier visibility in real-time analytics.

### Name: Anjana Dhakal, 09/03/2025

## Objectives:
1. Understand Python Kafka producers.
2. Modify producers and consumers for real-time data streaming.
3. Perform basic real-time analytics using Kafka.

## Task 1. Install and Start Kafka (using WSL if Windows)

Before starting, ensure you have completed the setup tasks in <https://github.com/denisecase/buzzline-01-case> first.
Python 3.11 is required.

In this task, we will download, install, configure, and start a local Kafka service.

1. Install Windows Subsystem for Linux (Windows machines only)
2. Install Kafka Streaming Platform
3. Start the Kafka service (leave the terminal open).

For detailed instructions, see:

- [SETUP_KAFKA](SETUP_KAFKA.md)

## Task 2. Manage Local Project Virtual Environment

Open your project in VS Code and use the commands for your operating system to:

1. Create a Python virtual environment
2. Activate the virtual environment
3. Upgrade pip
4. Install from requirements.txt

### Windows

Open PowerShell terminal in VS Code (Terminal / New Terminal / PowerShell).

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip wheel setuptools
py -m pip install --upgrade -r requirements.txt
```

If you get execution policy error, run this first:
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Mac / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade -r requirements.txt
```

## Task 3. Start a Kafka Producer

Producers generate streaming data for our topics.

In VS Code, open a terminal.
Use the commands below to activate .venv, and start the producer.

Windows:

```shell
.venv\Scripts\activate
py -m producers.kafka_producer_anjana
```

Mac/Linux:

```zsh
source .venv/bin/activate
python3 -m producers.kafka_producer_anjana
```

## Task 4. Start a Kafka Consumer

Consumers process data from topics or logs in real time.

In VS Code, open a NEW terminal in your root project folder.
Use the commands below to activate .venv, and start the consumer.

Windows:

```shell
.venv\Scripts\activate
py -m consumers.kafka_consumer_anjana
```

Mac/Linux:

```zsh
source .venv/bin/activate
python3 -m consumers.kafka_consumer_anjana
```

## Later Work Sessions

When resuming work on this project:

1. Open the folder in VS Code.
2. Start the Kafka service.
3. Activate your local project virtual environment (.venv).

## Save Space

To save disk space, you can delete the .venv folder when not actively working on this project.
You can always recreate it, activate it, and reinstall the necessary packages later.
Managing Python virtual environments is a valuable skill.

## License

This project is licensed under the MIT License as an example project.
You are encouraged to fork, copy, explore, and modify the code as you like.
See the [LICENSE](LICENSE.txt) file for more.
