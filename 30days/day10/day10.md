## 📅 Date
**29 November 2024**

## 📰 Resource

[SyftBox](https://syftbox-documentation.openmined.org/)

[Ring App](https://github.com/OpenMined/ring) 

## 🔖 My Learning

Today, I dove into more practical federated learning solutions. The goal of today's learning was to continue exploring the capabilities of the [SyftBox](https://syftbox-documentation.openmined.org/) library with an implementation of an application: **Ring App**. 

If you missed the introduction of the library, what is it, how to use it and how to install it, you can find it [here](../day8/day8.md), while the structure and APIs usage can be found [here](../day9/day9.md).


### The Ring App

During the first Hackaton sponsorized by OpenMined, on `24th October 2024`, I discovered for the first time the SyftBox library. There, I met my fellow [Sahani Pradeep](https://github.com/TensorSpd). 

After some meetings dedicated to understand the library and learn how to use it, with [Sahani Pradeep](https://github.com/TensorSpd), we worked on a custom version of the the so called [`Ring App`](https://github.com/OpenMined/ring), a simple application that allows users to do some basic statistical computations over their private and secret numbers. 

The app is built using the SyftBox APIs and I think it could be a really simple and easy way to demonstrate how to interact with the Syft network to send and receive messages.

Let's dive into it! -> Check the Explanation Notebook [here](ringapp/RingApp_Explanation_Notebook.ipynb) or the `main.py` code.
Our Entire code could be find here: [Ring App](ringapp/).

### How to use Ring App?
**EACH CLIENT**:
1. Create `<path_to>/SyftBox/datasites/<your@email.com>/privatefolder` folder.
2. Create a `_syftperm` file for the configuration of the permission of this folder in order to have it strictly private. Example of the `_syftperm` file content:
   ```
   {"admin": ["<your@email.com>"], "read": ["<your@email.com>"], "write": ["<your@email.com>"], "filepath": "<path_to>/SyftBox/datasites/<your@email.com>/privatefolder/_.syftperm", "terminal": false}
    ```
3. In the `<path_to>/SyftBox/datasites/<your@email.com>/privatefolder` folder, create your `secret.txt` file where you store your secret numbers. Example of the ``secret.txt`` file content:
    ```txt
    123
    ```
3. Copy the folder `ringapp` in your SyftBox project: `<path_to>/SyftBox/apis/`
4. Run your `SyftBox` client, by `curl -LsSf https://syftbox.openmined.org/install.sh | sh`.
Then, it's sufficient that only one client triggers the `ringapp` , how?
5. Create `data.json` file and put it in the `<path_to>/SyftBox/datasites/<your@email.com>/app_pipelines/ringapp/running/` folder. Then, the first client should see the `data.json` file disappearing from the `running` folder.

### Results 
Once the ring app end into the last client (datasite) of the ring, in the `<path_to>/SyftBox/datasites/<last_person_in_the_ring@email.com>/app_pipelines/ringapp/done` you should see the result of the computation. It corresponds to the total sum of the secret numbers of all the users in the ring.

Check it out and let us know if it worked!

## 📮 Post 

[📘 LinkedIn Post]()

------
The _**Federated Learning Term of the Day**_ is ****
> [!NOTE]
> 
