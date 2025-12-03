ETHAN LAMPONE

HOMEWORK 5

CSC 362 - AI

6 NOVEMBER 2025

# HOMEWORK 5 --- DESCRIPTION DETAILS

To begin HW5, we need to get a couple of files. The files can be found from **Module 5** in the course GitHub:
  - **car_dqn_visualizer.py** --> This is the main file that we will be editing and running.
  - **car_DQN.ipynb** --> This is a Python notebook that explains the Python file above.

## PART 1 --> The Exploration-Exploitation Trade-Off (Epislon Decay)

To  begin Part I, we need to explore the **.py** file and find where we will focus most of our work on. This will be the hyperparameters. Below is an image of what the environment looks like (**LINES 522-537**):

  <img width="612" height="325" alt="image" src="https://github.com/user-attachments/assets/2f21240c-e1f6-4b5f-8a4b-af3eb3428cd7" />

As we can see, we have the following hyperparameters that we will primarily focus on for this assignment:
  - **Gamma (Discount Factor)**
  - **Learning Rate (Alpha)**
  - **Epsilon Start**
  - **Epsilon End**
  - **Epsilon Decay**

To begin, we are going to tweak the value(s) of **Epsilon Decay** to see the effects different values have on the car and its exploration/exploitation. We are also going to lock all the other values to their default, which are below:
  - **Gamma (Discount Factor)** --> 0.99
  - **Learning Rate (Alpha)** --> 0.0005
  - **Epsilon Start** --> 1.0
  - **Epsilon End** --> 0.2
  - **Epsilon Decay** --> 5000 **PRESET VALUE!!!!!!!!!**

For Part I, we are asked to do the following:

  <img width="592" height="265" alt="image" src="https://github.com/user-attachments/assets/08fdf4a4-174e-4bda-bac4-650b45c5eafa" />

We should be using three different values for **Epsilon-Decay Rate**. One should be very high, one should be very low, and one should be in the middle. The expected outcomes from using these three values are explained below, respectively:

  <img width="808" height="437" alt="image" src="https://github.com/user-attachments/assets/05441fdc-a41f-403d-af48-1ec7780605db" />

With that being said, lets first look at the high **Epsilon-Decay Value**:

  






## PART 2 --> The Planning Horizon

After looking at the many different effects varying epsilon values have, 
